# Domain-Driven Design — Quality Gate Checklist

> Definition of done for the `domain-driven-design` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `domain-driven-design` · **Category:** Architecture · **Version:** 1.0.0

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

- [ ] Addressed: ubiquitous language and domain glossary
- [ ] Addressed: bounded contexts and a context map
- [ ] Addressed: aggregates, entities, value objects, and invariants
- [ ] Addressed: domain events and application/domain layering
- [ ] Addressed: strategic vs tactical DDD and anti-corruption layers

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: anemic domain models — logic leaks into services
- [ ] Confirmed avoided: one giant model instead of bounded contexts
- [ ] Confirmed avoided: sharing models across contexts without an anti-corruption layer
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Context map with relationships
- [ ] Produced: Ubiquitous-language glossary
- [ ] Produced: Aggregate and domain-event model
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
