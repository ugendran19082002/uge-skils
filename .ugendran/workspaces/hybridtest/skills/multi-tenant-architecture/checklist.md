# Multi-Tenant Architecture — Quality Gate Checklist

> Definition of done for the `multi-tenant-architecture` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `multi-tenant-architecture` · **Category:** Architecture · **Version:** 1.0.0

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

- [ ] Addressed: isolation model (silo / pool / bridge) selection
- [ ] Addressed: tenant data isolation and the row/schema/db trade-off
- [ ] Addressed: tenant context propagation and request routing
- [ ] Addressed: per-tenant limits, metering, and noisy-neighbor control
- [ ] Addressed: tenant lifecycle (onboard, offboard, data export/delete)

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: a single missing tenant filter leaking cross-tenant data
- [ ] Confirmed avoided: one-size isolation when tiers need different guarantees
- [ ] Confirmed avoided: no noisy-neighbor controls — one tenant starves the rest
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Tenancy model decision with isolation guarantees
- [ ] Produced: Tenant data-isolation design
- [ ] Produced: Tenant lifecycle and metering plan
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
