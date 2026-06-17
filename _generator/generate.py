#!/usr/bin/env python3
"""Generate the full Enterprise OpenSpec Skill Catalog."""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import engine
from skills_data import ALL_SKILLS, CATEGORIES, R


def render_root_readme(skills):
    by_cat = {}
    for s in skills:
        by_cat.setdefault(s["category_slug"], []).append(s)

    lines = [
        "# Enterprise OpenSpec Skill Catalog",
        "",
        f"**{len(skills)} production-ready, spec-driven skills** spanning the full software "
        "delivery lifecycle — from idea to maintenance. Each skill is an OpenSpec "
        "artifact: a reviewable, versioned, gated way of doing one thing well.",
        "",
        "## What is an OpenSpec skill?",
        "",
        "Each skill follows the same spec-driven lifecycle so they compose into one method:",
        "",
        "| Phase | Intent |",
        "|-------|--------|",
    ]
    for name, desc, _gate in engine.PHASES:
        lines.append(f"| **{name}** | {desc} |")
    lines += [
        "",
        "Every skill folder contains:",
        "",
        "```",
        "<category>/<skill>/",
        "  SKILL.md            # frontmatter + purpose, workflow, deliverables, anti-patterns",
        "  checklist.md        # quality gates = definition of done",
        "  examples.md         # worked, end-to-end examples",
        "  templates/          # ready-to-fill domain artifacts",
        "  prompts/prompts.md  # copy-paste prompts to drive each phase",
        "```",
        "",
        "## How to use a skill",
        "",
        "1. Open the skill's `SKILL.md` and read **Purpose** and **When to Use**.",
        "2. Work the five phases in order; do not skip one (record *why* if it has no work).",
        "3. Copy the relevant file from `templates/` and fill it in.",
        "4. Drive each phase with `prompts/prompts.md`.",
        "5. Verify against `checklist.md` before sign-off — it is the definition of done.",
        "",
        "## Catalog",
        "",
    ]

    # Preserve catalog order from R
    for cat_slug in R.keys():
        cat_title = CATEGORIES[cat_slug]
        items = by_cat.get(cat_slug, [])
        lines.append(f"### {cat_title} ({len(items)})")
        lines.append("")
        lines.append("| Skill | What it does |")
        lines.append("|-------|--------------|")
        for s in items:
            link = f"[`{s['slug']}`]({cat_slug}/{s['slug']}/SKILL.md)"
            lines.append(f"| {link} | {s['desc']} |")
        lines.append("")

    lines += [
        "## Lifecycle map",
        "",
        "These skills are designed to be run in sequence across a project's life:",
        "",
        "```",
        "Idea → market-research → business-analysis → prd-generation →",
        "requirements-analysis → proposal-creation → user-story-generation →",
        "design-document → frontend/backend-architecture → api-design →",
        "database-design → security-architecture → testing-strategy →",
        "docker-architecture → ci-cd-pipeline → observability-design →",
        "incident-response → bug-investigation → refactoring-planning →",
        "scalability-planning → technical-debt-management",
        "```",
        "",
        "## Regenerating",
        "",
        "This catalog is generated. To change a skill, edit its definition in",
        "`_generator/skills_data.py` and run:",
        "",
        "```bash",
        "python3 _generator/generate.py",
        "```",
        "",
        "---",
        f"*{len(skills)} skills · OpenSpec spec v1.0 · Apache-2.0*",
    ]
    return "\n".join(lines) + "\n"


def main():
    n_files = engine.generate(ROOT, ALL_SKILLS)
    readme = render_root_readme(ALL_SKILLS)
    with open(os.path.join(ROOT, "README.md"), "w") as f:
        f.write(readme)
    n_files += 1
    print(f"Generated {len(ALL_SKILLS)} skills, {n_files} files into {ROOT}")


if __name__ == "__main__":
    main()
