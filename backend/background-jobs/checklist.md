# Background Jobs — Quality Gate Checklist

> Definition of done for the `background-jobs` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `background-jobs` · **Category:** Backend · **Version:** 1.0.0

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

- [ ] Addressed: queue/broker selection and topology
- [ ] Addressed: job idempotency, retries, and backoff
- [ ] Addressed: dead-letter queues and poison-message handling
- [ ] Addressed: scheduling, prioritization, and concurrency limits
- [ ] Addressed: observability, alerting, and backpressure

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: non-idempotent jobs that double-charge on retry
- [ ] Confirmed avoided: no dead-letter queue — failures vanish silently
- [ ] Confirmed avoided: unbounded concurrency overwhelming downstreams
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Job processing design
- [ ] Produced: Retry/DLQ and idempotency policy
- [ ] Produced: Monitoring and alerting plan
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
