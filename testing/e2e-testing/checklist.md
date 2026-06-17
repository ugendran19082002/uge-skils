# End-to-End Testing — Quality Gate Checklist

> Definition of done for the `e2e-testing` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `e2e-testing` · **Category:** Testing & Quality · **Version:** 1.0.0

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

- [ ] Addressed: critical user-journey selection
- [ ] Addressed: stable selectors and resilient locators
- [ ] Addressed: test data, environment, and state management
- [ ] Addressed: flake reduction (waits, retries, isolation)
- [ ] Addressed: cross-browser/device and CI/parallelization

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: e2E-testing everything instead of critical paths
- [ ] Confirmed avoided: brittle selectors (CSS/text) that break on UI tweaks
- [ ] Confirmed avoided: tolerating flaky e2e that erode trust in the suite
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: E2E suite covering critical journeys
- [ ] Produced: Flake-control and data strategy
- [ ] Produced: CI integration plan
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
