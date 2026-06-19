# Code Simplicity & Reuse — Prompts

Copy-paste prompts to drive the `code-simplicity-and-reuse` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

### Discover

```
You are an expert in code simplicity & reuse. Given this context:
<context>
...
</context>
Identify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:
- Reuse-first: search the codebase, standard library, and existing modules before writing new code (DRY)
- YAGNI: build only what a current, real requirement needs — defer the speculative
- KISS: choose the simplest design that meets the requirement; treat any added complexity as something to justify
- Right abstraction timing: tolerate duplication until the shared concept is proven (rule of three) — a wrong abstraction costs more than repetition
- Subtract: remove dead code, redundant layers, needless configuration, and unused flags
- Readability over cleverness: optimize for the next reader, not for fewer lines or a trick
List what you still need to know before proceeding.
```

### Specify

```
Using the discovered context, draft a reviewable Code Simplicity & Reuse spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria.
```

### Design & decide

```
Propose 2-3 viable approaches for <decision> in the context of code simplicity & reuse. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded.
```

### Validate (anti-pattern check)

```
Review the Code Simplicity & Reuse artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:
- Copy-pasting logic into a third place instead of extracting it
- Adding abstraction or configuration for an imagined future requirement
- Choosing a clever solution over a clear one
List the top risks and a mitigation for each.
```

### Deliver

```
Finalize the Code Simplicity & Reuse artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders.
```

## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
