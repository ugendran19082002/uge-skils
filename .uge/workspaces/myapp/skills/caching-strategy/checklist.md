# Caching Strategy — Quality Gate Checklist

> Definition of done for the `caching-strategy` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `caching-strategy` · **Category:** Backend · **Version:** 1.0.0

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

- [ ] Addressed: cache layer selection (client, CDN, app, db) and topology
- [ ] Addressed: cache patterns (cache-aside, read/write-through, write-behind)
- [ ] Addressed: TTL, invalidation, and consistency trade-offs
- [ ] Addressed: key design, stampede protection, and warming
- [ ] Addressed: hit-ratio monitoring and eviction policy

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: caching with no invalidation plan — permanent stale data
- [ ] Confirmed avoided: caching highly volatile or per-user-sensitive data wrongly
- [ ] Confirmed avoided: no stampede protection — cache miss melts the origin
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Caching strategy per data type
- [ ] Produced: Invalidation and consistency plan
- [ ] Produced: Cache-key and TTL conventions
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
