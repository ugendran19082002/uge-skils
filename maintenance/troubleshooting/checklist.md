# Troubleshooting — Quality Gate Checklist

> Definition of done for the `troubleshooting` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `troubleshooting` · **Category:** Maintenance & Operations · **Version:** 1.0.0

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

- [ ] Addressed: reproduction and symptom characterization
- [ ] Addressed: evidence gathering (logs, metrics, traces, state)
- [ ] Addressed: hypothesis-driven, binary-search isolation
- [ ] Addressed: root-cause vs symptom distinction
- [ ] Addressed: fix verification and knowledge capture

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: changing many things at once so the real cause stays hidden
- [ ] Confirmed avoided: fixing the symptom and leaving the root cause
- [ ] Confirmed avoided: not capturing the lesson — the same issue recurs
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Diagnosis writeup (symptom → root cause)
- [ ] Produced: Verified fix
- [ ] Produced: Runbook/knowledge-base entry
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
