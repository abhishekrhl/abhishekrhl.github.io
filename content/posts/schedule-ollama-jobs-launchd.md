---
title: "Scheduling local LLM jobs with launchd on a Mac mini"
date: 2026-11-08T23:50:00+05:30
draft: false
slug: "schedule-ollama-jobs-launchd"
tags: ["local-ai", "apple-silicon", "ollama"]
description: "Set up a launchd timed job for Ollama on macOS, what happens when the Mac sleeps, and memory tips for 16 GB."
author: "LogicatInc"
---

> **Affiliate disclosure:** Some links are affiliate links. As an Amazon Associate I earn from qualifying purchases. See [Disclosure](/disclosure/). AI-assisted drafting runs on a local Ollama desk; a human still gates claims before public ship.

# Scheduling local LLM jobs with launchd on a Mac mini

If you want a Mac mini to run Ollama jobs at set times, launchd is the scheduler macOS ships with. Here is how I set up a timed job, what launchd does when the Mac is asleep, and the mistakes worth avoiding on a 16 GB machine.

## launchd or cron?

Apple's own guide to [scheduling timed jobs](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/ScheduledJobs.html) recommends launchd. The practical difference is sleep: if the Mac is asleep at the scheduled time, a cron job is skipped until its next slot, while a launchd job with `StartCalendarInterval` runs when the Mac wakes. Neither runs if the machine is switched off.

So launchd does not wake the Mac for you. If a job must start at an exact time, keep the Mac awake (System Settings → Energy) or schedule a wake yourself.

## A minimal user agent

Save this as `~/Library/LaunchAgents/com.example.ollama-batch.plist`. It runs a script once a day at 09:30.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>com.example.ollama-batch</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/zsh</string>
    <string>/Users/you/scripts/ollama-batch.sh</string>
  </array>
  <key>StartCalendarInterval</key>
  <dict><key>Hour</key><integer>9</integer><key>Minute</key><integer>30</integer></dict>
  <key>StandardOutPath</key><string>/Users/you/Library/Logs/ollama-batch.log</string>
  <key>StandardErrorPath</key><string>/Users/you/Library/Logs/ollama-batch.err</string>
</dict>
</plist>
```

Leave out `KeepAlive`. With `KeepAlive` set to true, launchd restarts the script every time it exits, which is not what you want for a once-a-day batch.

Load it with:

```bash
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.example.ollama-batch.plist
launchctl print gui/$(id -u)/com.example.ollama-batch | head
```

## The batch script

The Ollama Mac app already runs the server, so the script does not need to start or kill it. Talk to it and let it unload the model afterwards:

```bash
#!/bin/zsh
set -eu
# Keep the Mac from idle-sleeping only while this script runs
exec caffeinate -i /bin/zsh -c '
  ollama run qwen3.5:4b "Summarise this file in five bullets: $(cat ~/notes/today.md)" > ~/notes/today-summary.md
  ollama stop qwen3.5:4b
'
```

`caffeinate -i` holds an idle-sleep assertion only for as long as the command it wraps is running ([caffeinate reference](https://ss64.com/mac/caffeinate.html)). `ollama stop` unloads the model straight away instead of waiting for the keep-alive timer, which is documented in the [Ollama FAQ](https://docs.ollama.com/faq).

## Keeping memory in check on 16 GB

- Run jobs one after another, not in parallel. The Ollama FAQ notes that memory use grows with `OLLAMA_NUM_PARALLEL` × context length.
- Check what is loaded with `ollama ps` before a big job.
- On our 16 GB Mac mini M4, a 9B model at a 16K context showed about 9.1 GB in `ollama ps` in our own measured runs ([benchmarks.json](/benchmarks.json)). That leaves room for one job at a time, not two.

## When it does not run

- `launchctl print gui/$(id -u)/com.example.ollama-batch` shows the last exit status.
- Read the `.err` log you set in the plist.
- Use full paths in the script. launchd does not load your shell profile, so `ollama` may not be on its `PATH`. Run `which ollama` in Terminal and use that path.

That is the whole setup: one plist, one script, logs you can read, and no assumption that the Mac will wake itself up.
