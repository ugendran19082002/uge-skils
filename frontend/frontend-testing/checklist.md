# Frontend Testing — Quality Gate Checklist

> Definition of done for the `frontend-testing` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `frontend-testing` · **Category:** Frontend · **Version:** 1.0.0

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

- [ ] Addressed: test pyramid for the frontend and what each layer owns
- [ ] Addressed: component testing with user-centric queries
- [ ] Addressed: mocking network (MSW) and test data strategy
- [ ] Addressed: visual-regression and accessibility testing
- [ ] Addressed: flake control, determinism, and CI integration

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: testing implementation details that break on refactor
- [ ] Confirmed avoided: an inverted pyramid — slow e2e for everything
- [ ] Confirmed avoided: tolerating flaky tests instead of fixing them
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Frontend test strategy
- [ ] Produced: Coverage targets per layer
- [ ] Produced: Flake and CI policy
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
