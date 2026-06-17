# State Management — Quality Gate Checklist

> Definition of done for the `state-management` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `state-management` · **Category:** Frontend · **Version:** 1.0.0

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

- [ ] Addressed: state categorization (server, URL, form, UI, global)
- [ ] Addressed: server-state caching (query libraries) vs client state
- [ ] Addressed: store design, selectors, and normalization
- [ ] Addressed: derived state and avoiding redundant sources of truth
- [ ] Addressed: performance (re-render control, memoization, splitting)

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: putting server data in a global store and hand-syncing it
- [ ] Confirmed avoided: one mega-store causing app-wide re-renders
- [ ] Confirmed avoided: duplicating the same truth in multiple places
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: State architecture decision record
- [ ] Produced: State ownership map
- [ ] Produced: Caching/invalidation strategy
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
