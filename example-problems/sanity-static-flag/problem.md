# Sanity Download

- Namespace: picoctf/examples
- ID: sanity-download
- Type: custom
- Category: General Skills
- Points: 1
- Templatable: no

## Description

Test your internet connection!

## Details

Download the flag {{url_for("flag.txt", "here")}}.

## Hints

- Download the file and open it in a text editor like vi or Notepad.

## Solution Overview

Download `flag.txt` and open it.

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

Test and verify your connectivity to our CTF

## Tags

- example

## Attributes

- author: LT 'syreal' Jones
- organization: picoCTF
- event: picoCTF Problem Developer Training
