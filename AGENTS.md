# FMD pointer

This project uses **Foundational Matrix Documents (FMD)** via a zero-footprint pointer. Do not duplicate FMD rules here. Follow the pinned engine.

**Pinned engine:** FMD v3.0.1

## How to operate FMD in this repo

1. **Session start:** Follow FMD v3.0.1 for routing, trigger phrases, file naming, and workflow. This pointer defers to it entirely.

2. **Routing surface:** Use the FMD v3.0.1 trigger matrix when you need to map a request to an artifact. It holds the signal register and every artifact's trigger and non-trigger conditions.

3. **Templates on demand:** When a trigger fires, use the matching FMD v3.0.1 template `<NAME>_Template.md`. Example: `PRD_Template.md` for a PRD request. Read the `> **Agent Instructions**` blockquote first.

4. **Guides on demand:** Detailed reference (orchestrator, milestones, context, knowledge, agents, frameworks, business development, engineering ladder, public surfaces, workflows) is part of FMD v3.0.1. Read only the guide the current task needs. Do not preload the folder.

5. **Offline fallback:** FMD v3.0.1 is not copied into this repo. Engine-relative paths, when you already have the engine, are `AGENTS.md`, `templates/_triggers.md`, `templates/<NAME>_Template.md`, and `guides/<NAME>.md`.

6. **Validation:** After generating docs, run FMD v3.0.1 `check.py` against `docs/`. Add `--strict` for CI-grade checks.

7. **Cockpit (visual progress):** Regenerate only on cockpit trigger or explicit request with FMD v3.0.1 `cockpit.py`. This writes `cockpit.html` at the project root (listed in `.gitignore`; it is a generated artifact).

8. **Generated output:** Save filled artifacts to `docs/{{type}}-{{slug}}.md` per FMD v3.0.1. Keep the operating position in `docs/state.md` by hand. After each artifact write or gate run, FMD v3.0.1 `record.py` regenerates `docs/index.md` (stamped "Built on FMD v3.0.1") and appends to `docs/log-{{slug}}.md`.

## Reference-only (never auto-load into build context)

`examples/`, `Playbook.md`, `CHANGELOG.md`, and `benchmarks/` stay inside FMD v3.0.1.
