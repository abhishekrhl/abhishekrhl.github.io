---
title: "Your first week with a local AI Mac mini: a checklist"
date: 2026-11-08T23:50:00+05:30
draft: false
slug: "first-week-local-ai-mac-mini-checklist"
tags: ["local-ai", "apple-silicon", "ollama"]
description: "A day-by-day first-week checklist for running Ollama on a 16 GB Mac mini, with measured model memory and speed."
author: "LogicatInc"
---

> **Affiliate disclosure:** Some links are affiliate links. As an Amazon Associate I earn from qualifying purchases. See [Disclosure](/disclosure/). AI-assisted drafting runs on a local Ollama desk; a human still gates claims before public ship.

# Your first week with a local AI Mac mini: a checklist

A 16 GB Mac mini runs small and mid-sized language models well, as long as you pick the right size and leave room for macOS. This is the checklist we follow on our own Mac mini M4. Most of it takes an evening.

## Day 1: check the machine

- Note your chip and memory: Apple menu → About This Mac. Everything below assumes 16 GB.
- Update macOS to the current release for your Mac.
- Check free disk space. Each model is a few gigabytes, so leave yourself plenty of headroom.
- Open Activity Monitor → Memory and look at Memory Pressure. Green before you start is what you want.

## Day 2: install Ollama and run a small model

- Install Ollama from ollama.com (or with Homebrew).
- Start with a small model and confirm it answers:

```bash
ollama run qwen3.5:4b "Say hello in one line."
```

- While it is loaded, run `ollama ps` to see how much memory it is really using. The [Ollama FAQ](https://docs.ollama.com/faq) explains the output.

## Day 3: pick the model size that fits

What we measured on our 16 GB Mac mini M4 with Ollama, generating 1,024-token answers ([full data](/benchmarks.json)):

| Model | Context | Answer speed (tokens/s) | Memory in `ollama ps` |
| :--- | :--- | :--- | :--- |
| qwen3.5 4B | 8K | 23.0–23.3 | 4.4 GB |
| qwen3.5 4B | 16K | 21.7–21.8 | 5.3 GB |
| qwen3.5 9B | 8K | 22.7–23.6 | 8.1 GB |
| qwen3.5 9B | 16K | 21.4–22.4 | 9.1 GB |

Our takeaway: a 9B model at 8K–16K context fits and still leaves room for a browser and an editor. Bigger models and longer contexts are where 16 GB starts to pinch.

- Try the 9B model and watch Memory Pressure. If it turns yellow or red, step down a size or close apps.
- If you see "out of memory", the model plus context is too big. Use a smaller model or a shorter context.

## Day 4: keep it quiet

- Long generations make the fan spin up. Short prompts and smaller models keep it quieter.
- Close heavy apps such as video calls and big browser sessions while long jobs run.
- Give the Mac mini space to breathe. Don't box it in.

## Day 5: tidy your models

- See what you have downloaded: `ollama list`
- Remove what you don't use: `ollama rm <model>`. This deletes it from disk; `ollama stop <model>` only unloads it from memory ([Ollama CLI reference](https://docs.ollama.com/cli)).
- You can always download a model again, so back up your prompts, notes and Modelfiles instead.

## Days 6 and 7: make it part of your routine

- Write down the two or three prompts you will actually use every day.
- Time one real task, such as summarising a document, and decide whether the 4B or the 9B is good enough.
- Keep one model as your default so you are not juggling downloads.

Next steps: [keep Ollama warm without eating RAM](/posts/keep-ollama-warm-without-eating-ram/) and the [16 GB RAM model matrix](/posts/ram-model-matrix-16gb-ollama/).
