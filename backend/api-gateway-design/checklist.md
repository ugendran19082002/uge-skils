# API Gateway Design — Quality Gate Checklist

> Definition of done for the `api-gateway-design` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `api-gateway-design` · **Category:** Backend · **Version:** 1.0.0

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

- [ ] Addressed: routing, aggregation, and protocol translation (REST/gRPC/GraphQL)
- [ ] Addressed: edge authn/authz, key management, and token validation
- [ ] Addressed: rate limiting, quotas, throttling, and circuit breaking
- [ ] Addressed: versioning, canary routing, and request/response transformation
- [ ] Addressed: edge observability, tracing propagation, and WAF integration

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: putting business logic in the gateway — a new monolith
- [ ] Confirmed avoided: no rate limiting — one client can starve the rest
- [ ] Confirmed avoided: breaking clients with unversioned routing changes
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Gateway routing and policy design
- [ ] Produced: Edge auth, rate-limit, and quota plan
- [ ] Produced: Versioning and canary routing strategy
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
