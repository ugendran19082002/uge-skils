#!/usr/bin/env python3
"""
ugendran — Smart OpenSpec Skills CLI
================================
THE BIG IDEA:
  ugendran do <project> "I want to add authentication"
  → AI picks the right skill automatically
  → Applies it (generates spec + artifacts)
  → Archives it as DONE
  → Suggests next skill
  All in ONE command. No manual skill selection needed.

Commands:
  do        <project> "<what you want>"    ★ AUTO: AI picks skill → apply → archive
  new       <project> "<idea>"             Create new project
  audit     <path> [project]              Audit existing project
  archive   <project> <skill>             Manual skill archive (run twice)
  status    [project]                     Dashboard
  history   <project>                     Timeline
  suggest   <project>                     Next skill suggestion
  skills    [category]                    List all 78 skills
  kill      <project>                     Discontinue & archive project
"""

import os, sys, json, re, shutil, textwrap
from datetime import datetime
from pathlib import Path

# ─── Paths ───────────────────────────────────────────────────────────────────
ROOT        = Path(__file__).parent
ARCHIVE_DIR = ROOT / ".ugendran" / "archive"
PROJECTS    = ROOT / ".ugendran" / "projects"

ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
PROJECTS.mkdir(parents=True, exist_ok=True)

# ─── Colors ──────────────────────────────────────────────────────────────────
COLORS = {
    "green":  "\033[92m", "yellow": "\033[93m", "red":   "\033[91m",
    "blue":   "\033[94m", "cyan":   "\033[96m", "bold":  "\033[1m",
    "reset":  "\033[0m",  "dim":    "\033[2m",  "magenta": "\033[95m",
}
def c(text, color): return f"{COLORS[color]}{text}{COLORS['reset']}"
def bold(t):   return c(t, "bold")
def dim(t):    return c(t, "dim")
def ok(t):     return c(f"✅ {t}", "green")
def warn(t):   return c(f"⚠️  {t}", "yellow")
def err(t):    return c(f"❌ {t}", "red")
def info(t):   return c(f"ℹ️  {t}", "cyan")
def ai_tag(t): return c(f"🤖 {t}", "magenta")
def ts():      return datetime.now().strftime("%Y-%m-%d %H:%M")

# ─── All 78 Skills ───────────────────────────────────────────────────────────
SKILL_MAP = {
    "product":      ["business-analysis","market-research","prd-generation",
                     "requirements-analysis","proposal-creation","user-story-generation",
                     "risk-analysis","cost-estimation","roadmap-planning"],
    "architecture": ["design-document","architecture-review","frontend-architecture",
                     "backend-architecture","api-design","database-design",
                     "security-architecture","scalability-planning","event-driven-architecture",
                     "multi-tenant-architecture","domain-driven-design","microservices-governance"],
    "frontend":     ["ui-ux-design","component-design","state-management","frontend-testing",
                     "frontend-optimization","accessibility-review","design-system"],
    "backend":      ["service-design","authentication-design","database-optimization",
                     "caching-strategy","background-jobs","api-contract-design",
                     "file-storage-design","search-architecture"],
    "ai":           ["ai-agent-design","rag-architecture","prompt-engineering","model-selection",
                     "ai-evaluation","llmops","vector-database-design","ai-monitoring",
                     "model-finetuning","guardrails-design"],
    "testing":      ["testing-strategy","unit-testing","integration-testing",
                     "performance-testing","e2e-testing","security-testing"],
    "devops":       ["infra-design","docker-architecture","docker-compose-design",
                     "kubernetes-planning","nginx-reverse-proxy","ssl-management",
                     "ci-cd-pipeline","observability-design","backup-recovery",
                     "server-hardening","secrets-management","disaster-recovery",
                     "infrastructure-as-code"],
    "security":     ["threat-modeling","compliance-audit","vulnerability-management",
                     "access-control-design"],
    "maintenance":  ["troubleshooting","bug-investigation","refactoring-planning",
                     "migration-planning","release-planning","documentation-generator",
                     "incident-response","monitoring-alerting","technical-debt-management"],
}

