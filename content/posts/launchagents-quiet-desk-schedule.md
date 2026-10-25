---
title: "LaunchAgents and the quiet desk schedule — keeping Ollama, overnight video, and Freqtrade in their lanes"
date: 2026-10-25T23:15:20+05:30
draft: false
slug: "launchagents-quiet-desk-schedule"
tags: ["local-ai", "launchagents", "freqtrade"]
description: "Practical local-AI notes for a 16 GB Apple silicon Mac mini — affiliate links disclosed."
---

> **Affiliate disclosure:** Some links are affiliate links. As an Amazon Associate I earn from qualifying purchases. See [Disclosure](/disclosure/).

**Series:** local-AI affiliate desk series (article 14)

> **Disclosure:** This article contains affiliate links to tools I use or recommend. Purchases through them may earn a commission at no extra cost to you.

A 16 GB Apple silicon Mac mini hosts local prose, static builds, short voice, and overnight video — but only if day and night stay in separate lanes. Without an explicit schedule, Ollama drafting, Hugo rebuilds, mlx-audio clips, and heavy renders compete for the same unified memory. This fourteenth post documents the LaunchAgent pattern that keeps the desk quiet during writing hours.

## Why a writing desk needs an explicit schedule

Day work is low-latency prose: briefs, outlines, drafts, claims worksheets, and dry Hugo builds. Those jobs require a responsive local model and a machine that is not swapping under a render. Night work is throughput: overnight video jobs-style video jobs that unload the chat model, saturate Metal, and write large files.

Running both simultaneously causes fans to rise, token latency to spike, and the writer to context-switch over heat. The fix is temporal separation, not a bigger cloud bill. GitHub Pages may host the eventual static site, but daytime bots do not publish — dry rebuilds only until a human clears deploy.

## LaunchAgents that belong on the desk

Four user LaunchAgents cover the quiet-desk loop on this machine. Names below match the live labels; treat them as a pattern, not a store catalogue.

**Keepalive.** A KeepAlive agent restarts the remote-agent bridge if it exits, ensuring unattended daytime sessions continue without manual relaunch.

**Display-awake.** A second agent runs a helper to prevent the panel from sleeping mid-draft when the box is idle. Writing hours need a reachable UI more than aggressive power saving.

**Overnight-video calendar.** A StartCalendarInterval agent fires at **01:00 Asia/Kolkata**. It runs the overnight video wrapper, promoting `.job.ready` files only inside the **01:00–06:30 IST** window.

**DNS pin.** A short-interval agent re-pins public DNS (e.g., 1.1.1.1) and keeps Tailscale `accept-dns=false`, preventing MagicDNS from overriding resolvers while the mesh stays up.

These agents start, log, and stop. They do not invent affiliate slugs, open payment flows, or deploy Pages.

## What stays untouched

**Tailscale.** Keep the mesh running for remote access and optional Ollama serve on the tailnet. Daytime content work does not logout, uninstall, or rewrite Network Extension state.

**Freqtrade dry_run.** Paper trading stays up 24/7. Content and video scripts unload Ollama for night RAM; they do not `trade-kill` or flip live.

**Payments and Cloudflare publish.** No store checkout from the bot. No `wrangler pages publish` from a daytime wake. Hugo `--minify` may write `site/public` locally; humans own the first public ship, disclosure page, and `/go/` allow-list review against `links.csv`.

## Daytime agent rules

Outside the night window, agents continue **content**: blog articles, ebook chapters, claims, short voice scripts, dry Hugo wiring. They may **inspect** the overnight video jobs queue (ready / running / done / failed) and read sanitize notes. They must **not** start overnight renders, promote jobs into the live runner, or treat a closed `ai-window` as an invitation to "just test one clip."

Leave-alone extends to noise: do not chase Freqtrade log lines or Tailscale heal chatter unless the wake's brief says so. Attention stays on the writing kit — askai write → ≤0.9× cut → extract-claims → voice ≤120 words — and on local site wiring.

## Hand-off note before 01:00–06:30 IST

Before the calendar agent wakes, leave a short night hand-off in notes:

1. Confirm **two** `.job.ready` files under the render queue (e.g., `small-complex` and `bigger-complex` templates already sanitized).
2. State that daytime did **inspect-only** — no overnight video jobs start.
3. Remind: unload chat models inside the night wrapper; leave Tailscale and Freqtrade alone.
4. Remind: still no Cloudflare publish from the overnight path.

When `ai-window` reports the window closed, the correct daytime verb is **prepare**, not **render**. The LaunchAgent owns the clock; the hand-off owns the checklist.

That is the quiet-desk contract: schedule in LaunchAgents, prose by day, video by night, mesh and paper trading untouched, publish still a human gate.
