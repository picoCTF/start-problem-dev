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



### File Listing



## Conclusion




[Return to the index](/README.md#walkthroughs)