# ─── Natural Language → Skill Mapping ────────────────────────────────────────
# Key: keyword in user's sentence → matched skill (priority order)
INTENT_MAP = [
    # Authentication / Login
    (["login","auth","sign in","signup","password","jwt","token","oauth","sso","mfa","otp",
      "user account","registration","logout","session","passkey"],             "authentication-design"),
    # API
    (["api","endpoint","rest","graphql","grpc","openapi","swagger","webhook"],  "api-design"),
    (["api contract","api spec","contract test","consumer driven"],            "api-contract-design"),
    # Database
    (["database","db schema","table","migration","sql","postgres","mysql",
      "mongodb","data model","erd","entity"],                                   "database-design"),
    (["slow query","index","n+1","query plan","db performance","database tuning"],"database-optimization"),
    # Caching
    (["cache","redis","memcache","caching","cdn","ttl","invalidat"],           "caching-strategy"),
    # Search
    (["search","elasticsearch","opensearch","full text","vector search","semantic search"],
                                                                               "search-architecture"),
    # File / Storage
    (["file upload","s3","object storage","media","image upload","file storage",
      "video","cdn upload"],                                                    "file-storage-design"),
    # Background / Queue
    (["background job","queue","worker","celery","sidekiq","async task","cron",
      "scheduler","job processing","message queue","rabbitmq","kafka"],         "background-jobs"),
    # AI / LLM
    (["ai agent","llm agent","autonomous agent","agentic","tool call","function call"],
                                                                               "ai-agent-design"),
    (["rag","retrieval","embeddings","vector","knowledge base","grounding"],    "rag-architecture"),
    (["prompt","system prompt","few shot","chain of thought","prompt template"],"prompt-engineering"),
    (["fine tune","finetune","lora","qlora","train model","model training"],    "model-finetuning"),
    (["ai monitor","model drift","quality drift","ai quality"],                "ai-monitoring"),
    (["guardrail","content filter","safety filter","input validation ai",
      "output filter","toxicity"],                                              "guardrails-design"),
    (["llmops","model deploy","prompt version","llm production"],              "llmops"),
    (["ai eval","model eval","eval harness","golden set","llm judge"],         "ai-evaluation"),
    (["model select","which model","gpt vs claude","model choice"],            "model-selection"),
    (["vector db","pinecone","weaviate","chroma","qdrant","pgvector","hnsw"],  "vector-database-design"),
    # Testing
    (["unit test","test coverage","tdd","mock","stub","pytest","jest"],        "unit-testing"),
    (["integration test","testcontainer","boundary test"],                     "integration-testing"),
    (["end to end","e2e","playwright","cypress","selenium","user journey test"],"e2e-testing"),
    (["load test","performance test","stress test","k6","locust","gatling",
      "slo test"],                                                              "performance-testing"),
    (["security test","pen test","penetration","sast","dast","owasp"],        "security-testing"),
    (["test strategy","test plan","test pyramid","testing approach"],          "testing-strategy"),
    # DevOps
    (["docker","dockerfile","container","containerize"],                        "docker-architecture"),
    (["docker compose","compose","local stack","multi container"],             "docker-compose-design"),
    (["kubernetes","k8s","helm","deployment","pod","namespace","rbac kube"],   "kubernetes-planning"),
    (["ci cd","pipeline","github actions","gitlab ci","jenkins","build pipeline",
      "deploy pipeline"],                                                       "ci-cd-pipeline"),
    (["terraform","pulumi","cdk","infrastructure as code","iac","cloudformation"],
                                                                               "infrastructure-as-code"),
    (["nginx","reverse proxy","load balancer proxy","ingress"],                "nginx-reverse-proxy"),
    (["ssl","tls","certificate","https","lets encrypt","acme"],                "ssl-management"),
    (["monitoring","alerting","alert","pagerduty","slo","sli","dashboard"],    "monitoring-alerting"),
    (["observability","logging","tracing","opentelemetry","metrics","datadog",
      "grafana","prometheus"],                                                  "observability-design"),
    (["backup","restore","recovery","disaster","rpo","rto"],                   "backup-recovery"),
    (["server hardening","cis benchmark","ssh hardening","firewall","patch"],  "server-hardening"),
    (["secrets","vault","secret manager","api key rotation","credentials",
      "env var secret"],                                                        "secrets-management"),
    (["disaster recovery","failover","dr plan","multi region","active active"], "disaster-recovery"),
    (["cloud infra","infrastructure design","aws setup","gcp setup","azure setup",
      "vpc","network"],                                                         "infra-design"),
    # Security
    (["threat model","stride","attack surface","security design","trust boundary"],
                                                                               "threat-modeling"),
    (["compliance","gdpr","hipaa","soc2","iso 27001","audit"],                 "compliance-audit"),
    (["vulnerability","cve","patch","security scan","snyk","dependabot"],      "vulnerability-management"),
    (["access control","rbac","permission","role","authorization","abac"],     "access-control-design"),
    # Architecture
    (["design doc","technical design","tdd document","rfc","adr"],             "design-document"),
    (["architecture review","system review","quality attribute","atam"],       "architecture-review"),
    (["frontend architecture","fe architecture","rendering strategy","nextjs arch",
      "react architecture"],                                                    "frontend-architecture"),
    (["backend architecture","service boundary","microservice","monolith",
      "service map"],                                                           "backend-architecture"),
    (["event driven","events","kafka arch","event sourcing","saga","outbox",
      "pub sub","message broker"],                                              "event-driven-architecture"),
    (["multi tenant","tenant isolation","saas architecture","per tenant"],     "multi-tenant-architecture"),
    (["ddd","domain driven","bounded context","aggregate","ubiquitous language",
      "context map"],                                                           "domain-driven-design"),
    (["microservice governance","service catalog","paved road","service standard"],
                                                                               "microservices-governance"),
    (["scale","scaling","horizontal scale","autoscale","capacity","load plan",
      "throughput","bottleneck"],                                               "scalability-planning"),
    # Frontend
    (["ui design","ux design","wireframe","prototype","figma","user research",
      "usability"],                                                             "ui-ux-design"),
    (["component","ui component","storybook","design token","reusable component"],
                                                                               "component-design"),
    (["state management","redux","zustand","context api","react query","swr",
      "global state"],                                                          "state-management"),
    (["frontend test","component test","testing library","vitest","react test"],
                                                                               "frontend-testing"),
    (["performance","lcp","cls","inp","core web vitals","lighthouse","bundle size",
      "code split"],                                                            "frontend-optimization"),
    (["accessibility","wcag","aria","screen reader","a11y","keyboard nav"],    "accessibility-review"),
    (["design system","token","component library","storybook system","design guide"],
                                                                               "design-system"),
    # Product
    (["prd","product requirement","product spec","feature spec"],              "prd-generation"),
    (["market research","competitor","tam","sam","market size","positioning"],  "market-research"),
    (["business analysis","stakeholder","business case","process map","gap analysis"],
                                                                               "business-analysis"),
    (["requirements","srs","acceptance criteria","functional requirement",
      "non functional"],                                                        "requirements-analysis"),
    (["proposal","sow","statement of work","bid","quote"],                     "proposal-creation"),
    (["user story","story","backlog","sprint","invest","given when then"],     "user-story-generation"),
    (["risk","risk register","risk analysis","mitig","contingency"],           "risk-analysis"),
    (["cost estimate","effort estimate","tco","pert","story point","budget"],  "cost-estimation"),
    (["roadmap","now next later","priorit","rice","wsjf","backlog plan"],      "roadmap-planning"),
    # Maintenance
    (["debug","troubleshoot","diagnose","root cause","investigate"],           "troubleshooting"),
    (["bug","fix bug","bug report","regression","defect"],                    "bug-investigation"),
    (["refactor","clean code","tech debt cleanup","code quality improve"],     "refactoring-planning"),
    (["migrate","migration","data migration","platform migration","zero downtime",
      "dual write"],                                                            "migration-planning"),
    (["release","deploy release","release plan","feature flag","go live",
      "launch checklist"],                                                      "release-planning"),
    (["documentation","docs","readme","runbook","wiki","api docs"],            "documentation-generator"),
    (["incident","outage","postmortem","on call","sev1","sev2","page"],        "incident-response"),
    (["alert","alert fatigue","runbook","on call burnout","pagerduty setup"],  "monitoring-alerting"),
    (["tech debt","technical debt","legacy","rewrite plan","deprecat"],        "technical-debt-management"),
]

