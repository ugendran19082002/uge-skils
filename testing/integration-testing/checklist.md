# Integration Testing — Quality Gate Checklist

> Definition of done for the `integration-testing` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `integration-testing` · **Category:** Testing & Quality · **Version:** 1.0.0

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

- [ ] Addressed: integration scope and boundary selection
- [ ] Addressed: realistic dependencies (testcontainers, sandboxes)
- [ ] Addressed: contract and API integration testing
- [ ] Addressed: test data setup/teardown and isolation
- [ ] Addressed: failure-mode and resilience testing

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: mocking the very integration you meant to test
- [ ] Confirmed avoided: shared mutable test data causing cross-test flake
- [ ] Confirmed avoided: only happy-path integration, no failure injection
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Integration test plan and harness
- [ ] Produced: Environment/data setup approach
- [ ] Produced: Boundary coverage map
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
