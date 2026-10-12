---
trigger: always_on
---

# FMD: see AGENTS.md

This project uses FMD via a **zero-footprint pointer** at `AGENTS.md` in the repo root. Read `AGENTS.md` first; it pins FMD v3.0.1.

Do not duplicate FMD rules in this file. If the workflow changes, update the pointer in this repo. Installer scripts (`init.ps1` on Windows, `init.sh` on Linux/macOS) stay in FMD v3.0.1.