PROJECT_PROFILES = {
    "web":     ["prd-generation","api-design","backend-architecture","frontend-architecture",
                "database-design","authentication-design","security-architecture",
                "testing-strategy","ci-cd-pipeline","docker-architecture","observability-design"],
    "ai":      ["ai-agent-design","rag-architecture","prompt-engineering","model-selection",
                "guardrails-design","ai-monitoring","ai-evaluation","llmops",
                "api-design","testing-strategy","ci-cd-pipeline"],
    "mobile":  ["prd-generation","ui-ux-design","api-design","authentication-design",
                "testing-strategy","ci-cd-pipeline","accessibility-review"],
    "data":    ["database-design","database-optimization","search-architecture",
                "vector-database-design","observability-design","backup-recovery",
                "api-contract-design"],
    "saas":    ["market-research","prd-generation","multi-tenant-architecture","api-design",
                "authentication-design","security-architecture","compliance-audit",
                "scalability-planning","ci-cd-pipeline","monitoring-alerting","incident-response"],
    "startup": ["market-research","business-analysis","prd-generation","user-story-generation",
                "api-design","docker-architecture","ci-cd-pipeline","testing-strategy"],
}

# ─── Helpers ─────────────────────────────────────────────────────────────────
def skill_path(skill):
    for cat, skills in SKILL_MAP.items():
        if skill in skills:
            return ROOT / cat / skill
    return None

def all_skills():
    return [s for ss in SKILL_MAP.values() for s in ss]

def skill_category(skill):
    return next((cat for cat, ss in SKILL_MAP.items() if skill in ss), "?")

def project_file(name): return PROJECTS / f"{name}.json"

def load_project(name):
    f = project_file(name)
    return json.loads(f.read_text()) if f.exists() else None

def save_project(name, data):
    project_file(name).write_text(json.dumps(data, indent=2))

def detect_project_type(idea):
    lo = idea.lower()
    if any(k in lo for k in ["ai","llm","gpt","agent","chat","ml","model","rag"]): return "ai"
    if any(k in lo for k in ["mobile","ios","android","flutter","react native"]):  return "mobile"
    if any(k in lo for k in ["saas","subscription","tenant","multi-tenant"]):      return "saas"
    if any(k in lo for k in ["data","analytics","pipeline","warehouse","etl"]):    return "data"
    if any(k in lo for k in ["startup","mvp","launch","market"]):                  return "startup"
    return "web"

