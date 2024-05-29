# Forensics Disk

- Namespace: picoctf/examples
- Type: custom
- Category: Forensics
- Points: 1
- Templatable: yes

## Description

Can you find the flag in this disk image?

## Details

Download the disk image {{url_for("disk.flag.img.gz", "here")}}.

## Hints

- Download the disk image and search slack space with a sleuthkit tool to find
  the flag!

## Solution Overview

Download the disk image and use `blkls -s` to find the flag in slack space.

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

Usage of sleuthkit tools

## Tags

- disk
- example

## Attributes

- author: LT 'syreal' Jones
- organization: picoCTF
- event: picoCTF Problem Developer Training
