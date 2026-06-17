# Unit Testing — Quality Gate Checklist

> Definition of done for the `unit-testing` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `unit-testing` · **Category:** Testing & Quality · **Version:** 1.0.0

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

- [ ] Addressed: test structure (AAA), naming, and behavior focus
- [ ] Addressed: test doubles (mock/stub/fake/spy) and when to use each
- [ ] Addressed: boundary, equivalence, and property-based testing
- [ ] Addressed: determinism, isolation, and speed
- [ ] Addressed: coverage interpretation and mutation testing

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: testing private internals — brittle on refactor
- [ ] Confirmed avoided: over-mocking until tests assert the mocks, not behavior
- [ ] Confirmed avoided: non-deterministic tests (time, randomness, ordering)
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Unit test conventions and examples
- [ ] Produced: Test-double guidelines
- [ ] Produced: Coverage/mutation targets
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
