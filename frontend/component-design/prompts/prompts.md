# Component Design — Prompts

Copy-paste prompts to drive the `component-design` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

### Discover

```
You are an expert in component design. Given this context:
<context>
...
</context>
Identify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:
- Component API (props/events/slots) and composition model
- State, variant, and interaction matrix
- Accessibility (roles, keyboard, focus, ARIA)
- Theming, tokens, and style encapsulation
- Stories, docs, and visual-regression coverage
List what you still need to know before proceeding.
```

### Specify

```
Using the discovered context, draft a reviewable Component Design spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria.
```

### Design & decide

```
Propose 2-3 viable approaches for <decision> in the context of component design. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded.
```

### Validate (anti-pattern check)

```
Review the Component Design artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:
- Over-configurable components with 30 boolean props
- Components that hard-code spacing/colors instead of tokens
- Skipping keyboard/focus handling
List the top risks and a mitigation for each.
```

### Deliver

```
Finalize the Component Design artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders.
```

## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
