# User Story Generation — Quality Gate Checklist

> Definition of done for the `user-story-generation` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `user-story-generation` · **Category:** Product · **Version:** 1.0.0

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

- [ ] Addressed: INVEST-compliant story slicing
- [ ] Addressed: role-goal-benefit framing ('As a... I want... so that...')
- [ ] Addressed: acceptance criteria in Given/When/Then
- [ ] Addressed: vertical slicing and story splitting patterns
- [ ] Addressed: definition of Ready and Definition of Done

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: horizontal slices (DB story, API story) with no user value
- [ ] Confirmed avoided: acceptance criteria that restate the title
- [ ] Confirmed avoided: epics masquerading as stories — too big to finish in a sprint
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Backlog of estimable, testable stories
- [ ] Produced: Acceptance criteria per story
- [ ] Produced: Definition of Ready / Done
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
