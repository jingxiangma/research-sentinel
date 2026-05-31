# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Weekly Research Sentinel** — a tool that scrapes ArXiv and news sources to automatically update a living literature review focused on Geometry, Mathematical Physics, and AI.

## Automation

> **Disabled as of 2026-05-31.** The scheduled task `ResearchSentinel_WeeklyUpdate` has been disabled because this PC is no longer in active use. Run the pipeline manually as needed (see below), or re-enable/recreate the task on another machine.

~~The pipeline runs **fully locally** on Windows Task Scheduler (task name: `ResearchSentinel_WeeklyUpdate`), every Friday at 9:00pm. If the computer is off at that time, it runs on next boot (`StartWhenAvailable`). The GitHub Actions workflow is not in use.~~

~~The scheduled task executes `run_pipeline.bat`, which runs the three pipeline scripts in order and commits/pushes the results. Logs are written to `logs/pipeline.log`.~~

To re-enable on a new machine, create a scheduled task pointing to `run_pipeline.bat`:
- **Re-enable (if task still exists):** `powershell -Command "Enable-ScheduledTask -TaskName 'ResearchSentinel_WeeklyUpdate'"`
- **Run manually:** `powershell -Command "Start-ScheduledTask -TaskName 'ResearchSentinel_WeeklyUpdate'"`

## Manual Pipeline

Run scripts in this order:
1. `python src/arxiv_client.py`
2. `python src/news_client.py`
3. `python src/report_builder.py`

Then update `docs/changelog.md` and commit/push all changed files.

## Reviewer Priority Keywords

`src/reviewer.py` has a `PRIORITY_KEYWORDS` list at the top. Any fetched paper whose `matched_keywords` intersect this list is pinned verbatim into the `<!-- ARXIV_HIGHLIGHTS -->` block of `docs/lit_review.md`, regardless of what the LLM (Ollama llama3.2) selects. Edit this list when introducing new core lit-review topics so future pipeline runs surface them automatically instead of relying on the LLM to pick them up.

## Important: Update CLAUDE.md and README.md

Whenever a new feature or automation is introduced, update both this file and `README.md` to reflect it.
