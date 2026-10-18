<!-- MATERIALIZED from docs/dsd-signsync.md by scripts/materialize.py on 2026-10-12. Do not hand-edit; edit the canonical doc and re-run. -->

# Design:

> Visual language, materialized from DSD §2-§8.

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
