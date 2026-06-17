# Model Selection — Quality Gate Checklist

> Definition of done for the `model-selection` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `model-selection` · **Category:** AI & Data · **Version:** 1.0.0

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

- [ ] Addressed: requirement definition (quality, latency, cost, context, modality)
- [ ] Addressed: candidate shortlist (frontier vs small vs open vs fine-tuned)
- [ ] Addressed: task-specific benchmarking on representative data
- [ ] Addressed: cost/latency modeling at expected volume
- [ ] Addressed: data-residency, privacy, and licensing constraints

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: picking by leaderboard rank, not your task evals
- [ ] Confirmed avoided: ignoring cost/latency at production scale
- [ ] Confirmed avoided: no fallback when the chosen model is down or degraded
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Model selection decision record with benchmark data
- [ ] Produced: Cost/latency model at projected volume
- [ ] Produced: Fallback/routing strategy
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
