# Sanity Problem Creation Walkthrough

This walkthrough will step you through what's needed to get a working sanity 
problem on a `cmgr` challenge server.

A sanity problem is one of the easiest problems in any CTF that is given as a
sanity check that your internet connection is working as intended, etc.



## Pre-requisites:

1. You have setup `cmgr`.
  - Refer to [the README](https://github.com/syreal17/start-problem-dev#setup)
    if this is not the case for you.



## Overview

We are going to create a "sanity check" problem, often refered to simply as
"sanity". This problem would be one of the easiest in the CTF and would act
as proof that at least your computer can talk to the CTF server.

We're starting with the sanity problem with this walkthrough series because it
is one of the simplest real world challenges that exist in every CTF.

The following walkthough has 3 parts:

1. File listing and explanation

2. Playtest deploy demo

3. Modification of problem source and redeploy

After the walkthrough there is an Appendix that goes into more detail about
what each line in both files does.

## Walkthrough

### File Listing and Explanation

Using `cmgr`, the Sanity Download problem is just 2 files, 1. `problem.md`, 
and, 2. `Makefile`:

  1. `problem.md` specifies the name of the problem, the description, and other
      metadata about the problem. Here is the [specification](https://github.com/ArmyCyberInstitute/cmgr/blob/master/examples/markdown_challenges.md)
      for this file in general.

  2. `Makefile` specifies the creation of the 'artifacts' or files associated
      with the problem, including the flag.



### Playtest deploy demo

We are going to take this problem from just 2 files to actual deployment.

1. Clone this repo.
2. `cd start-problem-dev/example-problems`
3. Get a copy of cmgr in the `example-problems` directory:
    - `wget https://github.com/ArmyCyberInstitute/cmgr/releases/download/v0.9.0/cmgr.tar.gz && tar xvzf cmgr.tar.gz`
4. Update cmgr with the sanity problem:
    - `sudo ./cmgr update sanity-static-flag/`
5. Ensure problem appears in cmgr list:
    - `sudo ./cmgr list`
6. Deploy problem in playtest mode:
    - `sudo ./cmgr playtest syreal/examples/sanity-download`
    - NOTE: this command might take a few minutes.
    - Expected output is something like: `challenge information available at: http://localhost:4242/`
7. Ensure you get the problem details by browsing to the listed host and port. It should look like this:
    - ![Successful deploy](/img/sanity-download-playtest.png)



### Modification and Redeploy

