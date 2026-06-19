---
name: frontend-testing
title: Frontend Testing
description: >-
  Build a layered frontend test strategy that catches regressions cheaply.
category: Frontend
version: 1.0.0
updated: 2026-06-19
license: Apache-2.0
openspec:
  spec_version: "1.0"
  lifecycle: [discover, specify, design, validate, deliver]
  artifact_type: skill
tags:
  - frontend
---

# Frontend Testing

> **Category:** Frontend · **Skill:** `frontend-testing` · **OpenSpec lifecycle skill**

## Purpose

Define what to test and at which level — unit, component, integration, e2e, visual — to maximize confidence per minute of test runtime.

This skill is spec-driven: it produces a reviewable artifact *before* work
begins, records the decisions and trade-offs behind it, and defines the quality
gates that say when it is done. The artifact — not tribal knowledge — is the
source of truth.

## When to Use

- Starting work that requires frontend testing as a deliberate, documented step
- A decision here is hard to reverse, cross-team, or high-impact
- You need a reviewable artifact others can build on or audit
- Onboarding, handoff, or compliance requires the reasoning to be explicit

## When *Not* to Use

- The decision is trivial, reversible, and low-impact — just do it
- An existing, current spec already covers the need — reuse it instead
- You lack the inputs to do it well — gather them first (don't guess)

## Capabilities & Focus Areas

- Test pyramid for the frontend and what each layer owns
- Component testing with user-centric queries
- Mocking the network at the boundary and test-data strategy
- Visual-regression and accessibility testing
- Flake control, determinism, and CI integration

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

- Frontend test strategy
- Coverage targets per layer
- Flake and CI policy

## Roles & RACI

- **Driver** — owns the artifact and runs the workflow
- **Reviewers** — domain experts who approve the spec
- **Stakeholders** — consume the outcome and accept the result

## Success Metrics

Track these to know the skill delivered value:

- Critical-path coverage
- Flake rate
- Test runtime

## Quality Gates

The full, checkable gate list lives in [`checklist.md`](./checklist.md). Treat
it as the definition of done — a deliverable is not complete until every
applicable item is checked or explicitly waived with a recorded reason.

## Templates

- `templates/fe-test-strategy.md` — Frontend Test Strategy
- `templates/test-plan.md` — Test Plan

## Prompts

Copy-paste prompts that drive each phase live in
[`prompts/prompts.md`](./prompts/prompts.md).

## Worked Examples

See [`examples.md`](./examples.md) for realistic, end-to-end walkthroughs.

## Anti-Patterns to Avoid

- Testing implementation details that break on refactor
- An inverted pyramid — slow e2e for everything
- Tolerating flaky tests instead of fixing them

---
*Part of the Enterprise OpenSpec Skill Catalog. Generated artifact — edit the
skill definition and regenerate to change.*
