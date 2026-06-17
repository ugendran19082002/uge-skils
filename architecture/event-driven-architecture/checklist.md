# Event-Driven Architecture — Quality Gate Checklist

> Definition of done for the `event-driven-architecture` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `event-driven-architecture` · **Category:** Architecture · **Version:** 1.0.0

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

- [ ] Addressed: event modeling, schemas, and a schema registry
- [ ] Addressed: delivery semantics (at-least/exactly-once) and idempotency
- [ ] Addressed: ordering, partitioning, and the outbox/saga patterns
- [ ] Addressed: choreography vs orchestration trade-offs
- [ ] Addressed: dead-letter handling, replay, and observability

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: events as disguised RPC (tight coupling, no autonomy)
- [ ] Confirmed avoided: no idempotency — duplicates corrupt state
- [ ] Confirmed avoided: unversioned event schemas that break consumers
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Event catalogue with versioned schemas
- [ ] Produced: Delivery-semantics and idempotency decisions
- [ ] Produced: Saga/outbox design for consistency
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
