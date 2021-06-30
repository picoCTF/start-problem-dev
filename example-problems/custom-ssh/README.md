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

1. Besides problem details, the most important change in
   [problem.md](/example-problems/custom-ssh/problem.md) is changing Type to
   "custom".

2. instructions-to-Xof3.txt's contain verbal instructions on how to find the
   next part of the flag. The Dockerfile copies these into the container.

3. [profile](/example-problems/custom-ssh/profile) is a bash profile that
   places the newly logged in user into a different folder than their home
   directory. This is done so that returning home from the root directory
   yields the last part of the flag instead of the first.
   
4. [start.sh](/example-problems/custom-ssh/start.sh) starts a listener that
   receives ssh connections. This script is ran as the last step in the
   Dockerfile.
   
5. [gen-password.py](/example-problems/custom-ssh/gen-password.py) generates
   a short password based on a seed using crc32. This password is written to
   a file named `password` which is read by the Dockerfile to be put in
   `metadata.json`.
   
6. [split-flag.py](/example-problems/custom-ssh/split-flag.py) reads the
   flag from the file, `flag`, modifies it, and splits it into 3 parts,
   each of which are written to files that are later copied into different
   parts of the filesystem of the container by the Dockerfile.
   
7. [Dockerfile](/example-problems/custom-ssh/Dockerfile) this file is quite
   involved as it pulls an Ubuntu 18.04 image down, updates the container,
   installs addtional packages and runs multiple other shell commands and
   Python scripts to ready the container to be the Magikarp Ground Mission
   challenge. Please view the file directly to view more specific comments
   on its functionality.


### Debugging your Dockerfile

For typical problem playtest deployment and testing strategy, see 
[this section](/example-problems/sanity-static-flag#Deployment).

In this walkthrough we will demonstrate how to debug one's Dockerfile. Cmgr
does a decent job on relaying the error that it received when it tried to
build the Docker container, however, the entire build process is opaque to
the cmgr user, and some more control and introspection of the docker build
process goes a long way in being able to determine what is going wrong.

1. Clone this repo
2. Go to the custom-ssh directory
    - `cd start-problem-dev/example-problems/custom-ssh/`
3. Switch Dockerfiles. `Dockerfile.test` has 1 discrepancy in it.
    - `mv Dockerfile Dockerfile.good`
    - `mv Dockerfile.test Dockerfile`
4. 
   * Try to build the problem with cmgr
      - `cmgr update`
      - `cmgr build syreal/examples/magikarp-ground-mission 9001`
      - Expected output:
```
cmgr: [ERROR:  failed to build image: The command '/bin/sh -c echo "ctf-player:$(cat password)" | chpasswd' returned a non-zero code: 1]
error: failed to build image: The command '/bin/sh -c echo "ctf-player:$(cat password)" | chpasswd' returned a non-zero code: 1
```
   * We at least know what step failed, however, we can get much more info
     by building the container manually with Docker
5. Build the container manually.
    - `docker build .`
    - Expected output (tail):
```
Step 20/30 : RUN echo "ctf-player:$(cat password)" | chpasswd
 ---> Running in 42c1b67b6e85
cat: password: No such file or directory
No password supplied
No password supplied
No password supplied
chpasswd: (user ctf-player) pam_chauthtok() failed, error:
Authentication token manipulation error
chpasswd: (line 1, user ctf-player) password not changed
The command '/bin/sh -c echo "ctf-player:$(cat password)" | chpasswd' returned a non-zero code: 1
```
6. Fix the issue.
    - `$(cat password)` needs to be `$(cat /challenge/password)`

## Conclusion

[Return to the index](/README.md#walkthroughs)

