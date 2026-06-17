# AI Evaluation — Quality Gate Checklist

> Definition of done for the `ai-evaluation` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `ai-evaluation` · **Category:** AI & Data · **Version:** 1.0.0

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

- [ ] Addressed: eval dataset construction and golden sets
- [ ] Addressed: metric selection (task metrics, faithfulness, safety)
- [ ] Addressed: LLM-as-judge design and human eval calibration
- [ ] Addressed: offline vs online eval and A/B testing
- [ ] Addressed: regression gating and continuous evaluation in CI

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: LLM-as-judge with no human calibration
- [ ] Confirmed avoided: evaluating on data the model trained/was tuned on (leakage)
- [ ] Confirmed avoided: one-off eval rather than a regression gate
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Evaluation harness with datasets and metrics
- [ ] Produced: Baseline scores and release gates
- [ ] Produced: Continuous-eval integration
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
