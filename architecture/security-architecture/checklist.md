# Security Architecture — Quality Gate Checklist

> Definition of done for the `security-architecture` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `security-architecture` · **Category:** Architecture · **Version:** 1.0.0

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

- [ ] Addressed: trust boundaries and zero-trust segmentation
- [ ] Addressed: identity, authN/authZ, and secrets architecture
- [ ] Addressed: data protection (encryption in transit/at rest, key management)
- [ ] Addressed: threat modeling integration (STRIDE) and security controls
- [ ] Addressed: compliance mapping and security logging/audit

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: perimeter-only security with a soft interior
- [ ] Confirmed avoided: secrets in code/config instead of a managed store
- [ ] Confirmed avoided: security designed after the architecture is frozen
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Security architecture document with trust boundaries
- [ ] Produced: Control catalogue mapped to threats
- [ ] Produced: Data-protection and key-management plan
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