# ─── ★ CORE: Natural Language → Skill ────────────────────────────────────────
def match_skill(sentence: str) -> tuple[str | None, float]:
    """
    Parse a free-form sentence and return (best_skill, confidence_0_to_1).
    Uses keyword scoring: more keyword hits = higher confidence.
    """
    lo = sentence.lower()
    scores = {}
    for keywords, skill in INTENT_MAP:
        hits = sum(1 for kw in keywords if kw in lo)
        if hits > 0:
            scores[skill] = scores.get(skill, 0) + hits / len(keywords)

    if not scores:
        return None, 0.0

    best   = max(scores, key=scores.get)
    conf   = min(scores[best] * 2, 1.0)   # normalise to 0–1
    return best, round(conf, 2)

def top_skill_matches(sentence: str, n=3):
    """Return top N (skill, confidence) pairs."""
    lo = sentence.lower()
    scores = {}
    for keywords, skill in INTENT_MAP:
        hits = sum(1 for kw in keywords if kw in lo)
        if hits > 0:
            scores[skill] = scores.get(skill, 0) + hits / len(keywords)
    ranked = sorted(scores.items(), key=lambda x: -x[1])[:n]
    return [(sk, round(min(sc*2, 1.0), 2)) for sk, sc in ranked]

# ─── Skill Applier: reads SKILL.md + templates → generates spec in workspace ──
def apply_skill(project_name: str, skill: str, user_request: str) -> Path:
    """
    Copy skill templates to workspace and pre-fill with context.
    Returns the path to the generated workspace folder.
    """
    src  = skill_path(skill)
    dest = ROOT / ".ugendran" / "workspaces" / project_name / "skills" / skill

    if dest.exists(): shutil.rmtree(dest)
    if src and src.exists():
        shutil.copytree(src, dest)

    # Generate a quick context file with the user's request
    context_file = dest / "CONTEXT.md"
    context_file.write_text(
        f"# Applied: {skill}\n\n"
        f"**Project:** {project_name}\n"
        f"**Request:** {user_request}\n"
        f"**Applied At:** {ts()}\n\n"
        f"## What to do\n\n"
        f"1. Open `SKILL.md` — read the Capabilities & Workflow\n"
        f"2. Open `prompts/prompts.md` — copy prompts into your AI\n"
        f"3. Fill `templates/` — use templates as your output structure\n"
        f"4. Check `checklist.md` — every gate must pass before you're done\n\n"
        f"## Your Request\n\n> {user_request}\n"
    )
    return dest

