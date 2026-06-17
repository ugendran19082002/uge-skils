# Service Design — Quality Gate Checklist

> Definition of done for the `service-design` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `service-design` · **Category:** Backend · **Version:** 1.0.0

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

- [ ] Addressed: single-responsibility boundary and public contract
- [ ] Addressed: data ownership and persistence choice
- [ ] Addressed: dependency, timeout, retry, and circuit-breaker policy
- [ ] Addressed: idempotency, concurrency, and consistency handling
- [ ] Addressed: observability, health checks, and SLOs

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: a service that owns no data and just forwards calls
- [ ] Confirmed avoided: no timeouts/retries — one slow dependency cascades
- [ ] Confirmed avoided: no health checks or SLOs to operate against
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Service spec (contract, data, dependencies)
- [ ] Produced: Failure-mode and resilience plan
- [ ] Produced: SLOs and observability plan
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
