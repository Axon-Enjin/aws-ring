# Ring

Track repo for the Amazon Developer Hackathon. This folder is the whole project: rules, sponsor context, the research prompt, the research report, and `oss/` (a standalone library for the Open Source mini-challenge). It does not depend on any other local folder.

- **Hackathon:** Build, Ship, Shape: Amazon Developer Hackathon
- **Deadline:** 23 Oct 2026, 12:00 PM PT
- **Track:** A new or extended app on Ring APIs, SDKs, simulators, or devices. Sponsor themes include access control, business systems, home automation, accessibility, and caretaking. Facial recognition and license-plate reading are out.

## Recommended build

**SignSync** — doorbell video is reduced to hand and body landmarks, and the sign is sent to the resident as text. Faces are dropped. Rubric total 37, ahead of AuraDoor (34) and HapticHome (30).

The report's own formula is about $460k a year (1% of an estimated Ring-reachable base at $7.99). The executive summary also says $45M, which does not match that formula. Switch to AuraDoor if the RTSP stream is too unstable for frame analysis, or if translation takes more than 3 seconds.

## Docs

| File | What it is |
|---|---|
| [HACKATHON.md](HACKATHON.md) | Full hackathon rules and dates, copied so this repo stands alone |
| [ORG.md](ORG.md) | Amazon, AWS, and device-team goals, copied so this repo stands alone |
| [PROMPT.md](PROMPT.md) | Deep-research prompt for this track |
| [SignSync-AI-Deep-Research-Report.md](SignSync-AI-Deep-Research-Report.md) | Research report and the three pitches |
| [oss/](oss/) | Standalone Ring webhook receiver and hand-landmark helper (MIT) |
