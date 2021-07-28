# Forensics Disk

- Namespace: syreal/examples
- Type: static-make
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

## Learning Objective

Usage of sleuthkit tools

## Tags

- disk
- example

## Attributes

- author: LT 'syreal' Jones
- organization: picoCTF
