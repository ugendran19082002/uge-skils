# Server Hardening — Quality Gate Checklist

> Definition of done for the `server-hardening` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `server-hardening` · **Category:** DevOps & Platform · **Version:** 1.0.0

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

- [ ] Addressed: OS baseline and CIS-benchmark alignment
- [ ] Addressed: account, SSH, and least-privilege configuration
- [ ] Addressed: service minimization and firewall/host rules
- [ ] Addressed: patch management and automatic updates
- [ ] Addressed: audit logging, file integrity, and intrusion detection

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: default passwords/ports and unused services left on
- [ ] Confirmed avoided: root/password SSH login enabled
- [ ] Confirmed avoided: one-time hardening with no drift detection
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Hardening baseline/standard
- [ ] Produced: Compliance scan results vs benchmark
- [ ] Produced: Patch and audit plan
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
