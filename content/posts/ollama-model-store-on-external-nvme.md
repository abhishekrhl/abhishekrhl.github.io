---
title: "Ollama on External NVMe: A Safe Symlink Guide for 16 GB Mac Mini"
date: 2026-10-26T11:53:59+05:30
draft: false
slug: "ollama-model-store-on-external-nvme"
tags: ["local-ai", "apple-silicon", "ollama"]
description: "Local AI desk note — quality-gated draft."
---

> **Affiliate disclosure:** Some links are affiliate links. As an Amazon Associate I earn from qualifying purchases. See [Disclosure](/disclosure/). AI-assisted drafting runs on a local Ollama desk; a human still gates claims before public ship.

# Ollama on External NVMe: A Safe Symlink Guide for 16 GB Mac Mini

On a 16 GB unified memory Mac mini, loading large quantised models fills RAM instantly, forcing the system to swap or crash while the internal SSD chokes on OS and runtime overhead. This guide sets up an external NVMe as the primary model store via symlink, defines an eject safety routine to prevent corruption, and manages expectations around latency spikes.

## Why External Storage Matters

Internal storage on a 16 GB Mac mini is often consumed by the OS, virtual memory swap files, and the Ollama runtime itself. Moving `~/.ollama/models` to an external drive frees critical space on the internal SSD, keeping the system responsive while weights load from slower media. Not all file systems are suitable; the external drive must be formatted as APFS (preferably encrypted) or APFS Encrypted. exFAT or FAT32 will fail due to a lack of journaling support and permission structures required by macOS system calls. While Thunderbolt 3/4 offers sufficient bandwidth, the primary bottleneck remains IOPS rather than raw throughput.

## Symlink Setup

To redirect Ollama without losing existing downloads, create a persistent symbolic link from the internal home directory to the external mount point. First, identify your external drive name using `diskutil list` and note its volume identifier (e.g., `/Volumes/MyNVMe`). Ensure the target directory exists on the external drive:

```bash
mkdir -p /Volumes/MyNVMe/.ollama/models
```

Next, create the symlink in your home directory. It is safer to remove any existing broken link first:

```bash
rm -rf ~/.ollama/models
ln -s /Volumes/MyNVMe/.ollama/models ~/.ollama/models
```

Verify the link is active with `ls -l ~/.ollama/models`. If Ollama was running, it may have cached paths; restart the service or kill the runner (`killall ollama`) to ensure it recognises the new location immediately. Existing model files remain untouched on the external drive, preserving your downloads while shifting the logical path.

## The Eject Hazard

Unmounting an active volume while a process has open file handles is a guaranteed recipe for filesystem corruption or application crashes. If you eject the drive while Ollama is generating text, the runner may attempt to write tokens to a disappearing block device, resulting in a `SIGBUS` error or silent data loss. The protocol is strict: stop the inference service before disconnecting. Use `ollama stop <model_name>` for a graceful shutdown of the specific model, or `killall ollama` to terminate all runners on the machine. Only after confirming the process has ceased should you unmount the volume via Finder or `diskutil unmount`. This prevents the kernel from trying to flush buffers to a device that is no longer accessible.

## Performance and Latency Reality Check

While an external NVMe connected via Thunderbolt 3 or 4 can approach internal SSD speeds, latency spikes remain inevitable compared to native storage. Inference times increase slightly due to the additional hop through the controller, though throughput should remain adequate for 7B–13B parameter models on quantised versions (e.g., Qwen3.5:9b Q4_K_M). Do not expect parity with internal NVMe performance; context window loading may show noticeable delays as the system seeks data across the external interface. Specific controller speeds, such as PCIe Gen 3 versus Gen 4, influence this latency, but exact benchmarks vary by enclosure and cable quality. Manage expectations accordingly: this setup prioritises capacity over raw speed.

## Troubleshooting Common Pitfalls

Permission errors often arise if the external drive is not mounted with user ownership. Run `sudo chown -R $(whoami) /Volumes/MyNVMe/.ollama` to correct ownership issues. If the symlink breaks after a reboot, it usually indicates the mount point did not persist; macOS does not automatically remount volumes at boot without explicit configuration in System Settings or launchd agents. A "mount point not found" error typically signals the drive was ejected unexpectedly while Ollama was active; check `dmesg` for I/O errors and ensure the runner is stopped before removal. For deeper configuration details, see our guide on [core environment variables](/go/ollama/).

## Further Reading

Pair this with [Best external SSD for Ollama models (UK)](/posts/best-external-ssd-for-ollama-models-uk/) when choosing the drive, and [Samsung T7 Shield vs T9 for weights](/posts/samsung-t7-shield-vs-t9-for-weights/) if you are comparing portable SSDs. Core runner notes stay on the [Ollama project](/go/ollama/). For the broader desk budget, see [Best Mac mini for local LLMs](/posts/best-mac-mini-for-local-llms/).

## Next Steps

Stop the runner before every eject, keep the volume APFS, and treat external storage as capacity insurance — not a free speed upgrade. If internal free space is already choking swaps, move models out first; buy a faster enclosure only after you measure real load latency on your cable and dock.
