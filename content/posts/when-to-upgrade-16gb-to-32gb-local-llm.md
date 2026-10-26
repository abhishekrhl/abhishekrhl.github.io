---
title: "When to move from 16 GB to 32 GB for local LLMs"
date: 2026-10-26T09:53:45+05:30
draft: false
slug: "when-to-upgrade-16gb-to-32gb-local-llm"
tags: ["local-ai", "apple-silicon", "ollama", "buyer-guides"]
description: "When a 32 GB Mac mini config is worth it for local LLMs — soldered RAM, concurrent Hugo+Ollama, context pressure. Allow-list links only."
---

> **Affiliate disclosure:** Some links are affiliate links. As an Amazon Associate I earn from qualifying purchases. See [Disclosure](/disclosure/). AI-assisted drafting runs on a local Ollama desk; a human still gates claims before public ship.

On a 16 GB Mac mini, swap often shows up before you “need a bigger model.” This note is a buyer decision for **when a 32 GB config is worth it** for local LLMs — concurrent Hugo + Ollama + Freqtrade `dry_run`, context length pressure, and the hard rule that Apple silicon unified memory is **soldered at purchase** (you configure RAM when you buy; you do not socket-upgrade later).

Shopping stubs (allow-list only): [Mac mini M4 16 GB](/go/mac-mini-m4-16gb/), [Mac mini M4 32 GB](/go/mac-mini-m4-32gb/). No Apple list prices invented here — check Apple or the search stub on the day you buy.

Related: [RAM × model matrix (16 GB Ollama)](/posts/ram-model-matrix-16gb-ollama/), [Mac mini dock vs T7 for models](/posts/mac-mini-dock-vs-t7-for-models/), [llama.cpp quant choices on 16 GB](/posts/llama-cpp-quant-choices-16gb/), [Quiet desk checklist](/posts/quiet-desk-checklist-16gb/), [Best Mac mini for local LLMs](/posts/best-mac-mini-for-local-llms/).

# When to move from 16 GB to 32 GB for local LLMs

## What “upgrade” means on a Mac mini

On current Mac mini (M4 / M4 Pro), unified memory is soldered. **There is no after-purchase RAM upgrade path.** “Upgrade to 32 GB” means:

1. Buy a **new** mini configured with 32 GB (or more), or
2. Keep the 16 GB desk and stop fighting swap with smaller models / shorter context / less concurrency.

Do not plan around DIY SODIMM myths from older Intel Macs. Editorial hardware overview: [/go/apple-silicon/](/go/apple-silicon/).

## Signals that 16 GB is already the bottleneck

Treat these as **operator signals**, not lab benches:

- Activity Monitor (or `vm_stat`) shows sustained swap / compressor pressure while a Q4 ~8–9B class tag is loaded **and** Hugo is mid-build.
- `ollama ps` shows a warm model, but chat latency spikes whenever a second heavy process starts (browser UI, static build, backtest).
- Raising `num_ctx` is what tips you into jetsam or multi-second stalls — not just the weight file size.

For which model classes usually fit a quiet 16 GB desk, start with the [RAM × model matrix](/posts/ram-model-matrix-16gb-ollama/). Editorial runners: [/go/ollama/](/go/ollama/), [/go/llama-cpp/](/go/llama-cpp/).

## The concurrent triad: Hugo + Ollama + Freqtrade dry_run

A common quiet-desk mix on this machine:

| Piece | Typical pressure on 16 GB (operator estimate) |
| :--- | :--- |
| macOS + light desk tools | multi-GB baseline (often ~2–3 GB idle; more after a long day) |
| Ollama Q4 ~8–9B class | weight file multi-GB; runtime RSS higher once KV cache grows |
| Hugo `--minify` build | hundreds of MB to ~1 GB+ depending on theme / parallelism |
| Freqtrade `dry_run` / light backtest | often another couple of GB when dataframes are warm |

Exact RSS varies by tag, theme, and dataset — **measure on your box**. The point of the table is concurrency: three “fine alone” workloads stack into swap on 16 GB. Leaving Freqtrade in `dry_run` (never stopping a live bot from this pipeline) still costs RAM.

If you need that triad warm at once, **32 GB is the practical answer**. If you can serialise (stop Hugo builds while chatting; unload the model before a heavy backtest), 16 GB can still work.

## Context length — where the false “GB per token” myth fails

Do **not** budget “~1 GB RAM per context token.” That figure is wrong by orders of magnitude. Runtime memory is roughly:

**weights (quantised) + KV cache (scales with context × architecture) + OS / other apps**

KV cache grows with context, but per-token cost is measured in **kilobytes-class**, not gigabytes, for typical GGUF/Ollama setups — still enough that a jump from 4k → 32k context can be the difference between “stable” and “swap thrash” on 16 GB once a mid-size Q4 is resident. Prefer measuring: note RSS at your working `num_ctx`, then raise context until compressor/swap appears.

Rule of thumb for this desk (operator, not a published benchmark):

- **Stay on 16 GB** if daily drivers are Qwen-class ~4B Q4, short-to-medium context, and you unload before heavy builds.
- **Buy 32 GB** if you want ~8–9B Q4 warm **while** Hugo/UI/backtest stay up, or you routinely need longer context without babysitting unload cycles.
- **Above 32 GB** only when your own `ollama ps` + Activity Monitor say larger tags or long context still fight the OS — do not invent a 70B-on-laptop story without measuring.

## Optimise before you spend

Before replacing the machine:

1. Drop to a leaner quant / smaller tag (see [quant choices](/posts/llama-cpp-quant-choices-16gb/)).
2. Cap `num_ctx` to what you actually use.
3. Keep the **active** model library on a fast Thunderbolt NVMe path if reloads are painful — [dock vs T7](/posts/mac-mini-dock-vs-t7-for-models/) — storage speed does not add RAM, but it shortens the painful reload window.
4. Unload idle models (`ollama stop`) when free memory approaches the content-engine floor.

If those steps kill the swap and you still finish work, keep the 16 GB mini.

## Buyer call

| Situation | Call |
| :--- | :--- |
| Single Q4 ~4B, short context, serialised builds | **Stay 16 GB** |
| Q4 ~8–9B + Hugo/UI at once, or long context without unload discipline | **Configure 32 GB at purchase** |
| Expecting user-upgradable RAM later | **No-Go myth** — soldered; buy the config you need |

Allow-list shopping stubs when you are ready: [16 GB M4 search](/go/mac-mini-m4-16gb/), [32 GB M4 search](/go/mac-mini-m4-32gb/). UK stubs exist without Associates tags yet. Commission possible; the Go/Caution table above is still about memory pressure, not a review score.

## Close

Upgrade when **measured** concurrency or context needs exceed a quiet 16 GB budget — not because a blog invented a GB-per-token rule. Cross-check the [RAM × model matrix](/posts/ram-model-matrix-16gb-ollama/) and keep model stores on a sensible path per [dock vs T7](/posts/mac-mini-dock-vs-t7-for-models/). Human still gates claims before public ship.
