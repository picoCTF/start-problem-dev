# Disk Problem Creation Walkthrough

## Pre-requisites

1. You have `cmgr` installed and configured.
    - Refer to the [setup page](/setup-cmgr) if this is not the case for you.

2. You have done the [Sanity Problem Creation
   Walkthrough](/example-problems/sanity-static-flag/README.md). You do not have
   to do every walkthrough that is listed as easier than this one, but you must
   at least do the Sanity Problem Creation Walkthrough. This walkthrough is
   presented as a set of changes from the sanity problem. The sanity problem
   walkthrough is the core of cmgr challenges, and this problem presents what
   must be added on top of that for a more complicated challenge.

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

1. There's not much new in
   [problem.md](/example-problems/forensics-disk/problem.md). The only major
   difference between this problem.md and the static sanity's problem.md is that
   we specify that this problem is Templatable [in this
   section](/example-problems/forensics-disk/problem.md#forensics-disk). This
   means that multiple instances of this problem can be ran and each will have a
   different flag. Having multiple instances of the same problem gives many
   benefits. Most importantly for problem developers, it means we can detect
   cheating and regenerate flags on the fly.

2. There's a bit more new in
   [Makefile](/example-problems/forensics-disk/Makefile). Since we are not just
   immediately handing over the flag like in the sanity problem, we create a
   target for a challenge artifact that contains the flag, namely
   `disk.flag.img.gz`. We byteblast in the flag past the end of a suspicious
   file and there are multiple ways to recover this using sleuthkit tools.

3. [packages.txt](/example-problems/forensics-disk/packages.txt) specifies
   installing python3 so that we can use my byteblast.py python script in the
   make process.

4. [disk.img.gz](/example-problems/forensics-disk/disk.img.gz) is the image of
   the disk before it has the flag in it. For templating, adding the flag needs
   to happen at build time so that the flag can be different for each build.

5. [byteblast.py](/example-problems/forensics-disk/byteblast.py) is a script
   that I use in many problems that can insert bytes at arbitrary points in a
   file. This comes in hand for inserting templated flags in artifacts
   programmatically at build-time.

## Conclusion

With this walkthrough, we demonstrated using highly developed computer system
artifacts as part of a cmgr problem. Thankfully, the static-make cmgr problem
type can be used for this advanced forensics problem but most of the work for
this problem happens outside of cmgr. The Makefile for this problem
demonstrates handling this large uncompressed file and compressing it again
before giving it as an artifact to the player.

[Return to the index](/example-problems)
