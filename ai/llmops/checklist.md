# LLMOps — Quality Gate Checklist

> Definition of done for the `llmops` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `llmops` · **Category:** AI & Data · **Version:** 1.0.0

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

- [ ] Addressed: prompt/model versioning and deployment (canary, rollback)
- [ ] Addressed: observability (traces, tokens, latency, quality signals)
- [ ] Addressed: cost monitoring, budgets, and caching/routing
- [ ] Addressed: drift, feedback loops, and continuous evaluation
- [ ] Addressed: guardrail, rate-limit, and incident operations

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: shipping prompt/model changes with no versioning or rollback
- [ ] Confirmed avoided: no cost guardrails — runaway token spend
- [ ] Confirmed avoided: no production quality monitoring (drift goes unnoticed)
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: LLMOps runbook and deployment process
- [ ] Produced: Monitoring and cost dashboards
- [ ] Produced: Drift and incident response plan
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
