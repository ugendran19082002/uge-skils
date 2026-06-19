# Feature Flag Management — Quality Gate Checklist

> Definition of done for the `feature-flag-management` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `feature-flag-management` · **Category:** Maintenance & Operations · **Version:** 1.0.0

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

- [ ] Addressed: flag types (release, ops, experiment, permission) and lifecycle
- [ ] Addressed: targeting, segmentation, and gradual/percentage rollout
- [ ] Addressed: kill switches, defaults, and fail-safe evaluation
- [ ] Addressed: experimentation/A-B integration and metrics
- [ ] Addressed: flag debt: ownership, expiry, and systematic cleanup

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: flags that never get removed — permanent dead branches
- [ ] Confirmed avoided: no default/fail-safe when the flag service is down
- [ ] Confirmed avoided: testing only one side of the flag
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Flag taxonomy and lifecycle policy
- [ ] Produced: Rollout, targeting, and kill-switch plan
- [ ] Produced: Flag cleanup/expiry process
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
