# Testing Strategy — Quality Gate Checklist

> Definition of done for the `testing-strategy` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `testing-strategy` · **Category:** Testing & Quality · **Version:** 1.0.0

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

- [ ] Addressed: test pyramid/trophy and level responsibilities
- [ ] Addressed: coverage targets and risk-based prioritization
- [ ] Addressed: test environments and data management
- [ ] Addressed: automation vs manual and exploratory testing
- [ ] Addressed: quality gates, ownership, and shift-left practices

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: coverage-percentage worship over meaningful tests
- [ ] Confirmed avoided: inverted pyramid — slow, brittle, expensive suites
- [ ] Confirmed avoided: no environment/data strategy — flaky, unrepeatable runs
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Test strategy document
- [ ] Produced: Coverage targets per level
- [ ] Produced: Quality gate and ownership model
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
