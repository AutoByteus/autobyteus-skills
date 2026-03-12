# Deck archetype routing (article-first deck selection)

Use this after reading the raw article content.
The goal is to infer one **deck archetype** before choosing style pack, layout mix, and scene bias.

## Why this exists

Users think in article intent, audience, and feel.
They usually do not think in `pack-id`, `L5`, or `text budget`.

So the skill should first answer:
- What kind of deck is this?
- What kind of viewing experience fits this content?

## Core deck archetypes

### 1. Narrative cinematic

- Best for:
  - story-driven sermons
  - testimony arcs
  - character-led teaching
  - emotionally charged reflective essays
- Signals:
  - clear protagonist or journey
  - strong tension / release
  - vivid scenes or moments
  - short quotable lines that can carry a slide
- Default style direction:
  - `cinematic-light`
  - `cinematic-dark`
  - `cinematic-editorial`
- Default routing bias:
  - `cinematic`

### 2. Editorial teaching

- Best for:
  - explainers
  - sermons with teaching/application rhythm
  - reflective but readable article-to-deck conversions
- Signals:
  - clear thesis plus several teaching points
  - moderate density
  - wants beauty without sacrificing readability
- Default style direction:
  - `editorial-light`
  - `warm-sermon`
  - `airy-relaxed`
- Default routing bias:
  - `balanced`

### 3. Structured briefing

- Best for:
  - internal briefings
  - training decks
  - product or strategy overviews
  - practical action-oriented summaries
- Signals:
  - list-heavy structure
  - frameworks, steps, or recommendations
  - clarity matters more than atmosphere
- Default style direction:
  - `clean-corporate`
  - `editorial-light`
  - `neo-tech` when topic is product/AI
- Default routing bias:
  - `structured`

### 4. Evidence explainer

- Best for:
  - research summaries
  - policy explainers
  - analytical essays
  - evidence-heavy argument flow
- Signals:
  - citations, evidence anchors, objections, method, comparison
  - higher text density
  - trust and traceability matter
- Default style direction:
  - `research-academic`
  - `clean-corporate`
  - `editorial-light`
- Default routing bias:
  - `dense`

### 5. Warm devotional

- Best for:
  - pastoral sharing
  - prayer/devotional content
  - comfort, encouragement, healing, application
- Signals:
  - intimate tone
  - scripture + reflection + application
  - gentle emotional rhythm
- Default style direction:
  - `warm-sermon`
  - `editorial-light`
  - `airy-relaxed`
- Default routing bias:
  - `balanced`

### 6. Animated story

- Best for:
  - youth or family audiences
  - simplified character-led retellings
  - more playful, expressive communication
- Signals:
  - audience is children, youth, or mixed family
  - character-led scenes matter
  - wants optimistic, friendly energy
- Default style direction:
  - `animated-feature-bright`
  - `youth-social`
- Default routing bias:
  - `cinematic`

## Selection rules

1. Choose the archetype from the article's dominant behavior, not just isolated phrases.
2. If two archetypes fit, pick the one that best matches the intended audience.
3. If the user explicitly requests a mood or style, that can override the default style pack, but the archetype should still guide slide breakdown and layout mix.
4. If the article is mixed, prefer:
   - `editorial teaching` for balanced explainers
   - `narrative cinematic` for scene-led journeys
   - `evidence explainer` for analysis-heavy content

## What the archetype controls

Once chosen, the archetype should influence:
- style pack selection
- deck-level routing bias
- likely slide roles
- acceptable text density
- scene emphasis
- how often full-bleed cinematic slides should appear

## Recommended planning output

Record the chosen archetype near the top of `slides_plan.md` so later prompt-writing stays consistent.
