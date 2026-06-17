# Database Design — Quality Gate Checklist

> Definition of done for the `database-design` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `database-design` · **Category:** Architecture · **Version:** 1.0.0

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

- [ ] Addressed: conceptual / logical / physical modeling
- [ ] Addressed: normalization vs deliberate denormalization
- [ ] Addressed: indexing and access-pattern-driven design
- [ ] Addressed: constraints, integrity, and transactions
- [ ] Addressed: migration and schema-evolution strategy

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: modeling tables before knowing the query patterns
- [ ] Confirmed avoided: no constraints — relying on app code for integrity
- [ ] Confirmed avoided: big-bang migrations with no rollback
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: ERD and schema definition (DDL)
- [ ] Produced: Indexing and access-pattern notes
- [ ] Produced: Migration plan
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
