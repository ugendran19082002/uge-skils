# Search Architecture — Quality Gate Checklist

> Definition of done for the `search-architecture` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `search-architecture` · **Category:** Backend · **Version:** 1.0.0

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

- [ ] Addressed: search engine selection (full-text, vector, hybrid)
- [ ] Addressed: index modeling, analyzers, and mapping
- [ ] Addressed: relevance tuning, ranking, and faceting
- [ ] Addressed: indexing pipeline and source-of-truth sync
- [ ] Addressed: query performance, pagination, and observability

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: using SQL LIKE for real search workloads
- [ ] Confirmed avoided: index drift — search results don't match the source
- [ ] Confirmed avoided: tuning relevance with no evaluation set to measure it
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Search architecture and index design
- [ ] Produced: Relevance/ranking strategy
- [ ] Produced: Indexing/sync pipeline design
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
