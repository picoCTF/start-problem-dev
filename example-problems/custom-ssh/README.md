# Custom SSH Problem Creation Walkthrough


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
our challenge. In Custom SSH, we spin up an Ubuntu container and make it an ssh
server. Specifying our own Dockerfile gives us tremendous freedom but also
comes at the cost of more frequent debugging. Building our own Docker container
using our Dockerfile is key to properly debugging what is going wrong when we
are developing a `custom` challenge for cmgr. Cmgr gives a decent error report,
but the mechanics of the Docker build process remain opaque to the problem
developer just looking at `cmgr build ...`. Manually building using your
Dockerfile can give much greater insight into what is happening during your
build. The final section in this walkthrough before the conclusion goes into
greater depth on how to do this.


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
   
5. [config-box.py](/example-problems/custom-ssh/config-box.py) This script
   is the meat of setting up the machine for our problem. It generates the
   password for the ctf-player user, creates the user, creates supporting
   directories and splits the flag into 3 parts, distributing them across the
   filesystem.
   
7. [Dockerfile](/example-problems/custom-ssh/Dockerfile) this file is quite
   involved as it pulls an Ubuntu 18.04 image down, updates the container,
   installs addtional packages and runs the config-box.py Python script to
   ready the container to be the Custom SSH challenge. Please view the file
   directly to view more specific comments on its functionality.


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
4. Build the problem with cmgr
      - `cmgr update`
      - `cmgr build syreal/examples/custom-ssh 9001`
      - Expected output:
```
cmgr: [ERROR:  failed to build image: The command '/bin/sh -c python3 config-box.py' returned a non-zero code: 2]
error: failed to build image: The command '/bin/sh -c python3 config-box.py' returned a non-zero code: 2
```
* We at least know which step failed, however, we can get much more info
  by building the container manually with Docker:

5. Build the container manually.
    - `docker build .`
    - Expected output (tail end):
```
Step 11/13 : RUN python3 config-box.py
 ---> Running in f696b2257959
python3: can't open file 'config-box.py': [Errno 2] No such file or directory
The command '/bin/sh -c python3 config-box.py' returned a non-zero code: 2
```
6. Fix the issue.
    - `RUN python3 config-box.py` needs to be `RUN python3 /challenge/config-box.py`

## Conclusion

With this walkthrough, we created an advanced problem that used a custom
Dockerfile to create a container that could be ssh'd to and had parts of a
flag scattered across the filesystem.

Using the custom problem type in cmgr opens the doors to creativity but also
needs more powerful debugging. This walkthrough also demonstrated how to
gain more debugging insight into custom cmgr problems by building the
container manually with docker which provides a lot more information about
build failures.

[Return to the index](/README.md#walkthroughs)

