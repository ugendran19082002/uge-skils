# Observability Design — Quality Gate Checklist

> Definition of done for the `observability-design` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `observability-design` · **Category:** DevOps & Platform · **Version:** 1.0.0

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

- [ ] Addressed: the three pillars: structured logs, metrics, traces
- [ ] Addressed: SLI/SLO definition and error budgets
- [ ] Addressed: correlation IDs and distributed tracing
- [ ] Addressed: dashboards, alerting, and signal-to-noise
- [ ] Addressed: cardinality, retention, and cost management

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: logging everything as unstructured text
- [ ] Confirmed avoided: alerting on causes, not symptoms — alert fatigue
- [ ] Confirmed avoided: high-cardinality metrics that explode cost
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Observability design (logs/metrics/traces)
- [ ] Produced: SLI/SLO and alerting plan
- [ ] Produced: Dashboard and instrumentation standards
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
