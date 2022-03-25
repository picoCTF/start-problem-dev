# Custom Web

- Namespace: picoctf/examples
- Type: custom
- Category: Web Exploitation
- Points: 1
- Templatable: yes

## Description

Do you know how to use the web inspector?

## Details
Browse {{link_as('/', 'here')}}, and find the flag!

## Hints

- Use the web inspector to find other files included by the web page.

## Solution Overview

Inspect the landing page to find the css file. Open the css file to find the 
flag.

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

Usage of web inspector

## Tags

- example

## Attributes

- author: LT 'syreal' Jones
- organization: picoCTF
- event: picoCTF Problem Developer Training
