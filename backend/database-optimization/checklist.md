# Database Optimization — Quality Gate Checklist

> Definition of done for the `database-optimization` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `database-optimization` · **Category:** Backend · **Version:** 1.0.0

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

- [ ] Addressed: slow-query identification and EXPLAIN plan analysis
- [ ] Addressed: index design, covering indexes, and index hygiene
- [ ] Addressed: query rewriting and N+1 elimination
- [ ] Addressed: connection pooling, caching, and read replicas
- [ ] Addressed: partitioning, vacuum/stats, and configuration tuning

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: adding indexes blindly without checking plans
- [ ] Confirmed avoided: optimizing queries that aren't the bottleneck
- [ ] Confirmed avoided: fixing symptoms in app code instead of the query/schema
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Optimization report with before/after metrics
- [ ] Produced: Index and query change set
- [ ] Produced: Monitoring for regression
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
