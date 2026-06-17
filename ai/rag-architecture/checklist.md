# RAG Architecture — Quality Gate Checklist

> Definition of done for the `rag-architecture` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `rag-architecture` · **Category:** AI & Data · **Version:** 1.0.0

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

- [ ] Addressed: ingestion, chunking, and metadata strategy
- [ ] Addressed: embedding model selection and vector store design
- [ ] Addressed: retrieval (dense/sparse/hybrid), re-ranking, and filtering
- [ ] Addressed: context assembly, prompting, and citation
- [ ] Addressed: freshness, evaluation, and hallucination control

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: naive fixed-size chunking that splits meaning
- [ ] Confirmed avoided: no re-ranking — irrelevant context drowns the answer
- [ ] Confirmed avoided: no retrieval/grounding evaluation
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: RAG architecture document
- [ ] Produced: Chunking/embedding/retrieval design
- [ ] Produced: Evaluation harness and metrics
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
