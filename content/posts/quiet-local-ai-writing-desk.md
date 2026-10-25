---
title: "Quiet local AI writing desk on Apple silicon"
date: 2026-10-25T23:15:20+05:30
draft: false
slug: "quiet-local-ai-writing-desk"
tags: ["local-ai", "apple-silicon", "ollama", "16gb"]
description: "How a 16 GB Mac mini runs a quiet local writing desk: one model at a time, Ollama + Hugo, human rewrite gates, and disclosed /go/ affiliate links."
---

> **Affiliate disclosure:** Some links are affiliate links. As an Amazon Associate I earn from qualifying purchases. See [Disclosure](/disclosure/).

If two models load on a 16 GB Mac mini, the desk stops being quiet. Fans climb, swap starts, and the draft you wanted in two minutes takes twenty. The useful setup is boring on purpose: one local model for prose, a static Hugo publish path, and a human gate before anything public.

This is the operator overview. For the reusable folder map see [from desk to pack](/posts/from-desk-to-pack-writing-kit/); for day-of checks see the [16 GB checklist](/posts/quiet-desk-checklist-16gb/).

## The real constraint: unified memory, not “AI power”

Apple silicon shares one memory pool between OS, browser, Ollama, and anything else you left open. On 16 GB, plan for roughly 10–12 GB usable for model weights once macOS and a light editor are up. That is why daily writing here sticks to quantised 4B–9B models (`qwen3.5:4b` / `qwen3.5:9b` via [Ollama](/go/ollama/)), not a second 14B “just in case”.

Symptoms you should trust more than marketing:

- Activity Monitor shows memory pressure yellow/red while tokens crawl
- `ollama ps` lists more than one heavy runner
- Hugo builds or overnight video started while a chat context is still loaded

When those appear, unload — do not add another UI. Detail on the second-model failure mode: [avoiding the second model fight](/posts/continue-dev-editor-loop/).

## One honest workflow

1. **Brief** — audience, search intent, and the one decision the post must help the reader make.
2. **Outline** — H2s as decisions, not topic soup.
3. **Local draft** — `~/AI/bin/askai` with `AI_PROFILE=write` against the outline only.
4. **Deslop** — audit then rewrite; target ≤ 90% length and slop score ≤ 3.
5. **Claims** — `extract-claims.sh`; no empty `[CITE:]` on ship day.
6. **Affiliate inject** — only `/go/<slug>/` rows that exist in `links.csv`.
7. **Hugo publish** — build when inference is idle; push static files.

The machine is a fast typist. You own facts, tone, and whether a link is honest.

## What stays in separate lanes

| Lane | Window (IST) | Rule |
|------|----------------|------|
| Prose / deslop / claims | Day + evening | One Ollama model; no LTX |
| Hugo rebuild | After draft idle | Do not stack on a hot runner |
| Overnight video (LTX) | 01:00–06:30 only | Never beside a write job |
| Freqtrade | Always `dry_run` here | Do not kill it to free RAM for blogging |

Schedule mechanics: [LaunchAgents and the quiet desk schedule](/posts/launchagents-quiet-desk-schedule/) and [overnight windows](/posts/overnight-windows-quiet-desks/).

## Tools that earn a slot on 16 GB

- **[Ollama](/go/ollama/)** — default runner; pull only what you will actually load this week.
- **[llama.cpp](/go/llama-cpp/)** — when you need explicit GGUF / quant control; see [quant choices on 16 GB](/posts/llama-cpp-quant-choices-16gb/).
- **[Hugo](/go/hugo/)** — static site; no database tax.
- **[GitHub Pages](/go/github-pages/)** — host the build; affiliate redirects live in `_redirects` + `/go/` stubs.
- **[mlx-audio](/go/mlx-audio/)** — short daytime voiceovers only; never stacked on overnight renders.

Open WebUI is optional. Add it only when a browser UI is worth the RAM — [when to add a local UI](/posts/open-webui-llama-cpp-beside-ollama/).

## Affiliate links without embarrassing yourself

Readers buy when the post taught them something and the link matches the advice. Rules that keep this desk shippable:

- Disclose once at the top; repeat briefly near a product box if needed
- Never invent `/go/` slugs — [allow-list hygiene](/posts/affiliate-allow-list-hygiene/)
- Amazon.in tag `abhishekrhl-21` where approved; UK stays placeholder until Associates approval
- No fake reviews; no sockpuppet threads; promote by answering real questions with disclosure

## Start here, then go deeper

1. Assemble the pack — [from desk to pack](/posts/from-desk-to-pack-writing-kit/)
2. Walk the checklist — [quiet-desk checklist](/posts/quiet-desk-checklist-16gb/)
3. Learn what never to do — [anti-patterns](/posts/anti-patterns-quiet-desk/)
4. Build the stack deliberately — [building a quiet local AI desk](/posts/building-quiet-local-ai-desk-stack/)

Quiet is a schedule, not a brand word. Keep one model loaded, publish when the fans are calm, and let the content earn the click.

---

## Desk gear that actually helps a 16 GB Mac mini (affiliate)

If model files and drafts are fighting the internal SSD, external NVMe via a Mac mini dock is the practical upgrade — not a bigger cloud bill.

- [UGREEN Mac mini dock with NVMe slot](/go/ugreen-mac-mini-dock/) (affiliate) — ports + model-library drive in one stand.
- [Satechi Mac mini hub & stand](/go/satechi-mac-mini-hub/) (affiliate) — design-matched alternative.
- [Samsung T7 Shield portable SSD](/go/samsung-t7-shield/) (affiliate) — fast offload for GGUF libraries when a full dock is overkill.
- UK readers: [UGREEN on Amazon.co.uk](/go/ugreen-mac-mini-dock-uk/) (placeholder — Associates tag lands after UK approval).

Disclosure: as an Amazon Associate I earn from qualifying purchases. See [/disclosure/](/disclosure/).


---

**Buying hardware?** See the flagship guide: [Best Mac mini for local LLMs](/posts/best-mac-mini-for-local-llms/) (RAM × model matrix + disclosed price CTAs).
