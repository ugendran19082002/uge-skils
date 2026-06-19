#!/usr/bin/env python3
"""
Regression + behavior tests for the ugendran CLI.

Goal: prove the advanced layer (build / planner / parallel executor / resumable
memory / install / discontinue / review gate) works AND that existing logic
(do/new/status/skills/keyword fallback) is not disturbed.

All tests run OFFLINE — detect_llm is forced to the keyword fallback so no real
LLM CLI is invoked. Each test isolates state into a temp directory.

Run:  python3 -m unittest discover -s tests -v
      (or)  python3 tests/test_ugendran.py
"""
import io
import os
import sys
import json
import tempfile
import unittest
import contextlib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import ugendran as u  # noqa: E402

OFFLINE_LLM = {"name": "Keyword-Fallback", "cmd": None, "icon": "🟡"}


def quiet(fn, *a, **k):
    """Run fn capturing stdout so test output stays clean. Returns captured text."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        fn(*a, **k)
    return buf.getvalue()


class Base(unittest.TestCase):
    def setUp(self):
        # Force offline so no real LLM call happens.
        self._orig_detect = u.detect_llm
        self._orig_call = u.call_llm
        u.detect_llm = lambda: OFFLINE_LLM

        # Redirect all writable state into a temp dir; ROOT stays real so the
        # skill catalog (templates) can still be read/copied.
        self.tmp = tempfile.TemporaryDirectory()
        base = Path(self.tmp.name)
        self._orig = (u.UGDIR, u.ARCHIVE_DIR, u.PROJECTS)
        u.UGDIR = base / ".ugendran"
        u.ARCHIVE_DIR = base / ".ugendran" / "archive"
        u.PROJECTS = base / ".ugendran" / "projects"
        u.ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
        u.PROJECTS.mkdir(parents=True, exist_ok=True)

    def tearDown(self):
        u.detect_llm = self._orig_detect
        u.call_llm = self._orig_call
        u.UGDIR, u.ARCHIVE_DIR, u.PROJECTS = self._orig
        self.tmp.cleanup()

    def make_project(self, name="p", skills=("api-design", "authentication-design")):
        proj = {
            "name": name, "idea": "test idea", "type": "web", "status": "active",
            "created": u.ts(),
            "skills": {s: {"status": "pending", "started": None, "done": None} for s in skills},
            "log": [{"ts": u.ts(), "event": "project_created", "detail": "test idea"}],
        }
        u.save_project(name, proj)
        return proj


class TestKeywordFallback(Base):
    """Existing logic must keep working unchanged."""

    def test_auth_intent(self):
        self.assertEqual(u.keyword_fallback("add login with jwt")["skill"], "authentication-design")

    def test_cache_intent(self):
        self.assertEqual(u.keyword_fallback("need redis cache with ttl")["skill"], "caching-strategy")

    def test_vague_defaults_to_prd(self):
        self.assertEqual(u.keyword_fallback("just something")["skill"], "prd-generation")

    def test_all_skills_count(self):
        self.assertEqual(len(u.all_skills()), 88)

    def test_skill_path_resolves(self):
        self.assertTrue(u.skill_path("caching-strategy").exists())

    def test_new_domain_skill_intents(self):
        cases = {
            "add stripe subscription billing": "payments-billing",
            "send push notification and email": "notification-system",
            "websocket realtime presence": "realtime-architecture",
            "add i18n locale translation rtl": "internationalization",
            "build an etl data pipeline with airflow": "data-pipeline-design",
            "feature flag gradual rollout": "feature-flag-management",
            "pact consumer contract test": "contract-testing",
            "api gateway rate limit routing": "api-gateway-design",
            "mixpanel funnel event tracking": "product-analytics",
        }
        for req, expected in cases.items():
            self.assertEqual(u.keyword_fallback(req)["skill"], expected, req)


class TestCatalogSync(Base):
    """The CLI catalog must stay in lockstep with the generator — no drift."""

    def test_cli_matches_generator(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "skills_data",
            str(Path(__file__).resolve().parent.parent / "_generator" / "skills_data.py"))
        sd = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(sd)
        gen = set(s["slug"] for s in sd.ALL_SKILLS)
        cli = set(u.all_skills())
        self.assertEqual(gen, cli, f"drift: gen-cli={gen-cli}, cli-gen={cli-gen}")

    def test_every_skill_has_description_and_folder(self):
        for s in u.all_skills():
            self.assertIn(s, u.SKILL_DESCRIPTIONS, f"{s} missing description")
            self.assertTrue(u.skill_path(s) and u.skill_path(s).exists(), f"{s} missing folder")


class TestProjectTypes(Base):
    def test_eighteen_types(self):
        self.assertEqual(len(u.PROJECT_PROFILES), 18)

    def test_profile_skills_all_valid(self):
        valid = set(u.all_skills())
        for t, skills in u.PROJECT_PROFILES.items():
            for s in skills:
                self.assertIn(s, valid, f"{t} -> {s} not a real skill")

    def test_type_detection(self):
        cases = {
            "online store with cart and checkout": "ecommerce",
            "banking app with wallet and ledger": "fintech",
            "patient records system, HIPAA": "healthcare",
            "iot sensor telemetry fleet": "iot",
            "multiplayer game matchmaking": "gaming",
            "two-sided marketplace buyers and sellers": "marketplace",
            "command line developer tool / sdk": "cli",
            "internal developer platform paved road": "platform",
        }
        for idea, expected in cases.items():
            self.assertEqual(u.detect_type_keyword(idea), expected, idea)


class TestPlanner(Base):
    def test_plan_fallback_orders_by_category(self):
        proj = self.make_project(skills=["ci-cd-pipeline", "prd-generation", "api-design"])
        plan = u.plan_fallback("build it", proj)
        cats = [u.skill_category(s) for w in plan["waves"] for s in w["skills"]]
        # product must come before architecture before devops
        self.assertLess(cats.index("product"), cats.index("architecture"))
        self.assertLess(cats.index("architecture"), cats.index("devops"))

    def test_plan_fallback_parallel_grouping(self):
        proj = self.make_project(skills=["api-design", "security-architecture"])
        plan = u.plan_fallback("x", proj)
        # both are architecture → same wave (parallel)
        self.assertEqual(len(plan["waves"]), 1)
        self.assertEqual(set(plan["waves"][0]["skills"]), {"api-design", "security-architecture"})

    def test_plan_fallback_resume_when_done_is_empty(self):
        proj = self.make_project(skills=["api-design"])
        proj["skills"]["api-design"]["status"] = "done"
        plan = u.plan_fallback("continue", proj)
        self.assertEqual(plan["waves"], [])

    def test_ai_plan_build_offline_uses_fallback(self):
        proj = self.make_project(skills=["api-design"])
        plan = u.ai_plan_build("anything", proj, OFFLINE_LLM)
        self.assertIn("waves", plan)
        self.assertTrue(any("api-design" in w["skills"] for w in plan["waves"]))


class TestMemory(Base):
    def test_digest_lists_done_and_pending(self):
        proj = self.make_project(skills=["api-design", "authentication-design"])
        proj["skills"]["api-design"]["status"] = "done"
        digest = u.build_memory_digest(proj)
        self.assertIn("api-design", digest)
        self.assertIn("authentication-design", digest)
        self.assertIn("Completed", digest)

    def test_state_md_written(self):
        proj = self.make_project()
        u.write_state_md("p", proj)
        state = u.UGDIR / "workspaces" / "p" / "STATE.md"
        self.assertTrue(state.exists())
        self.assertIn("Resume", state.read_text())


class TestExecutor(Base):
    def test_apply_skill_core_writes_artifacts(self):
        proj = self.make_project()
        r = u.apply_skill_core("api-design", "design the api", proj, OFFLINE_LLM, "p")
        self.assertEqual(r["skill"], "api-design")
        self.assertGreater(r["score"], 0)
        spec = u.UGDIR / "workspaces" / "p" / "skills" / "api-design" / "SPEC.md"
        self.assertTrue(spec.exists())
        self.assertIn("api", spec.read_text().lower())

    def test_commit_skill_marks_done_and_archives(self):
        proj = self.make_project()
        r = {"skill": "api-design", "score": 85, "spec_file": "x", "category": "architecture"}
        u.commit_skill(proj, "p", r, "req", OFFLINE_LLM)
        self.assertEqual(proj["skills"]["api-design"]["status"], "done")
        archives = list(u.ARCHIVE_DIR.glob("p_api-design_*.json"))
        self.assertEqual(len(archives), 1)
        rec = json.loads(archives[0].read_text())
        self.assertEqual(rec["validation_score"], 85)


class TestBuildEndToEnd(Base):
    def test_full_build_reaches_100_percent(self):
        quiet(u.cmd_build, ["proj", "B2B SaaS with login and CI/CD"])
        proj = u.load_project("proj")
        self.assertIsNotNone(proj)
        done = [s for s, v in proj["skills"].items() if v["status"] == "done"]
        # every planned skill should be delivered
        pending = [s for s, v in proj["skills"].items() if v["status"] == "pending"]
        self.assertEqual(pending, [])
        self.assertGreater(len(done), 0)
        # continuous archiving produced one record per skill
        self.assertGreaterEqual(len(list(u.ARCHIVE_DIR.glob("proj_*.json"))), len(done))
        # resumable memory exists
        self.assertTrue((u.UGDIR / "workspaces" / "proj" / "STATE.md").exists())

    def test_resume_builds_nothing_when_done(self):
        quiet(u.cmd_build, ["proj2", "simple web app with auth"])
        out = quiet(u.cmd_build, ["proj2", "continue"])
        self.assertIn("Nothing left to build", out)

    def test_review_flag_is_non_interactive_safe(self):
        # Non-tty → _confirm returns default True → build proceeds without hanging.
        out = quiet(u.cmd_build, ["proj3", "web app with auth", "--review"])
        self.assertIn("review (asks after each skill)", out)
        self.assertEqual([s for s, v in u.load_project("proj3")["skills"].items()
                          if v["status"] == "pending"], [])


class TestDiscontinue(Base):
    def test_kill_writes_runbook_and_archives(self):
        self.make_project("dead")
        quiet(u.cmd_kill, ["dead"])
        proj = u.load_project("dead")
        self.assertEqual(proj["status"], "archived")
        runbooks = list(u.ARCHIVE_DIR.glob("project_dead_*/DISCONTINUATION.md"))
        self.assertEqual(len(runbooks), 1)
        self.assertIn("Decommission", runbooks[0].read_text())


class TestHybridOpenSpec(Base):
    def test_normalize_guarantees_structure(self):
        # Empty input must still yield a fully-formed, renderable change.
        data = u.normalize_change_data({}, "payments-billing", "add billing")
        self.assertTrue(data["capability"])
        self.assertTrue(data["requirements"])
        for r in data["requirements"]:
            self.assertIn("SHALL", r["shall"])
            self.assertGreaterEqual(len(r["scenarios"]), 1)
            for s in r["scenarios"]:
                self.assertTrue(s["when"] and s["then"])
        self.assertTrue(data["tasks"] and data["tasks"][0]["items"])

    def test_render_writes_openspec_files(self):
        ws = u.UGDIR / "workspaces" / "p"
        data = u.normalize_change_data({}, "api-design", "design api")
        cdir = u.render_openspec_change(ws, "api-design-x", data)
        self.assertTrue((cdir / "proposal.md").exists())
        self.assertTrue((cdir / "tasks.md").exists())
        spec = (cdir / "specs" / data["capability"] / "spec.md").read_text()
        self.assertIn("## ADDED Requirements", spec)
        self.assertIn("### Requirement:", spec)
        self.assertIn("- **WHEN**", spec)
        self.assertIn("- **THEN**", spec)
        self.assertTrue((u.UGDIR / "workspaces" / "p" / "openspec" / "config.yaml").exists())

    @unittest.skipUnless(u.openspec_available(), "openspec CLI not installed")
    def test_emitted_change_passes_real_validate(self):
        self.make_project("p")
        r = u.emit_and_validate_openspec("authentication-design", "secure login",
                                         u.load_project("p"), OFFLINE_LLM, "p")
        self.assertTrue(r["valid"], r["issues"])
        self.assertGreaterEqual(r["requirements"], 1)
        self.assertGreaterEqual(r["scenarios"], 1)


class TestApply(Base):
    def test_parse_emitted_files(self):
        text = ("<<<FILE: a/b.py>>>\nprint(1)\n<<<END>>>\n"
                "<<<FILE: c.txt>>>\nhi\n<<<END>>>\n<<<TEST: pytest -q>>>")
        files, cmd = u.parse_emitted_files(text)
        self.assertEqual([f[0] for f in files], ["a/b.py", "c.txt"])
        self.assertEqual(cmd, "pytest -q")

    def test_parse_test_none(self):
        _, cmd = u.parse_emitted_files("<<<FILE: x>>>\ny\n<<<END>>>\n<<<TEST: NONE>>>")
        self.assertEqual(cmd, "")

    def test_safe_write_rejects_traversal(self):
        tgt = u.UGDIR / "t"
        tgt.mkdir(parents=True, exist_ok=True)
        written, rejected = u.safe_write_files(
            tgt, [("ok.py", "1"), ("../escape.py", "2"), ("/abs.py", "3")])
        self.assertIn("ok.py", written)
        self.assertIn("../escape.py", rejected)
        self.assertFalse((tgt.parent / "escape.py").exists())

    def test_apply_implements_and_verifies(self):
        proj = self.make_project("ap", skills=["api-design"])
        proj["skills"]["api-design"]["status"] = "done"
        u.save_project("ap", proj)
        (u.UGDIR / "workspaces" / "ap").mkdir(parents=True, exist_ok=True)
        osr = u.emit_and_validate_openspec("api-design", "add add(a,b)", proj, OFFLINE_LLM, "ap")
        target = u.UGDIR / "workspaces" / "ap" / "code"

        u.detect_llm = lambda: {"name": "Mock", "cmd": "mock", "icon": "🧪"}
        u.call_llm = lambda *a, **k: (
            "<<<FILE: m.py>>>\ndef add(a,b):\n    return a+b\n<<<END>>>\n"
            '<<<TEST: python3 -c "import m; assert m.add(2,3)==5">>>')
        try:
            quiet(u.cmd_apply, ["ap", osr["change"], "--path", str(target)])
        finally:
            u.detect_llm = lambda: OFFLINE_LLM
        self.assertTrue((target / "m.py").exists())
        # tasks checked off only happens on pass
        tasks = (u.UGDIR / "workspaces" / "ap" / "openspec" / "changes" / osr["change"] / "tasks.md").read_text()
        self.assertIn("- [x]", tasks)
        self.assertTrue(list(u.ARCHIVE_DIR.glob("ap_apply_*.json")))


class TestInstall(Base):
    def test_install_creates_executable_wrapper(self):
        home = tempfile.TemporaryDirectory()
        orig_home = os.environ.get("HOME")
        os.environ["HOME"] = home.name
        try:
            quiet(u.cmd_install, [])
            link = Path(home.name) / ".local" / "bin" / "ugendran"
            self.assertTrue(link.exists())
            self.assertIn("ugendran.py", link.read_text())
            self.assertTrue(os.access(link, os.X_OK))
        finally:
            if orig_home is not None:
                os.environ["HOME"] = orig_home
            home.cleanup()


if __name__ == "__main__":
    unittest.main(verbosity=2)
