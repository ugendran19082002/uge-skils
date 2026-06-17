# Monitoring & Alerting — Quality Gate Checklist

> Definition of done for the `monitoring-alerting` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `monitoring-alerting` · **Category:** Maintenance & Operations · **Version:** 1.0.0

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

- [ ] Addressed: SLI/SLO-based, symptom-oriented alerting
- [ ] Addressed: alert thresholds, severity, and routing
- [ ] Addressed: actionability, runbooks, and ownership per alert
- [ ] Addressed: noise reduction (dedup, grouping, suppression)
- [ ] Addressed: on-call, escalation, and alert review

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: alerting on causes/low-level metrics, not user symptoms
- [ ] Confirmed avoided: alerts with no runbook or clear action
- [ ] Confirmed avoided: alert fatigue from noisy, non-actionable alerts
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Alerting plan tied to SLOs
- [ ] Produced: Alert catalog with runbooks and owners
- [ ] Produced: On-call/escalation policy
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
