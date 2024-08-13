# General SSH

- Namespace: picoctf/examples
- ID: general-ssh
- Type: custom
- Category: General Skills
- Points: 1

## Description

Do you know how to move between directories and read files in the shell?

## Details

`ssh -p {{port("ssh")}} ctf-player@{{server("ssh")}}` using password 
`{{lookup("password")}}`

## Hints

- Finding a cheatsheet for bash would be really helpful!

## Solution Overview

Login to the remote machine and use `ls` to find pieces of the flag and hints
to the next one.

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

Usage of ssh and bash commands

## Tags

- ssh
- bash
- example

## Attributes

- author: LT 'syreal' Jones
- organization: picoCTF
- event: picoCTF Problem Developer Training
