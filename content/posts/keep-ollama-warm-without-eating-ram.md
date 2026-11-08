---
title: "Keep Ollama warm without eating your 16 GB of RAM"
date: 2026-11-08T23:50:00+05:30
draft: false
slug: "keep-ollama-warm-without-eating-ram"
tags: ["local-ai", "apple-silicon", "ollama"]
description: "How Ollama keep_alive works, measured model memory for 4B and 9B, and when to stop or unload on a 16 GB Mac mini."
author: "LogicatInc"
---

> **Affiliate disclosure:** Some links are affiliate links. As an Amazon Associate I earn from qualifying purchases. See [Disclosure](/disclosure/). AI-assisted drafting runs on a local Ollama desk; a human still gates claims before public ship.

# Keep Ollama warm without eating your 16 GB of RAM

On a 16 GB Mac mini, how long a model stays loaded matters. If you keep it loaded all day, you lose a big slice of memory you are not using. If you unload it after every prompt, you wait for a reload each time. Ollama gives you two controls, and this is how we use them.

## What Ollama does by default

The [Ollama FAQ](https://docs.ollama.com/faq) says models stay in memory for 5 minutes after the last request and are then unloaded. You can change that in two places:

1. **For the whole server:** the `OLLAMA_KEEP_ALIVE` environment variable. On the Mac app, set it with `launchctl setenv OLLAMA_KEEP_ALIVE 15m` and restart Ollama, as the FAQ describes.
2. **Per request:** the `keep_alive` field on `/api/generate` or `/api/chat`. It takes a duration such as `"10m"`, a number of seconds, a negative number to keep the model loaded indefinitely, or `0` to unload as soon as the answer is done.

## How much memory is at stake

Model memory reported by `ollama ps` in our own runs on a 16 GB Mac mini M4 (full data in [benchmarks.json](/benchmarks.json)):

| Model | Context | Memory in `ollama ps` |
| :--- | :--- | :--- |
| `qwen3.5:4b` | 8K | 4.4 GB |
| `qwen3.5:9b` | 8K | 8.1 GB |
| `qwen3.5:9b` | 16K | 9.1 GB |

A 9B model left loaded with `keep_alive: -1` holds roughly half the machine's memory until you stop it. That is fine during a writing session and wasteful overnight.

## The policy we use

| Situation | Setting | Why |
| :--- | :--- | :--- |
| A run of drafts back to back | `"15m"` | The model stays loaded between steps |
| One quick question | default (5 minutes) | It unloads soon after |
| Before something memory-hungry (video export, big build) | `ollama stop <model>` | Frees the memory right away |

## Unload, don't delete

`ollama stop <model>` unloads a model from memory and keeps it on disk. `ollama rm <model>` deletes the model from disk (see the [Ollama CLI reference](https://docs.ollama.com/cli)), so you would have to download it again. When memory is tight, use `stop`.

To unload everything that is loaded:

```zsh
ollama ps
ollama stop qwen3.5:9b
```

Or, through the API:

```zsh
curl -s http://127.0.0.1:11434/api/generate -d '{"model":"qwen3.5:9b","keep_alive":0}'
```

## A simple memory-pressure check

macOS reports free memory with `memory_pressure`. A small script can unload the model when free memory drops:

```zsh
free_pct=$(memory_pressure | awk -F': ' '/free percentage/ {gsub("%","",$2); print $2}')
if (( free_pct < 10 )); then
  ollama stop qwen3.5:9b
fi
```

The 10% threshold is our own choice, not an Ollama recommendation. Pick one that suits what else runs on your Mac.

For more on sizing, see our [16 GB RAM model matrix](/posts/ram-model-matrix-16gb-ollama/) and [batch drafting without swap thrash](/posts/batch-drafting-without-swap-thrash/).
