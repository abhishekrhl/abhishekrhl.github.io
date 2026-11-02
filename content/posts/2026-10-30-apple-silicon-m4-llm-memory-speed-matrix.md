---
title: "Mac mini M4 16 GB: Measured Ollama Speed and Memory for Qwen3.5 4B and 9B"
date: 2026-11-02T12:18:00+05:30
draft: false
slug: "2026-10-30-apple-silicon-m4-llm-memory-speed-matrix"
tags: ["local-ai", "apple-silicon", "ollama", "benchmarks"]
description: "Twelve short Ollama runs on a base Mac mini M4 with 16 GB: generation tok/s and resident memory for qwen3.5:4b and qwen3.5:9b, with the raw JSON."
---

> **Affiliate disclosure:** Some links are affiliate links. As an Amazon Associate I earn from qualifying purchases. See [Disclosure](/disclosure/).

This page holds numbers I measured on my own desk machine, not estimates. If a model or a Mac is not in the table, I have not tested it, and I would rather leave the cell out than guess.

## The machine and the method

- **Hardware:** Mac mini (2024), Apple M4, 16 GB unified memory. Apple lists the base M4 at 120 GB/s memory bandwidth and the M4 Pro at 273 GB/s ([Apple tech specs](https://support.apple.com/en-us/121555)).
- **Runtime:** Ollama 0.40.7; the models are the stock `qwen3.5:4b` (4.0 GB on disk) and `qwen3.5:9b` (7.6 GB on disk) tags.
- **Run:** 2 November 2026, 12:15 to 12:18 IST. One 35-token prompt, 256 tokens max output, temperature 0.2, thinking disabled, three runs per model at `num_ctx` 4096 and 8192. Other desk services were idle, with about 78% of memory free before the first run.
- **What I report:** generation speed from Ollama's own `eval_count / eval_duration`, and resident size from `/api/ps`. I do not report prompt-processing speed, because the repeated prompt was cached and the figures are meaningless.

## Results

| Model | num_ctx | Gen tok/s (3 runs) | Resident memory (GB, `/api/ps`) |
|---|---|---|---|
| qwen3.5:4b | 4096 | 18.4 (cold), 22.4, 22.5 | 4.1 to 4.3 |
| qwen3.5:4b | 8192 | 21.1, 23.2, 23.5 | 4.3 to 4.4 |
| qwen3.5:9b | 4096 | 19.4, 19.4, 19.2 | 7.8 to 7.9 |
| qwen3.5:9b | 8192 | 19.2, 19.3, 17.8 | 8.0 to 8.1 |

Cold-load time was 6.3 s for the 4B model and 10.1 s for the 9B model from the internal SSD.

## Longer runs: big prompts and 1,024-token answers

Run 2 November 2026, 12:30 to 12:39 IST, same machine and Ollama version. Each run used a fresh prompt (so nothing was cached) and generated the full 1,024 tokens; two runs per cell.

| Model | num_ctx | Prompt tokens | Prompt tok/s (2 runs) | Gen tok/s (2 runs) | Peak resident (GB) |
|---|---|---|---|---|---|
| qwen3.5:4b | 8192 | 1,976 | 376, 386 | 23.0, 23.3 | 4.4 |
| qwen3.5:4b | 16384 | 7,796 | 357, 346 | 21.7, 21.8 | 5.3 |
| qwen3.5:9b | 8192 | 1,977 | 200, 190 | 22.7, 23.6 | 8.1 |
| qwen3.5:9b | 16384 | 7,797 | 180, 179 | 22.4, 21.4 | 9.1 |

Reading these: prompt processing on the 9B model ran at about half the 4B rate (roughly 180 to 200 against 345 to 385 tok/s), so a 7,800-token prompt took the 9B model about 43 seconds before it wrote anything. Resident memory grew with context, peaking at 9.1 GB for the 9B model at 16K. Generation on the 9B model was faster in these runs than in the short runs above; I have not worked out why, so I report both as measured rather than pick one.

## What I take from it

1. **The 9B model is barely slower than the 4B one here.** About 19 tok/s against about 22 tok/s warm. On this box the 4B tag does not buy the doubling in speed that its size suggests, so I keep the 4B for short extraction jobs where its smaller footprint matters, not for raw speed.
2. **Both fit in 16 GB with room left.** The 9B model sat at about 8 GB resident at 8K context, leaving several GB for macOS and a static-site build. At 16K context it peaked at about 9.1 GB (see the longer runs). I have not measured a second loaded model.
3. **Short runs flatter the numbers.** 256 tokens is a quick test. The longer runs above add large prompts and 1,024-token answers; prompt processing is where the 9B model is clearly slower.

## If you are choosing a Mac mini for this

For one 4B to 9B model at a time, the 16 GB base M4 handled it in my runs. The M4 has since been replaced: Apple now sells the Mac mini with the M6 (16, 24 or 32 GB; Apple lists 153 GB/s for 16 GB and 170 GB/s for 24 and 32 GB) and the M5 Pro (24 to 64 GB, 307 GB/s). I have not run these tests on either, so every number on this page describes the M4 only. The current 16 GB model: [Mac mini M6 16 GB (Amazon.in)](/go/mac-mini-m4-16gb/) · [Amazon.co.uk](/go/mac-mini-m4-16gb-uk/). If you want headroom for longer contexts or a browser full of tabs beside the model, 24 GB is the safer buy: [Mac mini M6 24 GB (Amazon.in)](/go/mac-mini-m4-24gb/) · [Amazon.co.uk](/go/mac-mini-m4-24gb-uk/). Runtime: [Ollama](/go/ollama/).

The raw run data is published as [/benchmarks.json](/benchmarks.json), and the [RAM calculator](/tools/ram-calculator.html) uses the same measured rows.
