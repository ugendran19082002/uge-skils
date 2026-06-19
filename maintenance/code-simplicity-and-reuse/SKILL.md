---
name: code-simplicity-and-reuse
title: Code Simplicity & Reuse
description: >-
  Choose the simplest solution and reuse before writing new code (KISS, DRY, YAGNI).
category: Maintenance & Operations
version: 1.0.0
updated: 2026-06-19
license: Apache-2.0
openspec:
  spec_version: "1.0"
  lifecycle: [discover, specify, design, validate, deliver]
  artifact_type: skill
tags:
  - maintenance
---

# Code Simplicity & Reuse

> **Category:** Maintenance & Operations · **Skill:** `code-simplicity-and-reuse` · **OpenSpec lifecycle skill**

## Purpose

Keep the codebase small, simple, and DRY. Before writing code, check whether it already exists or isn't needed yet, and always prefer the simplest design that satisfies the requirement — because the cheapest, most reliable, and most maintainable code is the code you never wrote. This skill is language- and framework-agnostic: it governs decisions, not syntax.

This skill is spec-driven: it produces a reviewable artifact *before* work
begins, records the decisions and trade-offs behind it, and defines the quality
gates that say when it is done. The artifact — not tribal knowledge — is the
source of truth.

## When to Use

- Starting work that requires code simplicity & reuse as a deliberate, documented step
- A decision here is hard to reverse, cross-team, or high-impact
- You need a reviewable artifact others can build on or audit
- Onboarding, handoff, or compliance requires the reasoning to be explicit

## When *Not* to Use

- The decision is trivial, reversible, and low-impact — just do it
- An existing, current spec already covers the need — reuse it instead
- You lack the inputs to do it well — gather them first (don't guess)

## Capabilities & Focus Areas

- Reuse-first: search the codebase, standard library, and existing modules before writing new code (DRY)
- YAGNI: build only what a current, real requirement needs — defer the speculative
- KISS: choose the simplest design that meets the requirement; treat any added complexity as something to justify
- Right abstraction timing: tolerate duplication until the shared concept is proven (rule of three) — a wrong abstraction costs more than repetition
- Subtract: remove dead code, redundant layers, needless configuration, and unused flags
- Readability over cleverness: optimize for the next reader, not for fewer lines or a trick

## Inputs

- Project context, goals, and constraints
- Relevant existing artifacts (specs, code, docs, diagrams)
- Stakeholders and their success criteria
- Non-functional requirements and compliance obligations

## OpenSpec Workflow

Run the skill as five phases. Do not skip a phase; if a phase has no work,
record *why* and move on.

### 1. Discover

Establish context, constraints, and success criteria before proposing anything.

**Exit gate:** Problem, stakeholders, constraints, and success criteria are written down and agreed.

### 2. Specify

Capture the intended outcome as a reviewable spec / proposal — the source of truth.

**Exit gate:** A reviewable spec exists with scope, non-goals, assumptions, and objective acceptance criteria.

### 3. Design

Decide the approach, record trade-offs, and document decisions (ADRs).

**Exit gate:** Approach chosen from ≥2 options; trade-offs and the decision are recorded as an ADR.

### 4. Validate

Prove the spec is correct, complete, and testable against the quality gates.

**Exit gate:** All applicable checklist gates pass or are waived; a domain expert has reviewed it.

### 5. Deliver

Produce the final artifact, hand it off, and define how it will be maintained.

**Exit gate:** Artifact is in the spec registry with an owner, review cadence, and handoff done.


## Deliverables

- Simplicity & reuse review notes (what was reused, simplified, or deleted, with rationale)
- A short project simplicity guideline (the codebase's DRY/KISS/YAGNI rules)
- A reuse index of shared utilities and where to find them

## Roles & RACI

- **Driver** — owns the artifact and runs the workflow
- **Reviewers** — domain experts who approve the spec
- **Stakeholders** — consume the outcome and accept the result

## Success Metrics

Track these to know the skill delivered value:

- Net lines of code (added minus removed)
- Code duplication / clone ratio (%)
- Cyclomatic complexity trend
- Reuse rate of shared utilities

## Quality Gates

The full, checkable gate list lives in [`checklist.md`](./checklist.md). Treat
it as the definition of done — a deliverable is not complete until every
applicable item is checked or explicitly waived with a recorded reason.

## Templates

- `templates/simplicity-review.md` — Simplicity & Reuse Review
- `templates/simplicity-guideline.md` — Simplicity Guideline

## Prompts

Copy-paste prompts that drive each phase live in
[`prompts/prompts.md`](./prompts/prompts.md).

## Worked Examples

See [`examples.md`](./examples.md) for realistic, end-to-end walkthroughs.

## Anti-Patterns to Avoid

- Copy-pasting logic into a third place instead of extracting it
- Adding abstraction or configuration for an imagined future requirement
- Choosing a clever solution over a clear one

---
*Part of the Enterprise OpenSpec Skill Catalog. Generated artifact — edit the
skill definition and regenerate to change.*
