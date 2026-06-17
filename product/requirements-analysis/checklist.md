# Requirements Analysis — Quality Gate Checklist

> Definition of done for the `requirements-analysis` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `requirements-analysis` · **Category:** Product · **Version:** 1.0.0

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

- [ ] Addressed: functional vs non-functional requirement separation
- [ ] Addressed: elicitation techniques and requirement prioritization
- [ ] Addressed: ambiguity, completeness, and consistency analysis
- [ ] Addressed: traceability matrix from need to requirement to test
- [ ] Addressed: acceptance criteria authoring (Given/When/Then)

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: ambiguous words ('fast', 'easy', 'secure') with no measure
- [ ] Confirmed avoided: mixing requirements with implementation detail
- [ ] Confirmed avoided: no traceability — orphan requirements and orphan tests
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Requirements specification (SRS) with IDs
- [ ] Produced: Requirements traceability matrix
- [ ] Produced: Acceptance criteria per requirement
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
