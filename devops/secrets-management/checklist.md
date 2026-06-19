# Secrets Management — Quality Gate Checklist

> Definition of done for the `secrets-management` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `secrets-management` · **Category:** DevOps & Platform · **Version:** 1.0.0

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

- [ ] Addressed: secret store selection (a dedicated secrets manager or cloud KMS)
- [ ] Addressed: dynamic/short-lived secrets and rotation
- [ ] Addressed: access control, scoping, and auditing
- [ ] Addressed: injection into apps/CI without exposure
- [ ] Addressed: leak detection and revocation procedures

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: secrets in git, env files, or CI variables in plaintext
- [ ] Confirmed avoided: long-lived static secrets never rotated
- [ ] Confirmed avoided: no audit trail of who accessed what
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Secrets management design and policy
- [ ] Produced: Rotation and access model
- [ ] Produced: Leak-response procedure
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
