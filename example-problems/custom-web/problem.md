# Custom Web

- Namespace: syreal/examples
- Type: custom
- Category: Web Exploitation
- Points: 1

## Description

Do you know how to use the web inspector?

## Details
Browse `{{server("web")}}:{{port("web")}}`, and find the flag!

## Hints

- Use the web inspector to find other files included by the web page.

## Solution Overview

Inspect the landing page to find the css file. Open the css file to find the 
flag.

## Learning Objective

Usage of web inspector

## Tags

- web
- example

## Attributes

- author: LT 'syreal' Jones
- organization: picoCTF
