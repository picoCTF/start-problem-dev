# Sanity Download

- Namespace: picoctf/examples
- Type: static-make
- Category: General Skills
- Points: 1
- Templatable: no

## Description

Test your internet connection!

## Details
Download the flag {{url_for("flag", "here")}}.

## Hints

- Download the file and open it in a text editor like vi or Notepad.

## Solution Overview

Download `flag` and open it.

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
