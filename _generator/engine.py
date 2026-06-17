"""
OpenSpec Enterprise Skill Catalog — generation engine.

Given a registry of skill definitions (see skills_data.py), this module renders
a fully OpenSpec-compliant skill package for each entry:

  <category>/<skill>/
    SKILL.md            -- frontmatter + structured instructions
    checklist.md        -- quality gates grouped by phase
    examples.md         -- worked, realistic examples
    templates/*.md      -- domain artifacts ready to fill in
    prompts/prompts.md  -- copy-paste prompts to drive the skill

The rendering is deliberately uniform so the catalog reads as one product,
while every skill carries its own domain-specific focus, deliverables,
anti-patterns, templates and examples.
"""

from __future__ import annotations

import os
import textwrap
from datetime import date
from typing import Dict, List

VERSION = "1.0.0"
TODAY = date.today().isoformat()

# ---------------------------------------------------------------------------
# OpenSpec phase model.
#
# Every skill is expressed as a spec-driven workflow. The five phases below are
# the OpenSpec lifecycle: each phase has a clear intent, an artifact, and an
# exit gate. Individual skills override the phase *descriptions* to make them
# concrete, but the phase names stay constant so all skills compose.
# ---------------------------------------------------------------------------

PHASES = [
    ("Discover", "Establish context, constraints, and success criteria before proposing anything.",
     "Problem, stakeholders, constraints, and success criteria are written down and agreed."),
    ("Specify", "Capture the intended outcome as a reviewable spec / proposal — the source of truth.",
     "A reviewable spec exists with scope, non-goals, assumptions, and objective acceptance criteria."),
    ("Design", "Decide the approach, record trade-offs, and document decisions (ADRs).",
     "Approach chosen from ≥2 options; trade-offs and the decision are recorded as an ADR."),
    ("Validate", "Prove the spec is correct, complete, and testable against the quality gates.",
     "All applicable checklist gates pass or are waived; a domain expert has reviewed it."),
    ("Deliver", "Produce the final artifact, hand it off, and define how it will be maintained.",
     "Artifact is in the spec registry with an owner, review cadence, and handoff done."),
]


def decap(text: str) -> str:
    """Lowercase the first letter, but leave acronyms (e.g. TTL, API) intact."""
    if len(text) >= 2 and text[0].isupper() and text[1].isupper():
        return text
    return text[0].lower() + text[1:] if text else text


def slugify(text: str) -> str:
    return text.lower().replace(" ", "-").replace("/", "-").replace("&", "and")


def fm_list(items: List[str]) -> str:
    return "\n".join(f"  - {i}" for i in items)


def bullets(items: List[str]) -> str:
    return "\n".join(f"- {i}" for i in items)


def numbered(items: List[str]) -> str:
    return "\n".join(f"{n}. {i}" for n, i in enumerate(items, 1))


def checkitems(items: List[str]) -> str:
    return "\n".join(f"- [ ] {i}" for i in items)


# ---------------------------------------------------------------------------
# Renderers
# ---------------------------------------------------------------------------

def render_skill_md(s: Dict) -> str:
    title = s["title"]
    cat = s["category_title"]
    focus = s["focus"]
    deliverables = s["deliverables"]
    inputs = s.get("inputs", DEFAULT_INPUTS)
    antipatterns = s["antipatterns"]
    when = s.get("when", default_when(s))
    phases = s.get("phases", default_phases(s))
    roles = s.get("roles", DEFAULT_ROLES)
    metrics = s.get("metrics", [])
    refs = s.get("refs", [])

    tags = [s["category_slug"]] + s.get("tags", [])

    fm = f"""---
name: {s['slug']}
title: {title}
description: >-
  {s['desc']}
category: {cat}
version: {VERSION}
updated: {TODAY}
license: Apache-2.0
openspec:
  spec_version: "1.0"
  lifecycle: [discover, specify, design, validate, deliver]
  artifact_type: skill
tags:
{fm_list(tags)}
---"""

    phase_md = "\n".join(
        f"### {i}. {name}\n\n{desc}\n\n**Exit gate:** {gate}\n"
        for i, (name, desc, gate) in enumerate(phases, 1)
    )

    metrics_md = ""
    if metrics:
        metrics_md = f"\n## Success Metrics\n\nTrack these to know the skill delivered value:\n\n{bullets(metrics)}\n"

    refs_md = ""
    if refs:
        refs_md = f"\n## References\n\n{bullets(refs)}\n"

    template_links = bullets([f"`templates/{t[0]}.md` — {t[1]}" for t in s["templates"]])

    return f"""{fm}

# {title}

> **Category:** {cat} · **Skill:** `{s['slug']}` · **OpenSpec lifecycle skill**

## Purpose

{s['purpose']}

This skill is spec-driven: it produces a reviewable artifact *before* work
begins, records the decisions and trade-offs behind it, and defines the quality
gates that say when it is done. The artifact — not tribal knowledge — is the
source of truth.

## When to Use

{bullets(when)}

## When *Not* to Use

{bullets(s.get('when_not', DEFAULT_WHEN_NOT))}

## Capabilities & Focus Areas

{bullets(focus)}

## Inputs

{bullets(inputs)}

## OpenSpec Workflow

Run the skill as five phases. Do not skip a phase; if a phase has no work,
record *why* and move on.

{phase_md}

## Deliverables

{bullets(deliverables)}

## Roles & RACI

{bullets(roles)}
{metrics_md}
## Quality Gates

The full, checkable gate list lives in [`checklist.md`](./checklist.md). Treat
it as the definition of done — a deliverable is not complete until every
applicable item is checked or explicitly waived with a recorded reason.

## Templates

{template_links}

## Prompts

Copy-paste prompts that drive each phase live in
[`prompts/prompts.md`](./prompts/prompts.md).

## Worked Examples

See [`examples.md`](./examples.md) for realistic, end-to-end walkthroughs.

## Anti-Patterns to Avoid

{bullets(antipatterns)}
{refs_md}
---
*Part of the Enterprise OpenSpec Skill Catalog. Generated artifact — edit the
skill definition and regenerate to change.*
"""


