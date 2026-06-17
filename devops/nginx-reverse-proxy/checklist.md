# Nginx Reverse Proxy — Quality Gate Checklist

> Definition of done for the `nginx-reverse-proxy` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `nginx-reverse-proxy` · **Category:** DevOps & Platform · **Version:** 1.0.0

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

- [ ] Addressed: server/location routing and upstream definitions
- [ ] Addressed: TLS termination, HTTP/2-3, and security headers
- [ ] Addressed: load balancing, healthchecks, and failover
- [ ] Addressed: caching, compression, and buffering
- [ ] Addressed: rate limiting, timeouts, and request limits

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: weak TLS config and missing security headers
- [ ] Confirmed avoided: no upstream healthchecks/timeouts — hung requests
- [ ] Confirmed avoided: default config exposing version and verbose errors
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Nginx configuration with TLS and routing
- [ ] Produced: Upstream/load-balancing setup
- [ ] Produced: Security-header and rate-limit policy
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
