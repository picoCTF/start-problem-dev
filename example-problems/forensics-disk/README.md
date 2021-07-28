# Disk Problem Creation Walkthrough


## Pre-requisites:

1. You have `cmgr` installed and configured.
    - Refer to the [setup section in the index](/README.md#setup)
      if this is not the case for you.

2. You have done the [Sanity Problem Creation Walkthrough](/example-problems/sanity-static-flag/README.md).
   You do not have to do every walkthrough that is listed as easier than this
   one, but you must at least do the Sanity Problem Creation Walkthrough. 
   This walkthrough is presented as a set of changes from the sanity problem.
   The sanity problem walkthrough is the core of cmgr challenges, and this 
   problem presents what must be added on top of that for a more complicated
   challenge.



## Overview

This problem is an example of creating a challenge that has significant work
outside of cmgr. Creating a disk worthy of being imaged for a forensics 
challenge is a difficult task, and this all happens outside of cmgr. After
broad experimentation, my favorite way to create a disk for a forensics
challenge is using a traditional virtual machine. Even if we could, we probably
wouldn't want to put this process of virtual machine creation in the
cmgr/Docker pipeline. Instead, we copy the raw disk image to our problem folder
when it is ready for templating. After that, the problem is much like previous
walkthroughs such as [Forensics Grep](/example-problems/forensics-grep/).



## Walkthrough


### Disk Image Creation

I'm capturing the high level notes on my disk image creation process here so
that others can do something similar for creating disk images for CTF challenges.
I initially tried many different methods for capturing a disk image such as
imaging from a Docker container and using Vagrant, but I've found that using
Virtualbox and creating a standard virtual machine (VM) is the most straightforward
method for this endeavor.

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



## Conclusion




[Return to the index](/README.md#walkthroughs)

