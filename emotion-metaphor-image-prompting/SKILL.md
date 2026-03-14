---
name: emotion-metaphor-image-prompting
description: Craft and iteratively refine image-generation and image-edit prompts that turn subtle feelings, idioms, pressure, or social dynamics into concrete visual metaphors. Use when a user can describe the emotion but not the picture yet, when a generated image is close but not exact, or when Codex needs to preserve style while correcting one visible signal at a time.
---

# Emotion Metaphor Image Prompting

## Overview

Turn a vague emotional description into a concrete visual scene, then tighten the image through targeted edit prompts. Prefer visual mechanics over abstract mood words: identify what the viewer must literally see.

## Workflow

1. Extract the emotional mechanics.
   - Identify the subject, the pressure source, the forced action, and the contradiction.
   - Translate idioms into visible objects, body positions, and scene dynamics.
2. Build the first prompt from visible signals.
   - Specify subject, setting, props, action, expression, and emotional duality.
   - Add style only after the scene is concrete.
3. Refine with preserve-style edits.
   - Start each edit prompt by naming what must remain unchanged.
   - State one key correction in plain language.
   - Add hard visual constraints that the model cannot plausibly miss.
   - Add negative constraints for the common failure mode you just saw.
4. Diagnose failures visually.
   - Replace vague feedback like "not the right feeling" with concrete mismatches like "the duck is still standing" or "the rope is blending into the speech letters."

## Prompt Rules

- Prefer "the viewer must immediately understand X" over "make it feel more X."
- Specify body mechanics when tension matters: stretched neck, dangling legs, feet off ground, shadow gap, taut rope.
- Separate physical objects from symbolic effects. If both a rope and floating letters matter, state that they must be visually distinct.
- Use preserve-style edit prompts once the image is close. Do not rewrite the whole scene unless the generation is fundamentally wrong.
- Change one core visual signal per edit pass unless the current image is far from the intended metaphor.
- Name failure-prevention constraints explicitly: "no human figure," "do not replace the rope with glowing lines," "do not let the feet touch the stage."
- Preserve emotional duality. Many strong metaphor images need two tones at once, such as painful and funny, pressured and brave, awkward and sincere.

## Edit Strategy

When a user says "this is close, but not yet," do this:

1. Keep a short list of preserved elements at the front of the prompt.
2. Describe the single incorrect visual fact.
3. Convert that fact into measurable geometry or material detail.
4. Add one or two "must not" lines based on the last failure.
5. Keep the same emotional tone so the fix does not flatten the image.

## References

- Read `references/prompt-patterns.md` for reusable first-pass and edit-pass templates, common failure patterns, and the worked German-practice duck example.
