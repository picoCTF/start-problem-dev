# Forensics Grep

- Namespace: picoctf/examples
- ID: forensics-grep
- Type: custom
- Category: Forensics
- Points: 1
- Templatable: yes
- MaxUsers: 0

## Description

Can you find the flag in this large file?

Download War and Peace {{url_for("war-and-peace.flag.txt", "here")}}.

## Details

## Hints

- Download the file and use grep or Ctrl-F to find the flag based on the known
  prefix.

## Solution Overview

Download war-and-peace.flag.txt and grep for `pico`

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

Usage of command line tools

## Tags

- grep
- example

## Attributes

- author: LT 'syreal' Jones
- organization: picoCTF
- event: picoCTF Problem Developer Training
