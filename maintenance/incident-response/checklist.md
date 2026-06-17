# Incident Response — Quality Gate Checklist

> Definition of done for the `incident-response` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `incident-response` · **Category:** Maintenance & Operations · **Version:** 1.0.0

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

- [ ] Addressed: severity classification and escalation
- [ ] Addressed: roles (incident commander, comms, ops) and runbooks
- [ ] Addressed: mitigation, communication, and status updates
- [ ] Addressed: coordination, timeline, and decision logging
- [ ] Addressed: blameless postmortem and action-item follow-through

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: no defined incident commander — chaotic response
- [ ] Confirmed avoided: blame culture that suppresses learning
- [ ] Confirmed avoided: postmortems with action items nobody completes
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Incident response plan and severity matrix
- [ ] Produced: Role definitions and runbooks
- [ ] Produced: Postmortem template and tracked actions
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
