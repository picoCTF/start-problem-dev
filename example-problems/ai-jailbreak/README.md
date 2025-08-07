# Reversing Python Problem Creation Walkthrough

## Pre-requisites

1. You have `cmgr` installed and configured.
    - Refer to the [setup page](/setup-cmgr.md) if this is not the case for you.

2. You have done the [Web CSS Problem Creation
   Walkthrough](/example-problems/web-css).

## Overview

This problem uses a container as a service host and presents this service
through a port. This problem is adapted from the live picoGym problem, [Picker-I](https://play.picoctf.org/practice/challenge/400).

This problem can be used as a template for any challenge that needs to host a
service that players connect to with netcat.

The following walkthrough will touch on new problem files and then look at how
to debug a Dockerfile by running it with Docker instead of cmgr.

## Walkthrough

### File Listing

1. [picker-I.py](/example-problems/reversing-python/picker-I.py) this is the
   vulnerable script that we will be hosting as a service on this container.

1. [start.sh](/example-problems/reversing-python/start.sh) starts a listener
   that receives connections. This script is ran as the last step in the
   Dockerfile. For this problem, we use socat to connect the output of our
   vulnerable script to a port, allowing users to interact with our script
   through the network.

1. [setup-challenge.py](/example-problems/reversing-python/setup-challenge.py)
   This script generates the flag for the problem and saves it in the important
   file, `/challenge/metadata.json`, which is required for every cmgr problem.

1. [Dockerfile](/example-problems/reversing-python/Dockerfile) this is the main
   setup for our problem. We pull down a pinned Ubuntu image, update it and
   install the required packages. We create the `/challenge` directory with
   specific permissions so only root can access it. `/challenge` is an
   important directory and contains files that cmgr needs to deploy a problem.
   We add `artifacts.tar.gz` to this directory as well, which contains a copy
   of the source for the service being run on the container.

NOTE: If you were hosting a vulnerable service that allowed arbitrary remote
code execution, you would want to consider separating the challenge building
container from the container hosting the service. If players landed a shell on
this machine, they would be able to read challenge management data, which
usually is not a problem, but is not the greatest look for a CTF competition.
See this [problem](/example-problems/general-ssh) for how to create multiple
containers for one challenge.

### Debugging your Dockerfile

For typical problem playtest deployment and testing strategy, see
[this section](/example-problems/sanity-static-flag#Deployment).

In this walkthrough we will demonstrate how to debug one's Dockerfile. Cmgr
does a decent job on relaying the error that it received when it tried to
build the Docker container, however, the entire build process is opaque to
the cmgr user, and some more control and introspection of the docker build
process goes a long way in being able to determine what is going wrong.

1. Clone this repo
2. Go to the reversing-python directory
    - `cd start-problem-dev/example-problems/reversing-python/`
3. Switch Dockerfiles. `Dockerfile.test` has 1 discrepancy in it.
    - `mv Dockerfile Dockerfile.good`
    - `mv Dockerfile.test Dockerfile`
4. Build the problem with cmgr
      - `cmgr update`
      - `cmgr playtest picoctf/examples/reversing-python`
      - Expected output:

         ```terminal
         cmgr: [ERROR:  failed to build image: The command '/bin/sh -c python3 /challenge/setup-challenge.py' returned a non-zero code: 2]
         error: failed to build image: The command '/bin/sh -c python3 /challenge/setup-challenge.py' returned a non-zero code: 2
         ```

      - We at least know which step failed, however, we can get much more info
      by building the container manually with Docker:

5. Build the container manually.
    - `docker build . --build-arg FLAG=picoCTF{deadbeef}`
    - Expected output (tail end):

      ```terminal
      > [7/9] RUN python3 /challenge/setup-challenge.py:
      #0 0.333 python3: can't open file '/challenge/setup-challenge.py': [Errno 2] No such
      file or directory
      ```

6. Fix the issue.
    - `RUN python3 /challenge/setup-challenge.py` needs to be `RUN python3 setup-challenge.py`

## Conclusion

With this walkthrough, we created an advanced problem that used a Dockerfile to
create a container that presented a service to be interacted with in the shell.

This walkthrough also demonstrated how to gain more debugging insight into cmgr
problems by building the container manually with docker which provides a lot
more information about build failures.

[Next problem](/example-problems/general-ssh)

[Return to the index](/example-problems#example-problems)
