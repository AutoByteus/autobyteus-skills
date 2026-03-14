# Emotion Metaphor Prompt Patterns

## First-Pass Generation Template

Use this when the user gives a feeling, idiom, or social dynamic but there is no image yet.

```text
Create a [tone/style] illustration about the feeling of [emotion or situation].
Center [subject] in [setting].
Show the pressure source through visible scene mechanics: [rope / stage / wave / crowd / clock / weight / spotlight / hands-off force].
Include concrete props that reveal the repeated struggle: [marked-up pages / recordings / crossed-out drafts / calendar / timer / crumpled paper].
Show the subject's body language clearly: [open beak / tense shoulders / stretched neck / tired eyes / dangling legs / clenched hands].
Make the emotional mix visible at once: [embarrassed but brave / funny but painful / pressured but determined].
Use [style description].
Do not add [common unwanted elements].
```

## Edit-Pass Template

Use this when the image is already close and the goal is to preserve style while correcting one visible fact.

```text
Edit this illustration while preserving the same [composition, style, lighting, colors, props, and emotional tone].
The key correction: [single wrong visual fact].
[Describe the exact geometry or material reality that must be true.]
[Describe one extra visual cue that makes the correction unmistakable.]
Keep the subject still [doing the core action].
Do not add [specific failure mode from the previous image].
Do not replace [physical object] with [symbolic effect].
```

## Worked Example: German-Practice Duck

### Final V5 Prompt

This is the exact prompt that produced the final "feet off the stage" version:

```text
Edit this illustration while preserving the same composition, painterly storybook style, lighting, colors, microphone, recording phone, classroom stage, and emotional tone. The key correction: the duck must be clearly hanging in the air, suspended by the rope around its neck. Its feet must be visibly off the wooden stage with a clear gap underneath both feet. Do not let the feet touch the platform at all. The rope from the top must look taut and actively pulling upward. Stretch the duck's neck and body upward slightly, make the legs dangle downward, and show a small shadow on the stage below the feet to emphasize suspension. Keep the duck still struggling to pronounce German sounds into the microphone, with tired eyes, open beak, tension, embarrassment, and effort. Preserve the floating German pronunciation fragments around the beak. No human figure, no gore, no brutality, just a strong visual metaphor of being forced to speak German while literally hanging in the air.
```

### Why This Prompt Worked

- It preserved the style first, so the model stopped replacing the whole scene.
- It named one correction only: the duck must be hanging in the air.
- It translated "hanging" into measurable facts: feet off stage, clear gap, taut rope, dangling legs, stage shadow.
- It blocked the earlier failure modes: no human figure, no gore, no brutality.

## Worked Example: Burnout as a Candle in a Meeting

### First-Pass Prompt

```text
Create a cinematic editorial illustration about the feeling of quiet workplace burnout. Center a half-melted candle wearing office clothes at the conference table of a polished corporate meeting room. The candle is still upright and trying to smile, but wax is dripping down onto papers, a laptop, and a calendar full of meetings. Around the table, other coworkers appear polished and composed, while the candle is visibly trying to stay professional as it burns away. Show the contradiction clearly: outwardly functioning, inwardly consumed. Use dramatic movie-like lighting, realistic material detail, restrained color palette, and a serious but slightly surreal tone. No caption text, no fantasy monsters, no flames engulfing the whole room.
```

### Tightening Edit Prompt

```text
Edit this illustration while preserving the same corporate meeting room, cinematic lighting, realistic materials, and restrained emotional tone. The key correction: the candle must look like it is still trying to participate professionally while visibly melting from overwork. Add a small forced smile, a pen still in hand, and wax pooling directly onto a notebook with meeting notes. Keep the candle seated upright in the meeting, but make the burnout unmistakable through the wax loss and tired posture. Do not turn this into horror, and do not replace the subtle office realism with exaggerated fire effects.
```

### Why This Example Matters

- It shows contradiction-driven prompting: professional composure plus visible depletion.
- It uses ordinary office props to make the metaphor believable.
- It prevents the model from drifting into horror or fantasy.

## Worked Example: Social Anxiety as a Deer Under Spotlight

### First-Pass Prompt

```text
Create a detailed cinematic storybook illustration about social anxiety during a group introduction. Center a small deer on a school auditorium stage under an intense spotlight, frozen in front of a microphone. Beyond the light, the audience is mostly dark and indistinct, but the deer feels every eye on it. Show trembling legs, wide eyes, a tight chest, and a stack of cue cards slipping from its hooves. The stage should feel enormous and empty around the subject. Make the image feel exposed, awkward, and painfully self-aware, yet still sympathetic. Use warm spotlight against cool surrounding darkness, premium painterly detail, and no caption text.
```

### Tightening Edit Prompt

```text
Edit this illustration while preserving the same auditorium, spotlight, painterly cinematic style, and vulnerable tone. The key correction: make the deer look frozen rather than merely sad. Lock the knees, stiffen the shoulders, widen the eyes further, and show one cue card slipping mid-fall from its hoof. Keep the microphone directly in front of the deer and the dark audience beyond the spotlight. Do not add tears, and do not turn the audience into detailed faces; the fear should come from exposure, not from visible mockery.
```

### Why This Example Matters

- It shows how to prompt exposure and paralysis through posture and stage scale.
- It uses negative constraints to avoid melodrama and cartoon bullying.
- It keeps the metaphor emotionally sharp without making it literal or violent.

## Common Failure Patterns

### The model captures mood but misses mechanics

Replace emotional feedback with visible facts.

Bad:

```text
Make it feel more forced and pressured.
```

Better:

```text
The subject must be visibly suspended by the neck, with both feet off the floor and a taut rope from above.
```

### The model introduces a helper figure

Block the helper explicitly.

```text
Remove the human figure and all human hands completely. The upward force must come only from the rope from above.
```

### The symbolic effect replaces the object

Separate object and symbol.

```text
The rope must be a real brown rope, clearly separate from the white pronunciation letters.
```

## What To Learn From This

- Strong image prompting is often scene direction, not adjective stacking.
- The winning prompt usually arrives after diagnosing exactly what the model misunderstood.
- "Almost right" images benefit from edit prompts more than full rewrites.
- If the user speaks in idioms, convert the idiom into posture, force, props, and spatial relationships.
- A reusable skill needs worked examples from different emotions so the pattern is transferable, not tied to one subject.
