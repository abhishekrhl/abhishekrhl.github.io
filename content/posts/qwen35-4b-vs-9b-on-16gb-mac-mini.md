---
title: "Qwen3.5 4B vs 9B on a 16 GB Mac mini M4: measured speed and memory"
date: 2026-11-08T23:50:00+05:30
draft: false
slug: "qwen35-4b-vs-9b-on-16gb-mac-mini"
tags: ["local-ai", "apple-silicon", "ollama"]
description: "Measured Ollama generation speed, prompt speed and model memory for Qwen3.5 4B and 9B on a 16 GB Mac mini M4."
author: "LogicatInc"
---

> **Affiliate disclosure:** Some links are affiliate links. As an Amazon Associate I earn from qualifying purchases. See [Disclosure](/disclosure/). AI-assisted drafting runs on a local Ollama desk; a human still gates claims before public ship.

# Qwen3.5 4B vs 9B on a 16 GB Mac mini M4: measured speed and memory

Should you run the 4B or the 9B version of Qwen3.5 on a 16 GB Mac mini? We measured both with Ollama on our own Mac mini M4 (16 GB, 120 GB/s memory bandwidth per [Apple's tech specs](https://support.apple.com/en-us/121555)). Here are the numbers and what we take from them.

## How we measured

- Ollama, `qwen3.5:4b` and `qwen3.5:9b`, thinking turned off, temperature 0.2.
- Short runs: a 35-token prompt and a 256-token answer, three runs per setting.
- Long runs: prompts of about 2,000 and 7,800 tokens and a 1,024-token answer, two runs per setting.
- Speed is Ollama's own `eval_count / eval_duration`. Memory is the model size reported by `ollama ps`, the highest value we saw.

All the raw numbers are in [benchmarks.json](/benchmarks.json).

## Short runs (256-token answers)

| Model | Context | Generation speed, median (tokens/s) | Memory in `ollama ps` |
| :--- | :--- | :--- | :--- |
| 4B | 4K | 22.4 | 4.25 GB |
| 4B | 8K | 23.2 | 4.37 GB |
| 9B | 4K | 19.4 | 7.93 GB |
| 9B | 8K | 19.2 | 8.11 GB |

## Long runs (1,024-token answers)

| Model | Context | Prompt tokens | Prompt speed (tokens/s) | Generation speed (tokens/s) | Memory in `ollama ps` |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 4B | 8K | 1,976 | 376, 386 | 23.0, 23.3 | 4.4 GB |
| 4B | 16K | 7,796 | 357, 346 | 21.7, 21.8 | 5.3 GB |
| 9B | 8K | 1,977 | 200, 190 | 22.7, 23.6 | 8.1 GB |
| 9B | 16K | 7,797 | 180, 179 | 22.4, 21.4 | 9.1 GB |

The 9B model generated faster in the long runs than in the short ones. We have not worked out why, so don't treat the gap between the two tables as meaningful.

## What we take from it

- **Generation speed is close.** In the long runs both models wrote at about 21–24 tokens per second. The 9B model is not much slower at writing.
- **Reading long prompts is where the 4B model wins.** It processed prompts roughly twice as fast as the 9B model in our runs. If you paste long documents, you will notice that.
- **Memory is the real difference.** The 9B model takes about twice the memory, 8–9 GB against 4–5 GB. On a 16 GB Mac, the 9B model plus a browser and an editor fits, but two models loaded at once does not leave much room.

## Which one we use

We use the 4B model for quick jobs (outlines, summaries, checks) and the 9B model when the quality of the writing matters. Load one at a time and unload with `ollama stop` when you switch. The [Ollama FAQ](https://docs.ollama.com/faq) covers `ollama stop` and `ollama ps`.

These numbers come from one machine and one Ollama version. Your results will differ with other models, settings and macOS versions.
