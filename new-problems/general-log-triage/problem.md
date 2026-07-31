# General Log Triage

- Namespace: academy/new-problems
- ID: general-log-triage
- Type: custom
- Category: General Skills
- Points: 1
- Templatable: yes
- MaxUsers: 0

## Description

An operations team captured a suspicious export workflow right before a system outage.

Download the triage bundle {{url_for("triage-bundle.tar.gz", "here")}}.

Recover the flag from the logs.

## Details

## Hints

- The requests with status code `418` are the only ones you need from `requests.log`.
- The final segment of each suspicious request path is an `export_id`.
- Use those IDs, in order, to pull matching chunks from `export-map.csv`.
- After combining the chunks, decode the resulting Base64 text.

## Solution Overview

Extract `triage-bundle.tar.gz`, then:

1. Filter `requests.log` for status `418` and extract each `export_id` from `/api/v1/export/<id>` in order.
2. Use each ID to pull a chunk from `export-map.csv` and concatenate chunks in that same order.
3. Base64-decode the combined string to recover the flag.

## Challenge Options

```yaml
cpus: 0.5
memory: 128m
pidslimit: 20
ulimits:
  - nofile=128:128
diskquota: 64m
init: true
```

## Learning Objective

Practice command-line triage with grep/awk/cut and data reconstruction.

## Tags

- logs
- grep
- awk
- base64

## Attributes

- author: GitHub Copilot
- organization: CyLab Security Academy
- event: Problem Developer Training