def render_checklist_md(s: Dict) -> str:
    groups = s.get("checklist", default_checklist(s))
    body = []
    for group_name, items in groups:
        body.append(f"## {group_name}\n\n{checkitems(items)}\n")
    body_joined = "\n".join(body)
    return f"""# {s['title']} — Quality Gate Checklist

> Definition of done for the `{s['slug']}` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `{s['slug']}` · **Category:** {s['category_title']} · **Version:** {VERSION}

{body_joined}
## Sign-off

- [ ] All gates above checked or waived (with reason recorded)
- [ ] Artifact peer-reviewed by at least one other person
- [ ] Decisions/trade-offs captured (ADR or decision log)
- [ ] Owner and review cadence assigned
- [ ] Linked from the project's spec index / `openspec/` registry

| Role | Name | Date |
|------|------|------|
| Author | | |
| Reviewer | | |
| Approver | | |
"""


def render_examples_md(s: Dict) -> str:
    examples = s.get("examples", default_examples(s))
    blocks = []
    for i, ex in enumerate(examples, 1):
        blocks.append(
            f"## Example {i}: {ex['title']}\n\n"
            f"**Context.** {ex['context']}\n\n"
            f"**Applying the skill.**\n\n{numbered(ex['steps'])}\n\n"
            f"**Outcome.** {ex['outcome']}\n"
        )
    blocks_joined = "\n---\n\n".join(blocks)
    return f"""# {s['title']} — Worked Examples

Realistic, end-to-end walkthroughs of the `{s['slug']}` skill. Each example
follows the OpenSpec phases (Discover → Specify → Design → Validate → Deliver).

{blocks_joined}
---

## How to reuse these

1. Pick the example closest to your situation.
2. Copy the matching template from [`templates/`](./templates/).
3. Drive each phase with the prompts in [`prompts/prompts.md`](./prompts/prompts.md).
4. Verify against [`checklist.md`](./checklist.md) before sign-off.
"""


def render_prompts_md(s: Dict) -> str:
    prompts = s.get("prompts", default_prompts(s))
    blocks = []
    for p in prompts:
        blocks.append(f"### {p['name']}\n\n```\n{p['text'].strip()}\n```\n")
    prompts_joined = "\n".join(blocks)
    return f"""# {s['title']} — Prompts

Copy-paste prompts to drive the `{s['slug']}` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

{prompts_joined}
## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
"""


def render_template(s: Dict, slug: str, title: str) -> str:
    sections = s.get("template_sections", {}).get(slug, DEFAULT_TEMPLATE_SECTIONS)
    body = []
    for sec in sections:
        body.append(f"## {sec}\n\n_TODO: fill in._\n")
    body_joined = "\n".join(body)
    return f"""# {title}

> Template for the `{s['slug']}` skill. Copy this file, rename it, and fill in
> each section. Delete sections that do not apply (and note why).

**Project:** _____  ·  **Author:** _____  ·  **Date:** _____  ·  **Status:** Draft

{body_joined}
---
*Generated from the `{s['slug']}` OpenSpec skill template.*
"""


# ---------------------------------------------------------------------------
# Defaults (used when a skill does not override)
# ---------------------------------------------------------------------------

DEFAULT_INPUTS = [
    "Project context, goals, and constraints",
    "Relevant existing artifacts (specs, code, docs, diagrams)",
    "Stakeholders and their success criteria",
    "Non-functional requirements and compliance obligations",
]

DEFAULT_ROLES = [
    "**Driver** — owns the artifact and runs the workflow",
    "**Reviewers** — domain experts who approve the spec",
    "**Stakeholders** — consume the outcome and accept the result",
]

