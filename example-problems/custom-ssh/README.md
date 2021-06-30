# Docker Problem Creation Walkthrough


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

This problem uses a container as a ssh server and has 3 files scattered around
the filesystem that together compose the flag.

There is 1 main change in this problem that makes it more interesting:

1. The use of a Dockerfile instead of a Makefile which vastly opens up the
   possibilities for problem development.

Being able to specify a Dockerfile lets cmgr spin up container(s) specific for
our challenge. In Magikarp Ground Mission, we spin up an Ubuntu container and
make it an ssh server. Specifying our own Dockerfile gives us tremendous
freedom but also comes at the cost of more frequent bugs. Building our own
Docker container using our Dockerfile is key to properly debugging what is
going wrong when we are developing a custom challenge for cmgr. Cmgr gives a
decent error report, but the mechanics of the Docker build process remain 
opaque to the problem developer. Manually building using your Dockerfile can
give much greater insight into what is happening during your build. The final
section in this walkthrough before the conclusion goes into greater depth on
how to do this.


## Walkthrough


### File Listing

1. There's not much new in 
   [problem.md](/example-problems/custom-ssh/problem.md).
   


### Debugging your Dockerfile

For typical problem playtest deployment and testing strategy, see 
[this section](/example-problems/sanity-static-flag#Deployment)



## Conclusion

[Return to the index](/README.md#walkthroughs)

