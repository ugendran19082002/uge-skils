# Prompt Engineering — Quality Gate Checklist

> Definition of done for the `prompt-engineering` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `prompt-engineering` · **Category:** AI & Data · **Version:** 1.0.0

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

- [ ] Addressed: prompt structure (role, instructions, context, examples, format)
- [ ] Addressed: few-shot, chain-of-thought, and decomposition techniques
- [ ] Addressed: output formatting (JSON/schema) and parsing robustness
- [ ] Addressed: prompt versioning, testing, and regression evals
- [ ] Addressed: injection resistance and failure handling

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: untracked prompt strings edited live in production
- [ ] Confirmed avoided: no eval set — 'it looked better' tuning
- [ ] Confirmed avoided: trusting model output format without validation
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Versioned prompt library with eval results
- [ ] Produced: Prompt spec per task (inputs/outputs/format)
- [ ] Produced: Regression eval set
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
