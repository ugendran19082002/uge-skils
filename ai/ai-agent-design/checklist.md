# AI Agent Design — Quality Gate Checklist

> Definition of done for the `ai-agent-design` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `ai-agent-design` · **Category:** AI & Data · **Version:** 1.0.0

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

- [ ] Addressed: task scoping, success criteria, and stop conditions
- [ ] Addressed: tool/function definitions and permissioning
- [ ] Addressed: control flow (single-shot, ReAct, planner-executor, multi-agent)
- [ ] Addressed: memory, context management, and state
- [ ] Addressed: guardrails, human-in-the-loop, and failure handling

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: giving an agent powerful tools with no permission scoping
- [ ] Confirmed avoided: no stop conditions — runaway loops and cost
- [ ] Confirmed avoided: demo-driven design with no eval of real task success
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Agent design spec (goal, tools, loop, limits)
- [ ] Produced: Tool contract definitions
- [ ] Produced: Guardrail and HITL plan
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
