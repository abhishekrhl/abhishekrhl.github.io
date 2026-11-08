---
title: "Ollama Modelfiles: a reusable writing assistant on a 16 GB Mac mini"
date: 2026-11-08T23:50:00+05:30
draft: false
slug: "ollama-modelfile-custom-system-prompts"
tags: ["local-ai", "apple-silicon", "ollama"]
description: "Build a reusable writing assistant with an Ollama Modelfile: SYSTEM prompt, num_ctx and temperature, with measured 16 GB memory figures."
author: "LogicatInc"
---

> **Affiliate disclosure:** Some links are affiliate links. As an Amazon Associate I earn from qualifying purchases. See [Disclosure](/disclosure/). AI-assisted drafting runs on a local Ollama desk; a human still gates claims before public ship.

# Ollama Modelfiles: a reusable writing assistant on a 16 GB Mac mini

If you paste the same instructions at the start of every Ollama chat, a Modelfile saves you the trouble. It bakes a system prompt and a few settings into a named model you can run with one command. Here is the setup we use for drafting on a 16 GB Mac mini.

## What a Modelfile is

A Modelfile is a short text file that starts from an existing model and adds your own settings. The [Ollama Modelfile reference](https://docs.ollama.com/modelfile) lists every instruction. The three you need for a writing assistant are:

- `FROM`: the base model (required)
- `SYSTEM`: the system prompt the model always sees
- `PARAMETER`: settings such as `temperature` and `num_ctx` (the context window, in tokens)

## A writing-assistant Modelfile

Save this as `writer.Modelfile`:

```dockerfile
FROM qwen3.5:9b

SYSTEM """
You are an editor for a technical blog written in British English.
Answer with the edited text only. No preamble, no closing summary.
Keep the author's facts and numbers exactly as given. If something looks wrong, flag it in one line at the end.
"""

PARAMETER num_ctx 8192
PARAMETER temperature 0.6
```

Build and run it:

```bash
ollama create writer -f writer.Modelfile
ollama run writer "Tighten this paragraph: ..."
```

Both commands come straight from the Modelfile reference. To see what a model was built with, run `ollama show --modelfile writer`.

## Choosing `num_ctx` on 16 GB

A bigger context window uses more memory. These are the model sizes `ollama ps` reported in our own runs on a 16 GB Mac mini M4 ([full data](/benchmarks.json)):

| Model | `num_ctx` | Memory in `ollama ps` |
| :--- | :--- | :--- |
| `qwen3.5:4b` | 8192 | 4.4 GB |
| `qwen3.5:4b` | 16384 | 5.3 GB |
| `qwen3.5:9b` | 8192 | 8.1 GB |
| `qwen3.5:9b` | 16384 | 9.1 GB |

For editing a single post, 8192 is plenty and leaves room for a browser and an editor. We only raise it to 16384 when we paste long source material.

## Keep the system prompt short

The system prompt is sent with every request and takes up part of the context window. A few direct lines work better than a page of rules. If the model keeps doing something you dislike, add one specific line about it rather than rewriting the whole prompt.

## Keep your Modelfiles in Git

A Modelfile is plain text, so put it in a Git repository next to your other notes. When an output changes after you edit the prompt, `git log -p writer.Modelfile` shows exactly what you changed and when.

```bash
mkdir -p ~/modelfiles && cd ~/modelfiles
git init
git add writer.Modelfile
git commit -m "Writer: shorter system prompt, num_ctx 8192"
```

## If something goes wrong

| Symptom | What to check |
| :--- | :--- |
| Model fails to load or the Mac slows to a crawl | Lower `num_ctx` or use the 4B model, then check `ollama ps` |
| Model ignores the system prompt | Run `ollama show --modelfile writer` to confirm the `SYSTEM` block was built in |
| Edits to the file have no effect | Run `ollama create` again; the model does not reread the file by itself |

For more on memory, see our [16 GB RAM model matrix](/posts/ram-model-matrix-16gb-ollama/).