# ─── CMD: do ★ THE MAIN AUTO COMMAND ─────────────────────────────────────────
def cmd_do(args):
    """
    ugendran do <project-name> "I want to add authentication to my app"

    Flow:
    1. Read the user's sentence
    2. AI picks the best matching skill (with confidence %)
    3. Show top 3 candidates — confirm or pick
    4. Apply the skill (copy templates → workspace)
    5. Mark as IN-PROGRESS → immediately DONE (auto-archive)
    6. Suggest next skill
    """
    if len(args) < 2:
        print(err("Usage: ugendran do <project-name> \"what you want to do\""))
        print(dim("  Example: ugendran do myapp \"I want to add user login with Google\""))
        return

    project_name = args[0]
    request      = " ".join(args[1:])

    # ── Load or auto-create project ──────────────────────────────────────────
    project = load_project(project_name)
    if not project:
        ptype   = detect_project_type(request)
        skills  = PROJECT_PROFILES.get(ptype, PROJECT_PROFILES["web"])
        project = {
            "name":   project_name,
            "idea":   request,
            "type":   ptype,
            "status": "active",
            "created": ts(),
            "skills": {s: {"status":"pending","started":None,"done":None} for s in skills},
            "log":    [{"ts":ts(),"event":"project_created","detail":request}],
        }
        save_project(project_name, project)
        ws = ROOT / ".ugendran" / "workspaces" / project_name
        ws.mkdir(parents=True, exist_ok=True)

    print()
    print(bold(f"🤖 AI Reading Your Request..."))
    print(dim(f"   \"{request}\""))
    print()

    # ── AI Skill Matching ────────────────────────────────────────────────────
    matches = top_skill_matches(request, n=3)

    if not matches:
        print(warn("Could not match any skill to your request."))
        print(dim("  Try: ugendran skills   to browse all 78 skills manually"))
        return

    best_skill, best_conf = matches[0]
    cat = skill_category(best_skill)

    print(bold("🎯 AI Skill Match:"))
    print()
    for i, (sk, conf) in enumerate(matches):
        conf_bar   = "█" * int(conf * 10) + "░" * (10 - int(conf * 10))
        conf_color = "green" if conf >= 0.6 else "yellow" if conf >= 0.3 else "dim"
        marker     = c(" ← BEST MATCH", "green") if i == 0 else ""
        print(f"  {c(str(i+1), 'bold')}. {c(sk, 'cyan'):<42} {c(conf_bar, conf_color)} {int(conf*100)}%{marker}")
    print()

    # ── Confidence Check ─────────────────────────────────────────────────────
    if best_conf < 0.2:
        print(warn(f"Low confidence ({int(best_conf*100)}%). Using best guess: {c(best_skill, 'cyan')}"))
        print(dim("  Tip: Be more specific in your request for better matching."))
        print()

    print(ai_tag(f"Selected: {bold(best_skill)} [{cat}]  (confidence: {int(best_conf*100)}%)"))
    print()

    # ── Read skill purpose from SKILL.md ─────────────────────────────────────
    sp = skill_path(best_skill)
    if sp:
        sm = sp / "SKILL.md"
        if sm.exists():
            content = sm.read_text()
            # Extract purpose paragraph
            idx = content.find("## Purpose")
            if idx != -1:
                chunk = content[idx+10:idx+400].strip()
                lines = [l.strip() for l in chunk.split("\n") if l.strip() and not l.startswith("#")]
                if lines:
                    purpose_text = lines[0][:120]
                    print(dim(f"   Skill purpose: {purpose_text}"))
                    print()

    # ── Apply Skill ───────────────────────────────────────────────────────────
    print(bold("⚡ Applying Skill..."))
    dest = apply_skill(project_name, best_skill, request)

    # List what was created
    created_files = sorted(dest.rglob("*"))
    file_list = [f for f in created_files if f.is_file()]
    print()
    print(bold(f"📁 Skill workspace created ({len(file_list)} files):"))
    for f in file_list[:8]:
        rel = f.relative_to(dest)
        print(f"   {c('›', 'dim')} .ugendran/workspaces/{project_name}/skills/{best_skill}/{rel}")
    if len(file_list) > 8:
        print(dim(f"   ... and {len(file_list)-8} more"))
    print()

    # ── Update Project State: pending → done (auto) ───────────────────────────
    if best_skill not in project["skills"]:
        project["skills"][best_skill] = {"status":"pending","started":None,"done":None}

    project["skills"][best_skill]["status"]  = "done"
    project["skills"][best_skill]["started"] = ts()
    project["skills"][best_skill]["done"]    = ts()
    project["log"].append({"ts":ts(),"event":"skill_auto_done","detail":best_skill})

    # ── Archive Entry ─────────────────────────────────────────────────────────
    archive_entry = {
        "project":  project_name,
        "skill":    best_skill,
        "request":  request,
        "confidence": best_conf,
        "applied":  ts(),
        "files":    [str(f.relative_to(dest)) for f in file_list],
    }
    afile = ARCHIVE_DIR / f"{project_name}_{best_skill}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    afile.write_text(json.dumps(archive_entry, indent=2))

    save_project(project_name, project)

    print(ok(f"Skill '{best_skill}' applied & archived!"))
    print(dim(f"   Archive record: {afile.name}"))
    print()

    # ── Progress Bar ─────────────────────────────────────────────────────────
    skills   = project["skills"]
    done_cnt = sum(1 for v in skills.values() if v["status"] == "done")
    total    = len(skills)
    pct      = int(done_cnt / total * 100) if total else 0
    bar      = "█" * (pct // 5) + "░" * (20 - pct // 5)
    print(bold("📊 Project Progress:"))
    print(f"   {c(bar, 'cyan')} {c(str(pct)+'%', 'bold')} ({done_cnt}/{total} skills done)")
    print()

    # ── Suggest Next ──────────────────────────────────────────────────────────
    pending = [s for s, v in skills.items() if v["status"] == "pending"]
    critical = ["security-architecture","testing-strategy","ci-cd-pipeline",
                "authentication-design","threat-modeling","observability-design"]
    if pending:
        next_skill = next((s for s in pending if s in critical), pending[0])
        print(bold("⚡ Next Suggested:"))
        print(f"   {c(next_skill, 'cyan')} [{skill_category(next_skill)}]")
        print()
        next_cmd = f'ugendran do {project_name} "<describe what you want next>"'
        print(bold("💡 How to continue:"))
        print(f"   {c(next_cmd, 'yellow')}")
        print(f"   {c('ugendran suggest '+project_name, 'yellow')}   — see full suggestion")
        print(f"   {c('ugendran status '+project_name, 'yellow')}    — see full dashboard")
    else:
        print(ok(f"All skills complete for '{project_name}'!"))
        print(f"   {c('ugendran kill '+project_name, 'yellow')}  — archive the full project")
    print()

# ─── CMD: new ────────────────────────────────────────────────────────────────
def cmd_new(args):
    if len(args) < 2:
        print(err("Usage: ugendran new <project-name> <idea>"))
        return
    name, idea = args[0], " ".join(args[1:])
    if load_project(name):
        print(warn(f"Project '{name}' already exists. Use: ugendran status {name}"))
        return
    ptype  = detect_project_type(idea)
    skills = PROJECT_PROFILES.get(ptype, PROJECT_PROFILES["web"])
    project = {
        "name": name, "idea": idea, "type": ptype, "status": "active",
        "created": ts(),
        "skills": {s:{"status":"pending","started":None,"done":None} for s in skills},
        "log": [{"ts":ts(),"event":"project_created","detail":idea}],
    }
    save_project(name, project)
    ws = ROOT / ".ugendran" / "workspaces" / name
    ws.mkdir(parents=True, exist_ok=True)
    (ws / "README.md").write_text(f"# {name}\n\n**Idea:** {idea}\n\n**Type:** {ptype}\n\n**Created:** {ts()}\n")
    print()
    print(bold(f"🚀 New Project: {name}"))
    print(dim(f"   Idea : {idea}"))
    print(dim(f"   Type : {ptype}"))
    print()
    print(bold(f"📋 {len(skills)} Skills Activated:"))
    for i, s in enumerate(skills, 1):
        print(f"  {dim(str(i).zfill(2))}  {c(s,'cyan'):<42} {dim('['+skill_category(s)+']')}")
    print()
    print(ok(f"Ready! Now use:"))
    _ex = 'ugendran do ' + name + ' "what you want to build"'
    print(f"   {c(_ex, 'yellow')}")
    print()

# ─── CMD: audit ──────────────────────────────────────────────────────────────
def cmd_audit(args):
    if not args:
        print(err("Usage: ugendran audit <project-path> [project-name]"))
        return
    path  = Path(args[0])
    pname = args[1] if len(args) > 1 else path.name
    if not path.exists():
        print(err(f"Path not found: {path}"))
        return
    print()
    print(bold(f"🔍 Auditing: {path}"))
    print()
    all_files  = list(path.rglob("*")) if path.is_dir() else [path]
    file_count = sum(1 for f in all_files if f.is_file())
    checks = [
        (any(f.name.lower()=="readme.md"    for f in all_files), "documentation-generator", "No README",           "🟢"),
        (any("test" in str(f).lower()       for f in all_files), "testing-strategy",         "No tests found",      "🔴"),
        (any(".github" in str(f) or "Jenkinsfile" in f.name for f in all_files), "ci-cd-pipeline", "No CI/CD",     "🔴"),
        (any(f.name in ["Dockerfile","docker-compose.yml"] for f in all_files),  "docker-architecture", "No Docker","🟡"),
        (any("security" in str(f).lower()   for f in all_files), "security-testing",         "No security config",  "🔴"),
        (any(f.suffix==".tf"                for f in all_files), "infrastructure-as-code",   "No IaC",              "🟡"),
        (any("openapi" in f.name.lower()    for f in all_files), "api-contract-design",      "No OpenAPI spec",     "🟡"),
        (any("prometheus" in f.name.lower() or "datadog" in f.name.lower() for f in all_files),"observability-design","No monitoring","🔴"),
        (any("migration" in str(f).lower()  for f in all_files), "database-design",          "No DB migrations",    "🟡"),
        (any("k8s" in str(f) or f.suffix==".yaml" for f in all_files), "kubernetes-planning","No K8s config",       "🟡"),
    ]
    missing = []
    print(bold(f"📁 Files scanned: {file_count}"))
    print()
    print(bold("🎯 Skill Gap Analysis:"))
    print()
    for present, skill, msg, sev in checks:
        st = ok("Present") if present else warn(msg)
        print(f"  {sev}  {c(skill,'cyan'):<42} {st}")
        if not present:
            missing.append((sev, skill))
    score = int(sum(1 for p,*_ in checks if p) / len(checks) * 100)
    print()
    rec = "CONTINUE" if score>=70 else "FINETUNE" if score>=40 else "DISCONTINUE"
    rec_c = "green" if score>=70 else "yellow" if score>=40 else "red"
    print(bold(f"📊 Health Score: {c(str(score)+'%', rec_c)}   →  {c(rec, rec_c)}"))
    print()
    if missing:
        print(bold("🛠️  Quick fixes (auto-apply):"))
        for sev, sk in missing[:3]:
            _fix_cmd = 'ugendran do ' + pname + ' "fix ' + sk.replace('-', ' ') + '"'
        print(f"   {sev}  {c(_fix_cmd, 'yellow')}")
    audit_data = {"project":pname,"path":str(args[0]),"ts":ts(),"score":score,
                  "recommendation":rec.lower(),"missing":[s for _,s in missing]}
    af = ARCHIVE_DIR / f"{pname}_audit_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
    af.write_text(json.dumps(audit_data, indent=2))
    print()
    print(dim(f"   Saved → {af.name}"))
    print()

# ─── CMD: archive (manual) ───────────────────────────────────────────────────
def cmd_archive(args):
    if len(args) < 2:
        print(err("Usage: ugendran archive <project> <skill>"))
        return
    name, skill = args[0], args[1]
    project = load_project(name)
    if not project:
        print(err(f"Project '{name}' not found."))
        return
    if skill not in project["skills"]:
        project["skills"][skill] = {"status":"pending","started":None,"done":None}
    prev = project["skills"][skill]["status"]
    if prev == "pending":
        project["skills"][skill].update({"status":"in-progress","started":ts()})
        event = "skill_started"
        dest  = apply_skill(name, skill, f"Manual: {skill}")
        print()
        print(info(f"Skill '{skill}' → IN-PROGRESS"))
        print(dim(f"   Files → .ugendran/workspaces/{name}/skills/{skill}/"))
        print(dim(f"   Run again to mark DONE: ugendran archive {name} {skill}"))
    else:
        project["skills"][skill].update({"status":"done","done":ts()})
        event = "skill_done"
        ae = {"project":name,"skill":skill,"done":ts()}
        af = ARCHIVE_DIR / f"{name}_{skill}_{datetime.now().strftime('%Y%m%d')}.json"
        af.write_text(json.dumps(ae, indent=2))
        print()
        print(ok(f"Skill '{skill}' DONE & archived!"))
    project["log"].append({"ts":ts(),"event":event,"detail":skill})
    save_project(name, project)
    print()

# ─── CMD: status ─────────────────────────────────────────────────────────────
def cmd_status(args):
    if not args:
        projects = list(PROJECTS.glob("*.json"))
        if not projects:
            print(warn("No projects. Run: ugendran new <name> <idea>"))
            return
        print()
        print(bold("📂 All Projects:"))
        print()
        for pf in projects:
            p    = json.loads(pf.read_text())
            done = sum(1 for v in p["skills"].values() if v["status"]=="done")
            tot  = len(p["skills"])
            pct  = int(done/tot*100) if tot else 0
            bar  = "█"*(pct//5) + "░"*(20-pct//5)
            sc   = "green" if p["status"]=="active" else "red"
            print(f"  {bold(p['name']):<28} {c('['+p['status']+']',sc)} {dim(p['type'])}")
            print(f"  {c(bar,'cyan')} {pct}%  ({done}/{tot} skills)")
            print(f"  {dim(p['idea'][:60])}")
            print()
        return
    name    = args[0]
    project = load_project(name)
    if not project:
        print(err(f"Project '{name}' not found."))
        return
    skills  = project["skills"]
    done    = sum(1 for v in skills.values() if v["status"]=="done")
    inprog  = sum(1 for v in skills.values() if v["status"]=="in-progress")
    pending = len(skills) - done - inprog
    pct     = int(done/len(skills)*100) if skills else 0
    bar     = "█"*(pct//5)+"░"*(20-pct//5)
    print()
    print(bold(f"📊 {project['name']}  [{project['type']}]"))
    print(f"   {dim(project['idea'])}")
    print()
    print(f"   {c(bar,'cyan')} {c(str(pct)+'%','bold')}  ✅{done}  ⏳{inprog}  ⏸{pending}")
    print()
    print(bold("📋 Skills:"))
    icons = {"done":c("✅","green"),"in-progress":c("⏳","yellow"),"pending":c("⏸ ","dim")}
    for skill, v in skills.items():
        icon = icons.get(v["status"],"?")
        dt   = dim(f" → {v['done']}") if v.get("done") else ""
        print(f"  {icon}  {c(skill,'cyan'):<42} {dim('['+skill_category(skill)+']')}{dt}")
    print()
    pending_list = [s for s,v in skills.items() if v["status"]=="pending"]
    if pending_list:
        _next_cmd = 'ugendran do ' + name + ' "describe what you need"'
        print(bold("⚡ Next:") + f" {c(_next_cmd, 'yellow')}")
    else:
        print(ok(f"Done! Run: ugendran kill {name}"))
    print()

# ─── CMD: history ────────────────────────────────────────────────────────────
def cmd_history(args):
    if not args:
        print(err("Usage: ugendran history <project>"))
        return
    project = load_project(args[0])
    if not project:
        print(err(f"Project '{args[0]}' not found."))
        return
    print()
    print(bold(f"📜 History: {args[0]}"))
    print()
    icons = {"project_created":"🚀","skill_started":"▶️ ","skill_done":"✅",
             "skill_auto_done":"🤖","project_killed":"💀"}
    for e in project["log"]:
        print(f"  {icons.get(e['event'],'•')}  {dim(e['ts'])}  {c(e['event'],'cyan'):<22}  {e['detail']}")
    print()

# ─── CMD: suggest ────────────────────────────────────────────────────────────
def cmd_suggest(args):
    if not args:
        print(err("Usage: ugendran suggest <project>"))
        return
    project = load_project(args[0])
    if not project:
        print(err(f"Project '{args[0]}' not found."))
        return
    pending = [s for s,v in project["skills"].items() if v["status"]=="pending"]
    inprog  = [s for s,v in project["skills"].items() if v["status"]=="in-progress"]
    print()
    print(bold(f"🤖 Suggestion for: {args[0]}"))
    print()
    if inprog:
        print(f"  {c('⏳ Finish first:', 'yellow')} {c(inprog[0], 'cyan')}")
        print(f"  Run: {c('ugendran archive '+args[0]+' '+inprog[0], 'yellow')}")
    elif pending:
        critical = ["security-architecture","testing-strategy","ci-cd-pipeline",
                    "authentication-design","threat-modeling","observability-design"]
        nxt = next((s for s in pending if s in critical), pending[0])
        print(f"  {c('⚡ Next:', 'green')} {c(nxt, 'cyan')} [{skill_category(nxt)}]")
        print()
        _sugg_cmd = 'ugendran do ' + args[0] + ' "describe what you need for ' + nxt + '"'
        print(f"  {c(_sugg_cmd, 'yellow')}")
    else:
        print(ok(f"All skills done! Run: ugendran kill {args[0]}"))
    print()

# ─── CMD: skills ─────────────────────────────────────────────────────────────
def cmd_skills(args):
    fcat = args[0].lower() if args else None
    icons = {"product":"🧠","architecture":"🏛️","frontend":"🖥️","backend":"⚙️",
             "ai":"🤖","testing":"🧪","devops":"🚀","security":"🔐","maintenance":"🔧"}
    print()
    print(bold("📚 OpenSpec — 78 Skills"))
    print()
    for cat, skills in SKILL_MAP.items():
        if fcat and fcat not in cat: continue
        print(f"{icons.get(cat,'•')}  {bold(cat.upper())} ({len(skills)})")
        for s in skills:
            print(f"   {dim('›')} {c(s,'cyan')}")
        print()

# ─── CMD: kill ───────────────────────────────────────────────────────────────
def cmd_kill(args):
    if not args:
        print(err("Usage: ugendran kill <project>"))
        return
    name    = args[0]
    project = load_project(name)
    if not project:
        print(err(f"Project '{name}' not found."))
        return
    project.update({"status":"archived","archived_at":ts()})
    project["log"].append({"ts":ts(),"event":"project_killed","detail":"Discontinued"})
    save_project(name, project)
    ws     = ROOT / ".ugendran" / "workspaces" / name
    arc_ws = ARCHIVE_DIR / f"project_{name}_{datetime.now().strftime('%Y%m%d_%H%M')}"
    if ws.exists(): shutil.move(str(ws), str(arc_ws))
    done = sum(1 for v in project["skills"].values() if v["status"]=="done")
    print()
    print(bold(f"💀 Project '{name}' ARCHIVED"))
    print(dim(f"   Skills completed: {done}/{len(project['skills'])}"))
    print(dim(f"   Archive: {arc_ws}"))
    print()

# ─── Main ────────────────────────────────────────────────────────────────────
COMMANDS = {
    "do":      cmd_do,
    "new":     cmd_new,
    "audit":   cmd_audit,
    "archive": cmd_archive,
    "status":  cmd_status,
    "history": cmd_history,
    "suggest": cmd_suggest,
    "skills":  cmd_skills,
    "kill":    cmd_kill,
}

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print()
        print(bold("  🚀 ugendran — Smart OpenSpec Skills CLI"))
        print()
        print(f"  {c('★ MAIN COMMAND:', 'green')}")
        _help_ex = '<project> "what you want"'
        print(f"    {c('ugendran do', 'cyan')} {c(_help_ex, 'yellow'):<38} {dim('AI picks skill → apply → archive')}")
        print()
        print(f"  {dim('Other commands:')}")
        for cmd, desc in [
            ("new    <name> <idea>",    "Create project"),
            ("audit  <path> [name]",    "Audit existing project"),
            ("status [name]",           "Dashboard"),
            ("history <name>",          "Timeline"),
            ("suggest <name>",          "Next skill"),
            ("skills  [cat]",           "List all 78 skills"),
            ("kill    <name>",          "Archive project"),
        ]:
            print(f"    {c('ugendran', 'cyan')} {c(cmd, 'yellow'):<35} {dim(desc)}")
        print()
        print(f"  {bold('Examples:')}")
        _e1 = 'ugendran do myapp "add google login"'
        _e2 = 'ugendran do myapp "I need to cache API responses"'
        _e3 = 'ugendran do myapp "set up CI/CD pipeline"'
        print(f"    {c(_e1, 'yellow')}")
        print(f"    {c(_e2, 'yellow')}")
        print(f"    {c(_e3, 'yellow')}")
        print(f"    {c('ugendran audit ./old-project', 'yellow')}")
        print()
        return

    COMMANDS[sys.argv[1]](sys.argv[2:])

if __name__ == "__main__":
    main()
