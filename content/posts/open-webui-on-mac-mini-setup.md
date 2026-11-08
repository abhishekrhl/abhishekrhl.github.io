---
title: "Open WebUI on a Mac mini without Docker"
date: 2026-11-08T23:50:00+05:30
draft: false
slug: "open-webui-on-mac-mini-setup"
tags: ["local-ai", "apple-silicon", "ollama"]
description: "Install Open WebUI on a Mac mini without Docker using uvx or pip, connect it to Ollama, and keep memory in check."
author: "LogicatInc"
---

> **Affiliate disclosure:** Some links are affiliate links. As an Amazon Associate I earn from qualifying purchases. See [Disclosure](/disclosure/). AI-assisted drafting runs on a local Ollama desk; a human still gates claims before public ship.

# Open WebUI on a Mac mini without Docker

Open WebUI gives Ollama a browser chat interface with history, model switching and document uploads. On a 16 GB Mac mini, you can run it as a plain Python app rather than in Docker. Here is the setup, following the project's own [quick start guide](https://docs.openwebui.com/getting-started/quick-start/).

## Before you start

- Ollama installed and running (the Mac app starts the server for you). Check with `ollama ps`.
- Python 3.11 or 3.12. The Open WebUI docs say Python 3.13 is not supported, because some dependencies have no 3.13 release.
- Optionally, [uv](https://docs.astral.sh/uv/), which can fetch the right Python for you.

## Option 1: one command with uv

The quick start guide gives this command for macOS:

```bash
DATA_DIR=~/.open-webui uvx --python 3.12 open-webui@latest serve
```

`DATA_DIR` keeps your chats and settings in `~/.open-webui`, so they survive upgrades. The guide recommends setting it to avoid losing data.

## Option 2: a virtual environment with pip

```bash
python3.12 -m venv ~/open-webui-venv
source ~/open-webui-venv/bin/activate
pip install open-webui
DATA_DIR=~/.open-webui open-webui serve
```

Either way, open http://localhost:8080 in your browser. The first account you create is the administrator, and the docs note that sign-up switches itself off once that admin account exists.

## Connecting to Ollama

Ollama's default address is `http://localhost:11434`. If your models do not appear, set that address under your avatar → Settings → Admin → Connections, and confirm Ollama answers:

```bash
curl -s http://localhost:11434/api/tags | head -c 300
```

## Using it from another device

By default, `open-webui serve` is for use on the Mac itself. The quick start guide notes you can change the address and port with `--host` and `--port`, for example `open-webui serve --port 3000`. If you open it to your home network:

- Leave sign-up off unless you really want other people to make accounts.
- Only do this on a network you trust.

Ollama itself listens only on `127.0.0.1:11434` by default, according to the [Ollama FAQ](https://docs.ollama.com/faq). Open WebUI talks to it locally, so you do not need to expose Ollama to the network to use the web UI from a phone.

## Memory on a 16 GB Mac

The model is what uses most of the memory, not the web UI. These are the model sizes `ollama ps` reported in our own runs on a 16 GB Mac mini M4 ([benchmarks.json](/benchmarks.json)):

| Model | Context | Memory in `ollama ps` |
| :--- | :--- | :--- |
| `qwen3.5:4b` | 8K | 4.4 GB |
| `qwen3.5:9b` | 8K | 8.1 GB |

If the Mac slows down, pick a smaller model or a shorter context in the chat settings, and check `ollama ps` to see what is loaded.

## Stopping and upgrading

Press Ctrl+C in the terminal to stop the server. To upgrade, run the `uvx ... open-webui@latest serve` command again, or `pip install -U open-webui` inside the virtual environment. Your data stays in `DATA_DIR`.

For running llama.cpp alongside Ollama, see [Open WebUI and llama.cpp beside Ollama](/posts/open-webui-llama-cpp-beside-ollama/).
