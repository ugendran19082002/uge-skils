# Guardrails Design — Quality Gate Checklist

> Definition of done for the `guardrails-design` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `guardrails-design` · **Category:** AI & Data · **Version:** 1.0.0

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

- [ ] Addressed: input validation, moderation, and prompt-injection defense
- [ ] Addressed: output filtering (toxicity, PII, policy, format)
- [ ] Addressed: topic/scope restriction and refusal design
- [ ] Addressed: sensitive-data leakage prevention
- [ ] Addressed: guardrail failure handling, logging, and HITL escalation

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: relying on the model's own judgment as the only guardrail
- [ ] Confirmed avoided: output-only filtering, ignoring injection at the input
- [ ] Confirmed avoided: silent guardrail failures with no logging/alerting
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Guardrail policy and control set
- [ ] Produced: Input/output validation design
- [ ] Produced: Violation handling and escalation plan
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
