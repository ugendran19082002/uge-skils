# Data Pipeline Design — Quality Gate Checklist

> Definition of done for the `data-pipeline-design` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `data-pipeline-design` · **Category:** AI & Data · **Version:** 1.0.0

## Discover

- [ ] Problem statement and success criteria are written down
- [ ] Stakeholders and their concerns are identified
- [ ] Constraints (time, budget, tech, compliance) are explicit
- [ ] Existing artifacts reviewed for reuse

## Specify

- [ ] Intended outcome captured as a reviewable spec
- [ ] Scope and non-goals stated
- [ ] Assumptions and open questions listed

## Design — domain coverage

- [ ] Addressed: source/sink inventory and the batch vs streaming decision
- [ ] Addressed: pipeline stages: ingest/extract, validate, transform, load (ETL/ELT)
- [ ] Addressed: schema management, source contracts, and schema-drift handling
- [ ] Addressed: data-quality checks, deduplication, and idempotent/exactly-once processing
- [ ] Addressed: orchestration, scheduling, dependencies, and backfills
- [ ] Addressed: lineage, freshness SLAs, observability, and failure recovery/replay

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: pipelines with no data-quality checks that propagate corruption downstream
- [ ] Confirmed avoided: non-idempotent loads that double-count on retry or backfill
- [ ] Confirmed avoided: no schema-drift handling, so an upstream change breaks the pipeline silently
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Data pipeline design (stages, schemas, and a data-flow diagram)
- [ ] Produced: Data-quality and validation rules
- [ ] Produced: Orchestration, scheduling, and backfill plan
- [ ] Final artifact stored in the spec registry
- [ ] Owner and review cadence assigned
- [ ] Handoff / communication done

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
