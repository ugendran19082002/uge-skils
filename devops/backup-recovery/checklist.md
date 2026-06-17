# Backup & Recovery — Quality Gate Checklist

> Definition of done for the `backup-recovery` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `backup-recovery` · **Category:** DevOps & Platform · **Version:** 1.0.0

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

- [ ] Addressed: RPO/RTO definition per data set
- [ ] Addressed: backup scope, frequency, and retention
- [ ] Addressed: encryption, immutability, and offsite/air-gap copies
- [ ] Addressed: restore testing and verification
- [ ] Addressed: automation, monitoring, and the 3-2-1 rule

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: backups that are never restore-tested
- [ ] Confirmed avoided: backups stored with (and deletable by) the same credentials
- [ ] Confirmed avoided: no immutability — ransomware encrypts the backups too
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Backup & recovery plan with RPO/RTO
- [ ] Produced: Backup schedule and retention policy
- [ ] Produced: Restore-test procedure and results
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
