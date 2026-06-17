# Backend Architecture — Quality Gate Checklist

> Definition of done for the `backend-architecture` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `backend-architecture` · **Category:** Architecture · **Version:** 1.0.0

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

- [ ] Addressed: service boundary and responsibility definition
- [ ] Addressed: data ownership and consistency model (per-service data)
- [ ] Addressed: sync vs async communication and contracts
- [ ] Addressed: cross-cutting concerns (auth, logging, idempotency, retries)
- [ ] Addressed: layering, modularity, and dependency direction

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: distributed monolith — services that can't deploy independently
- [ ] Confirmed avoided: shared database across service boundaries
- [ ] Confirmed avoided: synchronous chains that fail together under load
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Backend architecture document with service map
- [ ] Produced: Data ownership and consistency decisions
- [ ] Produced: Communication and contract standards
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
