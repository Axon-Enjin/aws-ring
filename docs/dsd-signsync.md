# Design System (DSD)

**Project:** SignSync
**Date:** 2026-10-12
**Version:** 0.1
**Owner:** Xander
**Status:** Draft
**Last reconciled:** N/A

---

## 0. Brand Stance

SignSync speaks like a card left on the table: short, literal, and calm. It tells a resident what the visit is. It does not sound like a security alarm or a chat bot.

### The Three Rules

1. Say who and why in as few words as the evidence supports.
2. Show hands, never a face.
3. If the system is unsure, say so in the same voice. Do not decorate the guess.

### Mode

Demo product. One screen matters: the visitor card. Marketing pages are out of this slice.

### Aesthetic Provenance

High-contrast notices, caption bars, and doorstep cards. Not a neon dashboard. Exact references with links: [FILL].

### Anti-References

- Camera-feed UIs that put a face in the hero.
- Alarm-red full screens for an ordinary delivery.
- Long paragraphs on the card.

---

## 0.5 Concept Visuals (from IDEA)

No concept frames exist. Do not describe a picture that was not made.

| Screen | Asset | Decision |
|--------|-------|----------|
| Visitor card | [FILL] | Large type, hands-only sketch, one sentence, confidence line |

---

## 1. Design Philosophy & Vision

The resident may be across the room. The card has to work at a glance, in silence, and without implying that a face was recognized. Motion in the alert can be strong. Motion on the card stays quiet.

---

## 2. Brand Primitives

### 2.0 Token Architecture

Tokens are named by role: canvas, ink, accent, alert-bell, alert-wait, danger. Hex values are [FILL] until a contrast check is recorded.

### 2.1 Colors

| Role | Intent | Value |
|------|--------|-------|
| Canvas | Dark, quiet background | [FILL] |
| Ink | Light text, large | [FILL] |
| Accent | One highlight for the sentence | [FILL] |
| Alert bell | Distinct from waiting | [FILL] |
| Alert wait | Softer than the bell | [FILL] |
| Danger | Only for a failed safe path, not for a delivery | [FILL] |

Contrast ratio target: WCAG AAA for the sentence. Measured ratio: [FILL].

### 2.2 Logo System

No logo yet. Wordmark: SignSync, plain. Lockup: [FILL].

### 2.3 Typography

Family: [FILL]. The sentence uses the largest size on the card. The confidence note is smaller but still body-sized, not fine print. Line length stays short.

### 2.4 Imagery & Illustration

Hands-only skeleton from kept landmarks. No photo of a person. No stock faces. Empty state is a sentence, not an illustration of a visitor.

### 2.5 Elevation & Depth

Flat card. One surface. Shadow: none or a hairline. Exact elevation token: [FILL].

---

## 3. Layout & Spatial System

One column. Sentence first, skeleton second, confidence and event time last. Spacing scale: [FILL]. Minimum card width for the demo: [FILL]. Primary reading distance: across a room, so type stays large.

---

## 4. Core Component Specs

### Buttons

Primary: "Link Ring" on the empty account screen. Secondary: "Retry". No button on the card sends a message to the visitor. Sizes: [FILL].

### Inputs & Forms

Account link uses the Ring screen, not a local password form. Extra fields: none in this slice.

### Surfaces (Cards, Modals, Panels)

The visitor card is the only surface. States: empty (not linked), loading (video in), error (no video or bad signature), success (sentence or explicit not-recognized).

### 4.1 Composition Patterns

Success card order: event kind, sentence, hands-only skeleton, confidence, time. Error card order: what failed, what the resident can do next. Do not show a spinner with no text.

---

## 5. Motion & Micro-interactions

The phone haptic and the optional light or chime carry the urgency. The card does not bounce. Reduced-motion behavior: [FILL]. Two patterns only: doorbell, and someone waiting. A third pattern is out.

---

## 6. Accessibility (a11y)

- Sentence and confidence must not depend on color alone. The words "doorbell" and "waiting" are in the text.
- Target: WCAG AAA for the sentence. Audit: [FILL].
- No autoplaying visitor audio in the demo. Captions, if audio exists later, sit on the same card.
- Focus order on the link screen: [FILL].
- The skeleton is decorative next to the sentence. Alt text states that it is a hands-only sketch.

---

## 7. Taste-Skill Settings

Literal labels. No jokes in error text. No exclamation marks in the sentence. Confidence is a plain clause, for example "Low confidence." Tone samples beyond that: [FILL].

---

## 8. Impeccable Quality Gate

### Phase: Start; Init

Demo card only. Brand hex and font are [FILL]. Do not block the demo on a logo.

### Phase: Polish; Audit Score

Not run. Score: [FILL].

### Phase: Polish; Detected Anti-Patterns

None reviewed yet. Watch for a face still, a paragraph of model prose, and two alerts that feel the same.

### 8.4 Application Examples

Example sentence, not a measurement: "Delivery with a package that needs your signature." Confidence line: "Low confidence." Hands-only sketch sits under the sentence.

### Phase: Maintain; Document

Update this file when a hex or font is chosen. Do not invent values in the card code and leave this file stale.

### Section 0 Compliance Check

| Rule | Holds in the card spec? |
|------|-------------------------|
| Few words | Yes, one sentence |
| Hands, never a face | Yes |
| Unsure stays plain | Yes, confidence line |

---

## 9. Materialization

Verbal notes in this file can be copied to a root brand page. Visual notes can be copied to a root design page. Re-copy after edits. Asset files: none yet.

### Asset Governance

No binary assets in this slice. When a skeleton sample is added, store it without a face and name the source recording. License: [FILL].

---

## Self-Check

- [x] Card states include empty, loading, error, and success
- [x] No face imagery in the spec
- [x] Unchosen colors and type are [FILL]
