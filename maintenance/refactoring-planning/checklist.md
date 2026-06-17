# Refactoring Planning — Quality Gate Checklist

> Definition of done for the `refactoring-planning` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `refactoring-planning` · **Category:** Maintenance & Operations · **Version:** 1.0.0

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

- [ ] Addressed: target identification (hotspots, complexity, churn)
- [ ] Addressed: behavior-preservation via test coverage first
- [ ] Addressed: incremental strangler/branch-by-abstraction strategy
- [ ] Addressed: risk assessment and rollback points
- [ ] Addressed: measuring improvement and avoiding scope creep

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: big-bang rewrites disguised as refactoring
- [ ] Confirmed avoided: refactoring without tests to catch behavior changes
- [ ] Confirmed avoided: mixing refactoring and feature changes in one commit
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Refactoring plan with sequenced steps
- [ ] Produced: Coverage/safety-net assessment
- [ ] Produced: Before/after quality metrics
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
