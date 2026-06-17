# SSL/TLS Management — Quality Gate Checklist

> Definition of done for the `ssl-management` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `ssl-management` · **Category:** DevOps & Platform · **Version:** 1.0.0

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

- [ ] Addressed: certificate lifecycle and automated renewal (ACME)
- [ ] Addressed: protocol/cipher hardening and HSTS
- [ ] Addressed: certificate storage, rotation, and inventory
- [ ] Addressed: wildcard/SAN, mTLS, and internal CA decisions
- [ ] Addressed: expiry monitoring and incident prevention

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: manual renewals that lapse and cause outages
- [ ] Confirmed avoided: legacy protocols/ciphers (TLS 1.0/1.1) enabled
- [ ] Confirmed avoided: untracked certs with no expiry alerting
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: TLS configuration standard
- [ ] Produced: Automated renewal and inventory
- [ ] Produced: Expiry monitoring/alerting
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
