# Security Testing — Quality Gate Checklist

> Definition of done for the `security-testing` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `security-testing` · **Category:** Testing & Quality · **Version:** 1.0.0

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

- [ ] Addressed: SAST, DAST, IAST, and dependency/SCA scanning
- [ ] Addressed: OWASP Top 10 / ASVS-based test cases
- [ ] Addressed: authentication, authorization, and session testing
- [ ] Addressed: secrets, injection, and misconfiguration testing
- [ ] Addressed: penetration testing and findings triage

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: scanner-only testing with no manual logic testing
- [ ] Confirmed avoided: drowning in low-severity noise, missing critical issues
- [ ] Confirmed avoided: testing only at the end, not in CI/CD
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Security test plan mapped to ASVS/OWASP
- [ ] Produced: Findings report with severity (CVSS)
- [ ] Produced: Remediation and retest plan
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
