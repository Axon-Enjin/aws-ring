# RFC: Drop face landmarks before storage

**Project:** SignSync
**Date:** 2026-10-12
**Version:** 0.1
**Owner:** Xander
**Status:** Draft
**Last reconciled:** N/A
**PRD:** PRD-F5 in [prd-signsync.md](prd-signsync.md)

---

## 1. Context & Objective

The track and the product both forbid facial recognition and plate reading. A holistic landmark extractor emits a face set unless we discard it. Once a face set is written, deleting it later is not the same as never having stored it.

**Objective:** The only landmark payload that reaches disk, logs, or the sentence call is hands and body (PRD-F5). This covers US-4.

---

## 2. Proposed Solution

Extract landmarks in memory. Delete the face set before the first write and before the classifier and sentence calls. Persist hands and body only. Do not persist the source frame in the demo path unless a separate, explicit clip bucket is added later. That bucket is [FILL] and is off by default.

The card may show a hands-only skeleton drawn from the kept points (PRD-F2). It must not draw a face.

---

## 3. Technical Details & Contracts

Request: in-memory landmark object with face, hands, and pose.

Response: a stored sequence whose schema has no face key. A test fixture asserts the key is absent.

Classifier input and sentence input use that same reduced object (PRD-F3, PRD-F4).

If the extractor cannot separate the face set, the job fails closed: no write, card shows "no video" rather than a full dump.

Library name and version: [FILL].

---

## 4. Alternatives Considered

| Option | Why it lost |
|--------|-------------|
| Store the full set and ignore the face in the UI | The data still exists. This fails the irreversible choice. |
| Blur a stored frame and keep face landmarks | Still a face measurement. Out of scope. |
| Skip holistic extraction and use a hands-only model | Viable later if the hands-only model is enough. Not required to decide the drop. |

---

## 5. AI / Agent Implementation Notes

The implementing agent must not add a face embedding, a recognition call, or a plate reader while building PRD-F3. Tests for US-4 belong in the QAD. Effort: UNCALIBRATED.

---

## 6. Security, Privacy & Performance

Privacy: this is the bar for biometric-adjacent data. Performance cost of dropping fields is negligible next to extraction. The unmeasured cost is extraction itself: [FILL].

---

## 7. Execution Plan

1. Confirm the extractor can omit the face set. If it cannot, stop that path (kill criterion K-2).
2. Write the reduced object only.
3. Add the fixture that fails if a face key appears.

Rollback: if a build writes face keys, stop ingest. Command: [FILL].

---

## Self-Check

- [x] The choice is irreversible
- [x] The rejected option is the one that stores faces anyway
- [x] PRD-F5 and US-4 are named
