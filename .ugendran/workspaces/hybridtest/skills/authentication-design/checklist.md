# Authentication Design — Quality Gate Checklist

> Definition of done for the `authentication-design` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `authentication-design` · **Category:** Backend · **Version:** 1.0.0

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

- [ ] Addressed: authN protocol selection (OIDC/OAuth2, SAML, passkeys)
- [ ] Addressed: token vs session design and lifetimes/rotation
- [ ] Addressed: MFA, passwordless, and account-recovery flows
- [ ] Addressed: credential storage (hashing) and secret handling
- [ ] Addressed: federation, SSO, and service-to-service auth

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: rolling your own crypto/token format
- [ ] Confirmed avoided: long-lived tokens with no rotation or revocation
- [ ] Confirmed avoided: storing passwords with fast or reversible hashing
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Authentication design with chosen protocol
- [ ] Produced: Token/session lifecycle and rotation policy
- [ ] Produced: MFA and recovery flow design
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
