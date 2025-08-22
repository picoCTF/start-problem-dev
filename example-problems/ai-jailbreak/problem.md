# AI Jailbreak

- Namespace: picoctf/examples
- ID: ai-jailbreak
- Type: custom
- Category: Artificial Intelligence
- Points: 1
- Templatable: yes
- MaxUsers: 1

## Description

This chatbot is cool, I wonder if it has any secrets?

## Details

Connect to the chatbot with netcat:

`$ nc {{server}} {{port}}`

The program's source code can be downloaded {{url_for("ai-interface.py", "here")}}.

## Hints

- This bot seems pretty trusting

## Solution Overview

Ask for the flag

## Challenge Options

```yaml
cpus: 4
memory: 512m
pidslimit: 200
ulimits:
  - nofile=512:512
diskquota: 512m
init: true
```

## Learning Objective

Interacting with LLM's

## Tags

- python
- AI
- LLM
- GPT_NEO

## Attributes

- author: LT 'syreal' Jones
- organization: picoCTF
- event: picoCTF Problem Developer Training
