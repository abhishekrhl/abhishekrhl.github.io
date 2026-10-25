---
title: "From desk to pack: assembling a reusable local AI writing kit"
date: 2026-10-25T23:15:20+05:30
draft: false
slug: "from-desk-to-pack-writing-kit"
tags: ["local-ai", "kit", "workflow", "ollama"]
description: "Turn a 16 GB Mac mini writing desk into a reusable kit: folder layout, askai prompts, deslop gates, claims QA, and /go/ affiliate stubs — without shipping AI slop."
---

> **Affiliate disclosure:** Some links are affiliate links. As an Amazon Associate I earn from qualifying purchases. See [Disclosure](/disclosure/).

Most “local AI writing setups” die as a pile of one-off Markdown files. A kit is different: the same folder map, the same prompts, and the same quality gates every time you start a post. On a 16 GB Apple silicon Mac mini that is the difference between a quiet desk and a second-model fight.

This post is the pack map I actually use under `~/AI/` and the published Hugo tree. It pairs with the [quiet desk overview](/posts/quiet-local-ai-writing-desk/) and the [16 GB checklist](/posts/quiet-desk-checklist-16gb/).

## What the kit must do

A reusable kit answers five questions before any model runs:

1. Where does research live, and what is allowed to become a claim?
2. Which local model writes, and which only extracts or audits?
3. How do we reject AI filler before Hugo sees the draft?
4. Which `/go/<slug>/` paths are real rows in `links.csv`?
5. Who signs off — human gate, or auto-publish only above a score threshold?

If any answer is fuzzy, stop. Shipping volume without those rails is how you get 50 thin posts and zero trust.

## Folder layout that survives overnight jobs

Keep prose work off the LTX and Freqtrade lanes. A layout that has held up:

```text
~/AI/
  prompts/          # deslop-audit, deslop-rewrite, niche-research, …
  bin/askai         # stdin → Ollama (tiered models)
  notes/            # rubrics, swap maps, ops logs
  tmp/deslop-YYYY-MM-DD/
~/Downloads/AI-outputs/
  local-ai-blog-affiliate/   # briefs, drafts, claims worksheets
  qa/                        # extract-claims.sh output
~/AI/tmp/publish/abhishekrhl.github.io/
  content/posts/             # Hugo markdown that ships
  content/go/                # /go/ stubs
  links.csv                  # allow-list only
  static/_redirects          # generated from links.csv
```

Rule: drafts never overwrite outlines. Copy forward (`brief → outline → draft → claims → publish`), and keep a dated backup under `~/AI/notes/backups-YYYY-MM-DD/` before a destructive rewrite.

## Prompt pack (minimum viable)

Ship these four beside `~/AI/bin/askai`:

| Prompt | Profile | Job |
|--------|---------|-----|
| `niche-research.md` | extract | Demand + gaps; mark unknowns as “no data” |
| `deslop-audit.md` | extract | Score 0–10 slop; quote phrases to cut |
| `deslop-rewrite.md` | write | Delete-first rewrite ≤ 90% length |
| `delete-first-shorten.md` | write | Hit ≤ 0.9×N when rewrite lands hot |

Add hook / flow / specificity / CTA honesty prompts once the [quality rubric](https://abhishekrhl.github.io/) gates settle — the local copy lives at `~/AI/notes/deslop-quality-rubric-2026-10-25.md` on the desk.

Balanced tier on this machine: chat and extract on `qwen3.5:9b`; reserve heavier write models for nights when unified memory is free and Freqtrade `dry_run` is left alone.

## Quality gates before publish

Do not “hope” the draft is fine. Score it:

1. **Hook** — first 2 sentences name the reader’s constraint (RAM, noise, privacy) and a concrete outcome.
2. **Flow** — each H2 advances one decision; no restating the 16 GB lecture three times.
3. **Specificity** — real paths, model tags, IST windows, or measured limits; no “studies show”.
4. **CTA honesty** — only `/go/` slugs that exist in `links.csv`; placeholders OK until Associates UK lands; never invent ASINs.
5. **Claims** — run `extract-claims.sh`; empty `[CITE:]` blocks human review.

Auto-publish only if slop score ≤ 3 and all five gates pass. Otherwise the draft stays in `AI-outputs/` until a human gate.

## Affiliate inject without breaking trust

Affiliate links are a closed set. The pack includes:

- `links.csv` rows → `scripts/generate-go-redirects.py` → `static/_redirects` + `content/go/*.md`
- In-body links only as `/go/<slug>/` (trailing slash)
- One disclosure block at the top; a short gear box at the end is enough
- Amazon.in tag `abhishekrhl-21` where approved; UK URLs stay untagged placeholders

See [affiliate allow-list hygiene](/posts/affiliate-allow-list-hygiene/) for why invented slugs fail QA.

## What this kit deliberately excludes

- Fake reviews or sockpuppet promotion
- Amazon Special Links inside ebook PDFs
- Overnight video (LTX) overlapping prose hours — keep that to 01:00–06:30 IST
- Stopping Freqtrade `dry_run` to free RAM for a write job

## Next steps in the series

Once the pack is assembled, schedule it: [LaunchAgents and the quiet desk schedule](/posts/launchagents-quiet-desk-schedule/), [overnight windows](/posts/overnight-windows-quiet-desks/), and [anti-patterns](/posts/anti-patterns-quiet-desk/). The goal is a sustainable cadence of posts readers finish — not a raw 50/day firehose.

---

## Desk gear that actually helps a 16 GB Mac mini (affiliate)

If model files and drafts are fighting the internal SSD, external NVMe via a Mac mini dock is the practical upgrade — not a bigger cloud bill.

- [UGREEN Mac mini dock with NVMe slot](/go/ugreen-mac-mini-dock/) (affiliate) — ports + model-library drive in one stand.
- [Satechi Mac mini hub & stand](/go/satechi-mac-mini-hub/) (affiliate) — design-matched alternative.
- [Samsung T7 Shield portable SSD](/go/samsung-t7-shield/) (affiliate) — fast offload for GGUF libraries when a full dock is overkill.
- UK readers: [UGREEN on Amazon.co.uk](/go/ugreen-mac-mini-dock-uk/) (placeholder — Associates tag lands after UK approval).

Disclosure: as an Amazon Associate I earn from qualifying purchases. See [/disclosure/](/disclosure/).
