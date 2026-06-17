# Model Fine-Tuning — Quality Gate Checklist

> Definition of done for the `model-finetuning` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `model-finetuning` · **Category:** AI & Data · **Version:** 1.0.0

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

- [ ] Addressed: fine-tune vs prompt vs RAG decision
- [ ] Addressed: dataset curation, labeling, and quality/bias checks
- [ ] Addressed: method selection (full, LoRA/PEFT, instruction, DPO/RLHF)
- [ ] Addressed: training setup, hyperparameters, and compute
- [ ] Addressed: evaluation vs baseline and regression/safety checks

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: fine-tuning when prompting/RAG would suffice
- [ ] Confirmed avoided: training on small, biased, or leaky data
- [ ] Confirmed avoided: no baseline comparison to prove the gain
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Fine-tuning decision and plan
- [ ] Produced: Curated, documented training dataset
- [ ] Produced: Eval results vs baseline
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
