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

## What I take from it

1. **The 9B model is barely slower than the 4B one here.** About 19 tok/s against about 22 tok/s warm. On this box the 4B tag does not buy the doubling in speed that its size suggests, so I keep the 4B for short extraction jobs where its smaller footprint matters, not for raw speed.
2. **Both fit in 16 GB with room left.** The 9B model sat at about 8 GB resident at 8K context, leaving several GB for macOS and a static-site build. Long contexts and a second loaded model are where 16 GB gets tight; I have not measured those yet.
3. **Short runs flatter the numbers.** 256 tokens is a quick test. Long generations and large prompts will be slower, and I will add them as separate rows when I measure them.

## If you are choosing a Mac mini for this

For one 4B to 9B model at a time, the 16 GB base M4 handled it in my runs: [Mac mini M4 16 GB (Amazon.in)](/go/mac-mini-m4-16gb/) · [Amazon.co.uk](/go/mac-mini-m4-16gb-uk/). If you want headroom for longer contexts or a browser full of tabs beside the model, the 24 GB model is the safer buy, though I have no measured numbers for it: [Mac mini M4 24 GB (Amazon.in)](/go/mac-mini-m4-24gb/) · [Amazon.co.uk](/go/mac-mini-m4-24gb-uk/). Runtime: [Ollama](/go/ollama/).

The raw run data is published as [/benchmarks.json](/benchmarks.json), and the [RAM calculator](/tools/ram-calculator.html) uses the same measured rows.
