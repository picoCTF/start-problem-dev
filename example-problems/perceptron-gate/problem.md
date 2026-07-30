# Perceptron Gate

- Namespace: academy/examples
- ID: perceptron-gate
- Type: custom
- Category: Reverse Engineering
- Points: 1
- Templatable: yes
- MaxUsers: 1

## Description

Probe a black-box perceptron and submit a matching model. If your model classifies all inputs exactly like the service, it will reward you.

## Details

Connect with netcat:

`$ nc {{server}} {{port}}`

The program's source can be downloaded {{url_for("perceptron_gate.py", "here")}}.

## Hints

- A perceptron with two binary inputs creates a linear threshold over {0,1}².
- Try querying all four inputs, then solve for weights and bias that reproduce the table.

## Solution Overview

Interact:
- Use `QUERY a b` to see outputs (up to 8 queries).
- Submit weights with `SUBMIT w1 w2 b`.
- If your submission matches the hidden model on all inputs, the program prints the flag.

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

Understand perceptron decision boundaries and practice black-box modeling.

## Tags

- python
- ml
- perceptron

## Attributes

- author: LT 'syreal' Jones
- organization: CyLab Security Academy
- event: picoCTF Problem Developer Training
