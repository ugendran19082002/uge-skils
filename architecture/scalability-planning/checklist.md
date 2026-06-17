# Scalability Planning — Quality Gate Checklist

> Definition of done for the `scalability-planning` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `scalability-planning` · **Category:** Architecture · **Version:** 1.0.0

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

- [ ] Addressed: load modeling and capacity planning
- [ ] Addressed: horizontal vs vertical scaling and statelessness
- [ ] Addressed: bottleneck and single-point-of-failure analysis
- [ ] Addressed: caching, partitioning/sharding, and queueing strategies
- [ ] Addressed: autoscaling policies and load/soak testing

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: premature optimization for scale you'll never reach
- [ ] Confirmed avoided: stateful services that block horizontal scaling
- [ ] Confirmed avoided: no load testing to validate the assumptions
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Scalability plan with capacity targets
- [ ] Produced: Bottleneck and SPOF inventory
- [ ] Produced: Scaling and autoscaling strategy
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
