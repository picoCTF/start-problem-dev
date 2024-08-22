# Disk Problem Creation Walkthrough

## Pre-requisites

1. You have `cmgr` installed and configured.
    - Refer to the [setup page](/setup-cmgr.md) if this is not the case for you.

2. You have done the [Forensics Grep Problem Creation
   Walkthrough](/example-problems/forensics-grep). This document builds on
   everything in the Forensics Grep walkthrough.

## Overview

This problem is an example of creating a challenge that has significant work
outside of cmgr. Creating a disk worthy of being imaged for a forensics
challenge is a difficult task, and this all happens outside of cmgr. After broad
experimentation, my favorite way to create a disk for a forensics challenge is
using a traditional virtual machine. Even if we could, we probably wouldn't want
to put this process of virtual machine creation in the cmgr/Docker pipeline.
Instead, we copy the raw disk image to our problem folder when it is ready for
templating. After that, the problem is much like previous walkthroughs such as
[Forensics Grep](/example-problems/forensics-grep/).

We'll look at the following points:

1. The strategy of creating a disk image
1. The file listing and any significant changes
1. The problem of cheesing

## Walkthrough

### Disk Image Creation

I'm capturing the high level notes on my disk image creation process here so
that others can do something similar for creating disk images for CTF
challenges. I initially tried many different methods for capturing a disk image
such as imaging from a Docker container and using Vagrant, but I've found that
using Virtualbox and creating a standard virtual machine (VM) is the most
straightforward method for this endeavor.

1. Create a virtual machine in Virtualbox
   - I opt for VMDK virtual disks.
2. Do something of forensic interest
   - Create files, change timestamps, etc.
3. Make a clone of the original VM
   - This is needed because otherwise the virtual disk can be spread out over
     multiple files. Cloning turns the VMDK into a single file.
4. Convert virtual disk file into raw disk format
   - `qemu-img convert -f vmdk -O raw disk.vmdk disk.img`

### File Listing

1. [Dockerfile](/example-problems/forensics-disk/Dockerfile). Most of the
   changes here have been explained in the previous walkthrough. One new thing
   is that we're back to using `ubuntu` as a base image. We could've used a
   `python` base like in the previous walkthrough, but I wanted to demonstrate
   how to use `apt-get` for a challenge. `DEBIAN_FRONTEND=noninteractive`
   ensures that the `apt-get` process doesn't get halted by some interactive
   prompt. This directive needs to be specified right before `apt-get install`.
   Since there was only 1 package we needed, I kept it on the same line, but if
   there are multiple packages, each package should be on its own line and each
   item should be alphabetized. Other than that, for the offset for byteblast, I
   created a file and this offset is the first byte after the end of the file.
   For more information, look up [slack
   space](https://stackoverflow.com/a/71760523/4798333).

1. There's not much new in
   [problem.md](/example-problems/forensics-disk/problem.md). The only major
   difference between this problem.md and the static sanity's problem.md is that
   we specify that this problem is Templatable [in this
   section](/example-problems/forensics-disk/problem.md#forensics-disk). This
   means that multiple instances of this problem can be ran and each will have a
   different flag. Having multiple instances of the same problem gives many
   benefits. Most importantly for problem developers, it means we can detect
   cheating and regenerate flags on the fly.

1. [disk.img.gz](/example-problems/forensics-disk/disk.img.gz) is the image of
   the disk before it has the flag in it. For templating, adding the flag needs
   to happen at build time so that the flag can be different for each build.

1. [byteblast.py](/example-problems/forensics-disk/byteblast.py) is a script
   that I use in many problems that can insert bytes at arbitrary points in a
   file. This comes in hand for inserting templated flags in artifacts
   programmatically at build-time.

### The Problem of Cheesing

This problem is great, but it actually has a little problem. It can be solved
very easily while totally bypassing the intended learning objective. It's meant
to be solved using the Sleuthkit, but it can more easily solved just using
`grep`.

`strings disk.flag.img | grep picoCTF`

This is called "cheesing" the problem. It's finding an easier, unintended
solution to a CTF problem. The most common cheese is `grep`. it's always good to
try it on your own problem to make sure it's not greppable. Forensics and
Reverse Engineering problems are particularly susceptible because they often
embed the flag in downloadable artifacts. Besides just making sure the flag
isn't greppable, testing the problems with good CTF players is the most helpful
thing, and it's the only way for more complex problems like Binary and Web
Exploitation to have a good pre-launch check.

For text like this, there are a couple simple "obfuscation" techniques. One of
the most used is base64 encoding the flag. If you use this method, I recommend
"salting" the flag and base64 encoding something like this: `aaaa picoCTF{...`
otherwise, the beginning of the base64 encoded string will still be greppable
(though admittedly unlikely).

Other options include: encoding the flag as ASCII art, introducing spaces
between characters, encoding text as UTF-16, or using the "in-scope" problem
material, like for this problem, you could split the flag between multiple slack
spaces, ordered such that using `blkls -s` still prints the right string.

While external testing is critical for reducing the cheese in a competition, you
as the problem author need to think outside the box with your problem as much as
possible to anticipate alternate solutions and determine whether they are
acceptable or not.

## Conclusion

With this walkthrough, we demonstrated using highly developed computer system
artifacts as part of a cmgr problem. We don't attempt to generate this disk
image artifact in Docker, we generate a template using a traditional VM and
overwrite the bytes at a very specific location.

We also discuss the problem of cheesing which is when players solve a challenge
in a much easier way that sidesteps the learning objective of the problem. There
are multiple obfuscation techniques that can be applied to flags hidden in
downloadable artifacts, with base64 encoding probably being the preferred
method. Salting a flag can help a base64 blob be nearly impossible to grep for.

[Next problem](/example-problems/web-css)

[Return to the index](/example-problems#example-problems)