DEFAULT_WHEN_NOT = [
    "The decision is trivial, reversible, and low-impact — just do it",
    "An existing, current spec already covers the need — reuse it instead",
    "You lack the inputs to do it well — gather them first (don't guess)",
]

DEFAULT_TEMPLATE_SECTIONS = [
    "Summary", "Context & Goals", "Scope", "Details", "Decisions & Trade-offs",
    "Risks & Mitigations", "Validation", "Open Questions",
]


def default_when(s: Dict) -> List[str]:
    return [
        f"Starting work that requires {s['title'].lower()} as a deliberate, documented step",
        "A decision here is hard to reverse, cross-team, or high-impact",
        "You need a reviewable artifact others can build on or audit",
        "Onboarding, handoff, or compliance requires the reasoning to be explicit",
    ]


def default_phases(s: Dict):
    return list(PHASES)


def default_checklist(s: Dict):
    # Domain-specific gates: every focus area must be addressed, and every known
    # anti-pattern must be confirmed avoided. This makes each checklist unique.
    focus_gates = [f"Addressed: {decap(f)}" for f in s["focus"]]
    antipattern_gates = [f"Confirmed avoided: {decap(a)}" for a in s["antipatterns"]]
    deliverable_gates = [f"Produced: {d}" for d in s["deliverables"]]
    return [
        ("Discover", [
            "Problem statement and success criteria are written down",
            "Stakeholders and their concerns are identified",
            "Constraints (time, budget, tech, compliance) are explicit",
            "Existing artifacts reviewed for reuse",
        ]),
        ("Specify", [
            "Intended outcome captured as a reviewable spec",
            "Scope and non-goals stated",
            "Assumptions and open questions listed",
        ]),
        ("Design — domain coverage", focus_gates),
        ("Validate — anti-patterns avoided", antipattern_gates + [
            "Spec is testable — acceptance criteria are objective",
            "Reviewed by domain expert(s)",
            "Risks identified with mitigations",
        ]),
        ("Deliver — artifacts", deliverable_gates + [
            "Final artifact stored in the spec registry",
            "Owner and review cadence assigned",
            "Handoff / communication done",
        ]),
    ]


def default_examples(s: Dict):
    return [
        {
            "title": f"Applying {s['title']} on a greenfield feature",
            "context": f"A team is starting new work and needs {s['title'].lower()} done properly the first time.",
            "steps": [
                "Discover: gather context, constraints, and success criteria from stakeholders.",
                "Specify: write the outcome as a reviewable spec using the template.",
                "Design: weigh two approaches and record the choice as an ADR.",
                "Validate: check against the quality gates and get a peer review.",
                "Deliver: store the artifact, assign an owner, and communicate.",
            ],
            "outcome": "A reviewed, owned artifact that the team builds on with confidence.",
        },
        {
            "title": f"Applying {s['title']} to an existing system",
            "context": f"An established system needs {s['title'].lower()} retrofitted to reduce risk.",
            "steps": [
                "Discover: inventory the current state and pain points.",
                "Specify: capture the target state and the gap.",
                "Design: plan an incremental path that avoids a big-bang change.",
                "Validate: confirm each step is independently shippable and safe.",
                "Deliver: sequence the work and define rollback.",
            ],
            "outcome": "A low-risk, incremental plan with clear checkpoints.",
        },
    ]


def default_prompts(s: Dict):
    t = s["title"]
    focus_list = "\n".join(f"- {f}" for f in s["focus"])
    anti_list = "\n".join(f"- {a}" for a in s["antipatterns"])
    return [
        {"name": "Discover",
         "text": f"You are an expert in {t.lower()}. Given this context:\n<context>\n...\n</context>\nIdentify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:\n{focus_list}\nList what you still need to know before proceeding."},
        {"name": "Specify",
         "text": f"Using the discovered context, draft a reviewable {t} spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria."},
        {"name": "Design & decide",
         "text": f"Propose 2-3 viable approaches for <decision> in the context of {t.lower()}. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded."},
        {"name": "Validate (anti-pattern check)",
         "text": f"Review the {t} artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:\n{anti_list}\nList the top risks and a mitigation for each."},
        {"name": "Deliver",
         "text": f"Finalize the {t} artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders."},
    ]


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def write(path: str, content: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)


def generate(root: str, skills: List[Dict]):
    count_files = 0
    for s in skills:
        base = os.path.join(root, s["category_slug"], s["slug"])
        write(os.path.join(base, "SKILL.md"), render_skill_md(s)); count_files += 1
        write(os.path.join(base, "checklist.md"), render_checklist_md(s)); count_files += 1
        write(os.path.join(base, "examples.md"), render_examples_md(s)); count_files += 1
        write(os.path.join(base, "prompts", "prompts.md"), render_prompts_md(s)); count_files += 1
        for slug, title in s["templates"]:
            write(os.path.join(base, "templates", f"{slug}.md"),
                  render_template(s, slug, title)); count_files += 1
    return count_files
