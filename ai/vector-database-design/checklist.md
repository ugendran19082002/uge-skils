# Vector Database Design — Quality Gate Checklist

> Definition of done for the `vector-database-design` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `vector-database-design` · **Category:** AI & Data · **Version:** 1.0.0

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

- [ ] Addressed: vector store selection and deployment model
- [ ] Addressed: index type (HNSW, IVF, etc.) and parameter tuning
- [ ] Addressed: distance metric and embedding dimensionality
- [ ] Addressed: metadata filtering and hybrid search
- [ ] Addressed: recall/latency trade-offs, sharding, and scaling

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: default index params without recall/latency testing
- [ ] Confirmed avoided: mismatched distance metric vs embedding model
- [ ] Confirmed avoided: ignoring metadata filtering and re-indexing cost
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Vector DB design and configuration
- [ ] Produced: Index/parameter tuning plan
- [ ] Produced: Scaling and cost model
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
