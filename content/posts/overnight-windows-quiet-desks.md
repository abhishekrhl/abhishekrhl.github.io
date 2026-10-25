---
title: "Overnight windows and quiet desks — scheduling local inference around Hugo builds and video jobs"
date: 2026-10-25T23:15:20+05:30
draft: false
slug: "overnight-windows-quiet-desks"
tags: ["local-ai", "scheduling", "freqtrade"]
description: "Practical local-AI notes for a 16 GB Apple silicon Mac mini — affiliate links disclosed."
---

> **Affiliate disclosure:** Some links are affiliate links. As an Amazon Associate I earn from qualifying purchases. See [Disclosure](/disclosure/).

Running a local inference stack alongside content creation and automated trading on 16 GB of RAM requires strict temporal separation. The primary friction lies in rival memory requirements. Loading heavy quantised models during peak daytime hours often results in swapping, latency spikes, or system crashes if VRAM and system RAM cannot simultaneously hold both model weights and active application context.

Ollama is popular for local deployment but risks instability on constrained hardware when running continuously alongside heavy applications like Hugo. The build process demands significant CPU cycles and temporary memory buffers, which directly conflicts with background model loading. To mitigate this risk, a strict temporal boundary isolates resource-intensive tasks from critical workflows.

The operational strategy defines specific "quiet hours" between 01:00 and 06:30 IST for local inference. During these hours, heavy inference and video jobs may run; paper trading (dry_run) stays up, while urgent drafting and other heavy daytime work yield. Outside this window, focus shifts to lightweight operations or complete system rest to preserve battery life and thermal headroom. Apple Silicon devices offer advantages in unified memory architecture but are not immune to physical limits. Continuous inference generates sustained thermal output; attempting to run a model while compiling code can cause aggressive throttling. The solution is scheduling execution when the machine is idle enough to absorb the thermal load without affecting immediate tasks.

Llama.cpp remains a foundational engine for local models, offering fine-grained control over quantisation. On a 16 GB system, loading a large model consumes nearly all available RAM exclusively. If another application tries to allocate memory during this time, the operating system must swap data to disk, resulting in stuttering. Therefore, deployment must be explicit: it is an overnight job, not a daytime companion. When managing a single machine, the Hugo build process takes precedence during daytime hours as it generates immediate deliverables. Conversely, model loading via `llama-cpp` or similar runtimes is deferred until the designated overnight window. A failed build renders no value, whereas a delayed inference job still fulfills its purpose once completed in the morning.

Voice synthesis tasks offer a middle ground for daytime usage if sufficiently lightweight. Tools like mlx-audio can handle text-to-speech with far smaller footprints than massive language models. A short TTS job might consume only a fraction of available memory, allowing limited daytime utility without triggering resource conflicts, provided total usage stays well below the 16 GB limit. The integration of video jobs adds complexity; encoding and decoding are CPU-intensive and generate significant heat. Running video renders while a model loads is inadvisable on constrained hardware. The priority hierarchy is clear: paper trading and live analysis take absolute precedence, followed by Hugo builds for content delivery, then light audio tasks, with heavy inference and video rendering relegated to the overnight slot.

Adhering to the IST calendar rule requires discipline. Users must resist the urge to run models during the day simply because they are available. On 16 GB hardware, "ready" often means "unstable." By accepting the delay, the user gains stability and predictability. One might draft content in the morning, queue the Hugo build for lunchtime, and let the inference job run while sleeping. Human oversight remains essential even with automated scheduling. A human rewrite step is necessary before any public paste to ensure tone, accuracy, and context are appropriate. Local models can hallucinate or produce content lacking nuance. The workflow should include a manual review phase after overnight inference completes.

(source: IST overnight window practice on 16 GB Apple Silicon desk)
