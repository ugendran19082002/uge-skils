# AI Monitoring — Quality Gate Checklist

> Definition of done for the `ai-monitoring` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `ai-monitoring` · **Category:** AI & Data · **Version:** 1.0.0

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

- [ ] Addressed: quality and output-drift monitoring
- [ ] Addressed: input/data-drift and distribution shift detection
- [ ] Addressed: safety, toxicity, and policy-violation monitoring
- [ ] Addressed: cost, latency, and token-usage tracking
- [ ] Addressed: feedback capture, alerting, and dashboards

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: monitoring infra metrics but not output quality
- [ ] Confirmed avoided: no drift detection — silent degradation over time
- [ ] Confirmed avoided: alerts with no thresholds tied to user impact
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: AI monitoring plan and dashboards
- [ ] Produced: Drift and safety alert thresholds
- [ ] Produced: Feedback-to-improvement loop
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
