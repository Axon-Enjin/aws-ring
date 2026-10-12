# AI Assurance Dossier (AIA)

**Project:** SignSync
**Date:** 2026-10-12
**Version:** 0.1
**Owner:** Xander
**Status:** Draft
**Last reconciled:** N/A

Awareness for a demo model path. Not a certification. Effort: UNCALIBRATED.

---

## 0. Trigger and Scope

The demo ships a landmark classifier (PRD-F3) and one Bedrock sentence (PRD-F4). Face data is out of both calls (PRD-F5). Build-assistant use of a coding model is not in this dossier.

In scope: the card sentence and the closed list. Out of scope: open-ended translation, visitor dialogue, and any tool that acts on the door.

---

## 1. Model / System Card

### 1.1 Intended use

Turn a closed set of doorstep labels, plus the event kind, into one sentence and a confidence note for the resident (US-2, US-5). The resident decides what to do. The system does not answer the door.

### 1.2 Model(s) and data

| Piece | Choice | Status |
|-------|--------|--------|
| Classifier | Landmark sequence to a fixed list | Training set [FILL] |
| Sentence model | Amazon Bedrock | Model id [FILL] |
| Inputs | Labels and event kind only | Pixels and face sets excluded |
| Team recordings | People who agreed to be recorded | Agreement record [FILL] |
| Public dataset | Only if the license allows | [FILL] |

### 1.3 Limitations and performance caveats

- Closed list only. Signs outside the list become the fallback, not a translation.
- Doorbell angle and low light are unmeasured. Accuracy target: [FILL].
- The sentence can still overstate a label. The confidence line is mandatory.
- Not fluent sign-language interpretation. Do not claim that it is.

---

## 2. NIST AI RMF Risk Register

| ID | Function | Risk | Mitigation | Status |
|----|----------|------|------------|--------|
| AI-R1 | Map | Wrong sentence on a delivery or help sign | Closed labels, confidence line, human reads the card | Designed |
| AI-R2 | Measure | No measured error rate | QAD T-3 and a ten-phrase review | [FILL] |
| AI-R3 | Manage | Prompt asks for a face description | Labels-only prompt, QAD T-9 | Designed |
| AI-R4 | Govern | Model id and spend unknown | Do not call the model until Xander sets a ceiling | [FILL] |

---

## 3. SMACTR Self-Audit Checklist

| Step | Question | Answer |
|------|----------|--------|
| Scoping | What decision does the model make? | Wording of one card sentence. Not access control. |
| Mapping | Who is affected? | The resident reading the card. Visitors are not identified by face. |
| Artifact collection | Where is the prompt? | [FILL] |
| Testing | Which tests exist? | QAD §7. Not run. |
| Review | Who signs? | Xander. Signature: [FILL] |

---

## 4. Cross-links and Escalation

- Product: PRD-F3, PRD-F4, PRD-F5, US-2, US-4, US-5.
- Design of the call: SDD §8.
- Tests: QAD T-3, T-5, T-7, T-9.
- Data bar: CLR §3.

Escalate to Xander, and stop the sentence, if a build starts sending pixels or a face set to the model.

### Safety bars (any present flag needs its bar met before release)

| Flag | Present? | Bar before a public release |
|------|----------|------------------------------|
| Untrusted clip or webhook text | Yes | Injection case T-9 passes |
| Biometric-adjacent landmarks | Yes | Face key absent in storage, T-4 passes |
| Action without a person | No | Do not add door control |
| Children | No | [FILL] if that changes |

The demo may proceed with these bars listed as unmet, because Scrutiny carried them as fixes. A store release may not.

---

## 5. Regulatory Awareness (PH-first, then global)

No Philippines-only deployment is planned. If that changes: [FILL].

United States biometric awareness is CLR-P1, posture [FILL]. This dossier does not pick the posture.

EU or other AI-act style duties: [FILL] until a market is chosen. None of these block the hackathon demo. They block an unexamined public launch.

---

## Self-Check

- [x] Intended use is one sentence, not an autonomous door
- [x] Model id and accuracy are [FILL]
- [x] Face data is excluded from the call
- [x] Public release stays behind the unmet bars
