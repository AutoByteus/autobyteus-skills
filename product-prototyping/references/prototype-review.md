# Prototype Review

Use this checklist after implementing the critical journey and before reporting the prototype as ready for product review.

## Runtime Checks

- Start the documented development command from the prototype folder.
- Open the documented entry route in a browser.
- Confirm the initial screen renders without console or asset-loading errors.
- Exercise the critical journey from start to success.
- Exercise each required service scenario and confirm visible feedback and recovery.
- Run `npm run build` or the project's equivalent build command.
- Run available typecheck, lint, unit, and browser checks.

## Behavior Checks

- Every documented action has a visible result.
- Every important transition has a stable ID and target state.
- Loading states prevent confusing duplicate actions.
- Success states explain what happened and what to do next.
- Error and empty states explain the situation and offer recovery.
- Service scenarios do not bypass frontend validation or state logic.
- The prototype does not depend on a live backend unless the user explicitly requested an integration prototype.

## Product Review Checks

- The prototype communicates the product story without requiring source-code knowledge.
- The critical journey is short enough to review but complete enough to expose the product decision.
- Copy, data, and labels are specific to the requested product rather than generic filler.
- Responsive layout remains usable at desktop and narrow mobile widths.
- Keyboard focus, labels, contrast intent, and readable hierarchy are present.
- Mocked behavior, assumptions, and production gaps are visible in the runbook or assumptions artifact.
- The prototype does not present unapproved behavior as a confirmed requirement.

## Aesthetic Checks

Treat this as an acceptance gate for the prototype, not optional polish. Review the entry screen, primary journey, and key loading, success, empty, and error states at desktop and narrow mobile sizes.

- The visual direction is specific to the product, audience, and context rather than a generic starter template.
- The shell, content, controls, and states share a coherent hierarchy, spacing rhythm, typography system, color roles, surfaces, borders, radii, and shadows.
- Headings, body text, labels, metadata, and actions have intentional scale, weight, line-height, and wrapping.
- Icons use one consistent family, size logic, and alignment; icon-only controls have clear accessible names and tooltips where needed.
- Primary actions, secondary actions, disabled states, loading states, errors, empty states, and success feedback are visually distinct and polished.
- Content density, imagery, data shapes, and copy feel credible for the product domain.
- Screenshots show no avoidable overlap, clipping, awkward wrapping, accidental whitespace, inconsistent alignment, layout shift, or unstyled browser controls.
- The prototype does not rely on decoration that obscures the product, interaction, or information hierarchy.

Record the final visual review in `prototype-runbook.md` or the behavior matrix, including the reviewed viewport sizes and any remaining aesthetic limitation.

## Reporting

Report:

- the prototype location and local URL;
- the journey and scenarios tested;
- the checks that passed;
- known limitations and mocked boundaries;
- decisions still requiring product or design confirmation.
