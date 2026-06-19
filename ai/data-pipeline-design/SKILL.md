---
name: data-pipeline-design
title: Data Pipeline Design
description: >-
  Design reliable ingestion and transformation pipelines that move data correctly and observably.
category: AI & Data
version: 1.0.0
updated: 2026-06-19
license: Apache-2.0
openspec:
  spec_version: "1.0"
  lifecycle: [discover, specify, design, validate, deliver]
  artifact_type: skill
tags:
  - ai
---

# Data Pipeline Design

> **Category:** AI & Data · **Skill:** `data-pipeline-design` · **OpenSpec lifecycle skill**

## Purpose

Move data from sources to destinations correctly, on time, and observably. Design the ingestion, validation, transformation, and loading stages — batch or streaming — so downstream consumers (analytics, search, RAG, ML) receive trustworthy, fresh data without silent corruption.

This skill is spec-driven: it produces a reviewable artifact *before* work
begins, records the decisions and trade-offs behind it, and defines the quality
gates that say when it is done. The artifact — not tribal knowledge — is the
source of truth.

## When to Use

- Starting work that requires data pipeline design as a deliberate, documented step
- A decision here is hard to reverse, cross-team, or high-impact
- You need a reviewable artifact others can build on or audit
- Onboarding, handoff, or compliance requires the reasoning to be explicit

## When *Not* to Use

- The decision is trivial, reversible, and low-impact — just do it
- An existing, current spec already covers the need — reuse it instead
- You lack the inputs to do it well — gather them first (don't guess)

## Capabilities & Focus Areas

- Source/sink inventory and the batch vs streaming decision
- Pipeline stages: ingest/extract, validate, transform, load (ETL/ELT)
- Schema management, source contracts, and schema-drift handling
- Data-quality checks, deduplication, and idempotent/exactly-once processing
- Orchestration, scheduling, dependencies, and backfills
- Lineage, freshness SLAs, observability, and failure recovery/replay

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

- Data pipeline design (stages, schemas, and a data-flow diagram)
- Data-quality and validation rules
- Orchestration, scheduling, and backfill plan

## Roles & RACI

- **Driver** — owns the artifact and runs the workflow
- **Reviewers** — domain experts who approve the spec
- **Stakeholders** — consume the outcome and accept the result

## Success Metrics

Track these to know the skill delivered value:

- Data freshness / end-to-end latency
- Data-quality pass rate
- Pipeline success rate
- Backfill / replay time

## Quality Gates

The full, checkable gate list lives in [`checklist.md`](./checklist.md). Treat
it as the definition of done — a deliverable is not complete until every
applicable item is checked or explicitly waived with a recorded reason.

## Templates

- `templates/pipeline-design.md` — Data Pipeline Design
- `templates/data-quality-rules.md` — Data Quality Rules

## Prompts

Copy-paste prompts that drive each phase live in
[`prompts/prompts.md`](./prompts/prompts.md).

## Worked Examples

See [`examples.md`](./examples.md) for realistic, end-to-end walkthroughs.

## Anti-Patterns to Avoid

- Pipelines with no data-quality checks that propagate corruption downstream
- Non-idempotent loads that double-count on retry or backfill
- No schema-drift handling, so an upstream change breaks the pipeline silently

---
*Part of the Enterprise OpenSpec Skill Catalog. Generated artifact — edit the
skill definition and regenerate to change.*
