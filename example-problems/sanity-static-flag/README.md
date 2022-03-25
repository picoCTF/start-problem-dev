# Sanity Problem Creation Walkthrough

This walkthrough will step you through what's needed to get a working sanity 
problem on a cmgr challenge server.

A sanity problem is one of the easiest problems in any CTF that is given as a
sanity check that your internet connection is working as intended and all
other assumptions are being met as expected.



## Pre-requisites:

1. You have `cmgr`.

    - Refer to the [setup section in the index](/README.md#setup)
      if this is not the case for you.



## Overview

We are going to create a "sanity check" problem, often refered to simply as
"sanity". This problem would be one of the easiest in the CTF and would act
as proof that at least your computer can talk to the CTF server.

We're starting with the sanity problem with this walkthrough series because it
is one of the simplest real world challenges that exist in every CTF.

The following walkthough has 3 parts:

1. File listing

2. Deployment

3. Testing



## Walkthrough

### File Listing

Using cmgr, the Sanity Download problem is just 2 files:

  1.  [problem.md](/example-problems/sanity-static-flag/problem.md) specifies
      the name of the problem, the description, and other metadata about the
      problem. Here is the [specification](https://github.com/ArmyCyberInstitute/cmgr/blob/master/examples/markdown_challenges.md)
      for this file in general.

  2.  [Makefile](/example-problems/sanity-static-flag/Makefile) specifies the
      creation of the 'artifacts' or files associated with the problem,
      including the flag.



### Deployment

We are going to take this problem from just 2 files to actual deployment.

1. Clone this repo.
2. `$ cd start-problem-dev/example-problems`
3. Update cmgr with the sanity problem:
    - `$ cmgr update sanity-static-flag/`
4. Ensure problem appears in cmgr list:
    - `$ cmgr list`
    - Expected output: `syreal/examples/sanity-download`
5. Deploy problem in playtest mode:
    - `$ cmgr playtest syreal/examples/sanity-download`
    - NOTE: this command might take a few minutes.
    - Expected output is something like: `challenge information available at: http://localhost:4242/`
6. Ensure you get the problem details by browsing to the listed host and port. It should look like this:
    - ![Successful deploy](/img/sanity-download-playtest.png)



### Testing

Testing of problems involves at least 3 things:
  * Testing that an incorrect flag is incorrect
  * Testing that a correct flag is correct
  * Testing that the correct flag can be found by using the materials given for
    the problem.

1. To test an incorrect flag, try submitting `aaa` as a flag to the problem.
    - Expected output: `That is not the correct flag`
    
2. To test the correct flag and that the correct flag can be found using the 
   given materials, download the flag from the problem and submit it
    - Expected output: `Correct`



## Conclusion

With this walkthrough, we deployed a problem from the two most required files
in a cmgr problem, creating a sanity problem that just involves downloading the
flag.

We also demonstrated some basic testing practices by proving that an incorrect
flag is incorrect, a correct flag is correct, and that the player can get the
correct flag from the materials given.

This was the first tutorial in a series designed to familiarize challenge
authors with the new cmgr format for picoCTF problems. Other tutorials in this
series will demonstrate generating a dynamic flag, creating challenges for
each of the traditional CTF categories and more!

[Return to the index](/README.md#walkthroughs)

