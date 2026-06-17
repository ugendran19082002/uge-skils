# Access Control Design — Quality Gate Checklist

> Definition of done for the `access-control-design` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `access-control-design` · **Category:** Security & Compliance · **Version:** 1.0.0

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

- [ ] Addressed: authorization model selection (RBAC, ABAC, ReBAC)
- [ ] Addressed: least privilege, separation of duties, and role design
- [ ] Addressed: policy enforcement points and centralization
- [ ] Addressed: privileged access and just-in-time elevation
- [ ] Addressed: access reviews, recertification, and audit

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: role explosion or one god-role everyone gets
- [ ] Confirmed avoided: authorization scattered and inconsistent across services
- [ ] Confirmed avoided: access granted and never reviewed or revoked
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Access control model and policy
- [ ] Produced: Role/permission matrix
- [ ] Produced: Access-review and audit process
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
