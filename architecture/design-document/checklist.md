# Design Document — Quality Gate Checklist

> Definition of done for the `design-document` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `design-document` · **Category:** Architecture · **Version:** 1.0.0

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

- [ ] Addressed: context, problem statement, and goals/non-goals
- [ ] Addressed: proposed design with diagrams (C4, sequence, data flow)
- [ ] Addressed: alternatives considered and why rejected
- [ ] Addressed: cross-cutting concerns (security, scaling, observability, cost)
- [ ] Addressed: rollout, migration, and testing strategy

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: describing the solution without the alternatives or trade-offs
- [ ] Confirmed avoided: diagrams that don't match the prose
- [ ] Confirmed avoided: no non-goals, so review scope creeps endlessly
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Reviewed design document (RFC/TDD)
- [ ] Produced: Architecture diagrams
- [ ] Produced: Decision record of the chosen approach
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
