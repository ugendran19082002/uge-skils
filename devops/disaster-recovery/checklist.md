# Disaster Recovery — Quality Gate Checklist

> Definition of done for the `disaster-recovery` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `disaster-recovery` · **Category:** DevOps & Platform · **Version:** 1.0.0

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

- [ ] Addressed: business impact analysis and RPO/RTO per system
- [ ] Addressed: DR strategy (backup-restore, pilot-light, warm/hot standby)
- [ ] Addressed: failover/failback procedures and dependencies
- [ ] Addressed: DR drills and game-day testing
- [ ] Addressed: communication plan and decision authority

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: a DR plan that has never been drilled
- [ ] Confirmed avoided: recovery depending on the very system that's down
- [ ] Confirmed avoided: undefined decision authority — paralysis during the disaster
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: DR plan with RPO/RTO and strategy
- [ ] Produced: Failover/failback runbooks
- [ ] Produced: DR drill results
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
