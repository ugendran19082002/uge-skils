# Performance Testing — Quality Gate Checklist

> Definition of done for the `performance-testing` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `performance-testing` · **Category:** Testing & Quality · **Version:** 1.0.0

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

- [ ] Addressed: workload modeling and performance requirements
- [ ] Addressed: test types (load, stress, soak, spike, capacity)
- [ ] Addressed: tooling, scripting, and realistic data
- [ ] Addressed: bottleneck analysis and profiling
- [ ] Addressed: baselining, regression, and CI integration

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: testing with unrealistic data volumes/distributions
- [ ] Confirmed avoided: measuring averages and ignoring tail latency
- [ ] Confirmed avoided: one-off testing with no baseline or regression
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Performance test plan with targets
- [ ] Produced: Test scripts and workload model
- [ ] Produced: Results report with bottlenecks
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
