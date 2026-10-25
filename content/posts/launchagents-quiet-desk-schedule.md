---
title: "LaunchAgents and the quiet desk schedule — keeping Ollama, overnight video, and Freqtrade in their lanes"
date: 2026-10-25T17:49:00+05:30
draft: false
tags: ["local-ai","affiliate","apple-silicon"]
---

# LaunchAgents and the quiet desk schedule — keeping Ollama, overnight video, and Freqtrade in their lanes

**Series:** local-AI affiliate desk series (article 14)

> **Disclosure:** This article contains affiliate links to tools I use or recommend. Purchases through them may earn a commission at no extra cost to you.

A 16 GB Apple silicon (/go/apple-silicon) writing desk can host local prose, static builds, short voice, and overnight video — but only if day and night stay in separate lanes. Without an explicit schedule, Ollama (/go/ollama) drafting, Hugo (/go/hugo) rebuilds, mlx-audio (/go/mlx-audio) clips, and heavy renders compete for the same unified memory. This fourteenth post documents the LaunchAgent and leave-alone pattern that keeps that desk quiet during writing hours.

## Why a writing desk needs an explicit schedule

Day work is low-latency prose: briefs, outlines, drafts, claims worksheets, and dry Hugo builds. Those jobs want a responsive local model and a machine that is not swapping under a render. Night work is throughput: LTX-style video jobs that unload the chat model, saturate Metal, and write large files. [CITE: day vs night RAM notes on 16 GB Mac mini schedule]

Running both at once is the usual failure mode. Fans rise, token latency spikes, and the writer context-switches to “why is the desk hot?” The fix is temporal separation, not a bigger cloud bill. Cloudflare Pages (/go/cloudflare-pages) may host the eventual static site, but daytime bots still do not publish — dry rebuilds only until a human clears deploy.

## LaunchAgents that belong on the desk

Four user LaunchAgents cover the quiet-desk loop on this machine. Names below match the live labels; treat them as a pattern, not a store catalogue. [CITE: ~/Library/LaunchAgents com.abhishek.* labels]

**Keepalive.** A KeepAlive agent restarts the remote-agent bridge if it exits, so unattended daytime sessions can continue without a manual relaunch.

**Display-awake.** A second agent runs a small caffeinate-style helper so the panel does not sleep mid-draft when the box is otherwise idle. Writing hours need a reachable UI more than they need aggressive power saving.

**Overnight-video calendar.** A StartCalendarInterval agent fires at **01:00 Asia/Kolkata**, not an arbitrary UTC hour. It runs the overnight video wrapper, which promotes `.job.ready` files only inside the **01:00–06:30 IST** window. [CITE: com.abhishek.overnight-video StartCalendarInterval Hour 1; ai-window 01:00–06:30 Asia/Kolkata]

**DNS pin.** A short-interval agent re-pins public DNS (for example 1.1.1.1 / 8.8.8.8) and keeps Tailscale `accept-dns=false`, so MagicDNS does not silently override resolvers while the mesh stays up. [CITE: tailscale-dns-pin LaunchAgent every 5 minutes]

These agents are boring on purpose. They start, log, and stop. They do not invent affiliate slugs, open payment flows, or deploy Pages.

## What stays untouched

**Tailscale.** Keep the mesh running for remote access and optional Ollama serve on the tailnet. Daytime content work does not logout, uninstall, or rewrite Network Extension state. [CITE: Tailscale KEEP directive]

**Freqtrade dry_run.** Paper trading stays up 24/7. Content and video scripts unload Ollama for night RAM; they do not `trade-kill` or flip live. [CITE: leave Freqtrade dry_run=true running]

**Payments and Cloudflare publish.** No store checkout from the bot. No `wrangler pages publish` (or equivalent) from a daytime wake. Hugo `--minify` may write `site/public` locally; humans own the first public ship, disclosure page, and `/go/` allow-list review against `links.csv`.

## Daytime agent rules

Outside the night window, agents invent or continue **content**: blog articles, ebook chapters, claims, short voice scripts, dry Hugo wiring. They may **inspect** the LTX queue (ready / running / done / failed) and read sanitize notes. They must **not** start overnight renders, promote jobs into the live runner, or treat a closed `ai-window` as an invitation to “just test one clip.”

Leave-alone extends to noise: do not chase Freqtrade log lines or Tailscale heal chatter unless the wake’s brief says so. Attention stays on the writing kit — askai write → ≤0.9× cut → extract-claims → voice ≤120 words — and on local site wiring.

## Hand-off note before 01:00–06:30 IST

Before the calendar agent wakes, leave a short night hand-off in notes:

1. Confirm **two** `.job.ready` files under the render queue (for example small-complex and bigger-complex templates already sanitized). [CITE: queue/render overnight-*.job.ready]
2. State that daytime did **inspect-only** — no LTX start.
3. Remind: unload chat models inside the night wrapper; leave Tailscale and Freqtrade alone.
4. Remind: still no Cloudflare publish from the overnight path.

When `ai-window` reports the window closed, the correct daytime verb is **prepare**, not **render**. The LaunchAgent owns the clock; the hand-off owns the checklist.

That is the quiet-desk contract: schedule in LaunchAgents, prose by day, video by night, mesh and paper trading untouched, publish still a human gate.
