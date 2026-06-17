# AI Evaluation — Prompts

Copy-paste prompts to drive the `ai-evaluation` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

### Discover

```
You are an expert in ai evaluation. Given this context:
<context>
...
</context>
Identify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:
- Eval dataset construction and golden sets
- Metric selection (task metrics, faithfulness, safety)
- LLM-as-judge design and human eval calibration
- Offline vs online eval and A/B testing
- Regression gating and continuous evaluation in CI
List what you still need to know before proceeding.
```

### Specify

```
Using the discovered context, draft a reviewable AI Evaluation spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria.
```

### Design & decide

```
Propose 2-3 viable approaches for <decision> in the context of ai evaluation. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded.
```

### Validate (anti-pattern check)

```
Review the AI Evaluation artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:
- LLM-as-judge with no human calibration
- Evaluating on data the model trained/was tuned on (leakage)
- One-off eval rather than a regression gate
List the top risks and a mitigation for each.
```

### Deliver

```
Finalize the AI Evaluation artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders.
```

## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
