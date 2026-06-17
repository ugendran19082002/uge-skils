# Accessibility Review — Prompts

Copy-paste prompts to drive the `accessibility-review` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

### Discover

```
You are an expert in accessibility review. Given this context:
<context>
...
</context>
Identify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:
- WCAG 2.2 AA conformance auditing
- Keyboard, focus order, and screen-reader testing
- Color contrast, target size, and motion preferences
- Semantic HTML and ARIA correctness
- Automated + manual + assistive-tech testing
List what you still need to know before proceeding.
```

### Specify

```
Using the discovered context, draft a reviewable Accessibility Review spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria.
```

### Design & decide

```
Propose 2-3 viable approaches for <decision> in the context of accessibility review. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded.
```

### Validate (anti-pattern check)

```
Review the Accessibility Review artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:
- Relying only on automated scanners (catch ~30%)
- ARIA-over-HTML — reinventing native semantics badly
- Treating a11y as a one-off audit, not a standard
List the top risks and a mitigation for each.
```

### Deliver

```
Finalize the Accessibility Review artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders.
```

## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
