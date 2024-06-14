# Sanity

This guide will walk you through the necessary steps to set up and validate a
sanity problem with `cmgr`.

A sanity problem is a straightforward task used in Capture the Flag (CTF)
competitions. It serves as a preliminary check to ensure that your internet
connection is stable and all other system assumptions are correctly configured.

This sanity challenge is a simple download of the flag in the file `flag.txt`.

## Pre-requisites

1. You have `cmgr` installed.
    - Refer to the [setup page](/setup-cmgr.md) if this is not the
      case for you.

## Overview

We're starting with a sanity problem because it is the simplest challenge that
exists in every CTF. We will demonstrate creating a very simple Docker container
that just copies in `flag.txt` and makes it a downloadable artifact for cmgr and
sets the flag for the challenge appropriately.

The following walkthough has 3 parts:

1. File listing. We will go over every file in the challenge directory.

2. Deployment. We will demonstrate deploying this challenge for testing.

3. Testing. We will demonstrate a good place to start with testing any challenge

### File Listing

  1. [Dockerfile](/example-problems/sanity-static-flag/Dockerfile) builds the
      container used for the challenge. A container is required for every
      challenge with cmgr. This file is heavily commented to explain what each
      Docker command does. Please refer to the file itself for further
      explanation.
  1. [problem.md](/example-problems/sanity-static-flag/problem.md) specifies the
      name of the problem, the description, and other metadata about the
      problem. Though this is a Markdown file, it is actually parsed by cmgr.
      Here is the
      [specification](https://github.com/picoCTF/cmgr/blob/master/examples/specification.md)
      for this file in general. We will go over some specifics here:
        - The first heading is the name of your problem as it will appear on the
          platform.
        - The first block contains important cmgr metadata and some
          problem-specific values.
            - `Namespace` this is the namespace in cmgr that your problem will
              be named under. Please use: `Namespace: picoctf`
            - `ID` this is the actual name of the problem for cmgr. If not
              specified, it will be the first heading converted to all lowercase
              and hyphens, but we like to specify it directly.
            - `Type` this should always be `Type: custom`
            - `Category` this should probably be "General Skills," "Forensics,"
              "Reverse Engineering," "Cryptography," "Binary Exploitation," or
              "Web Exploitation" but we might entertain other categories in the
              future.
            - `Points` this should be `Points: 1`. We won't know the points for
              any given challenge until we can calibrate them with the rest of
              the challenges in a competition.
            - `Templatable` this is a bookkeeping value which indicates whether
              a challenge has a static or dynamic flag. We try to keep as many
              flags dynamic as possible as it helps us catch cheaters and allows
              us to regenerate the instance flags if we need.
        - The `Solution Overview` is technically optional but we rely heavily on
          it to determine difficulty, and to verify working instances so please
          include it in reasonable detail.
        - The `Learning Objective` is also optional but is very useful to us as
          a one sentence statement about what a challenge aims to teach.
  1. [flag.txt](/example-problems/sanity-static-flag/flag.txt) this is what
     everyone is trying to get! We pass it into our container, and it creates a
     tarball out of it called `artifacts.tar.gz` which cmgr looks for so it can
     provide links in the Description or Details of problem.md.
  1. [.dockerignore](/example-problems/sanity-static-flag/.dockerignore) this
     lets us do `COPY . /app` in the Dockerfile and just copy `flag.txt`. We
     could've just done `COPY ./flag.txt /app` for this challenge, but if we
     have more challenge files the first method can be easier.

### Deployment

Follow [these steps](/setup-cmgr.md#test-cmgr) to deploy the sanity check
problem.

### Testing

Testing of problems involves at least 3 things:

- Testing that an incorrect flag is incorrect
- Testing that a correct flag is correct
- Testing that the correct flag can be found by using the materials given for
  the problem.

1. To test an incorrect flag, try submitting `aaa` as a flag to the problem.
    - Expected output: `That is not the correct flag`
2. To test the correct flag and that the correct flag can be found using the
   given materials, download the flag from the problem and submit it
    - Expected output: `Correct`

These steps ensure that `/challenge/metadata.json` was created correctly. This
is just basic, functional testing of your problem. A lot of testing  goes into
appropriately adjusting the difficulty of a problem and making it challenging
enough to be interesting, but still accessible.

## Conclusion

With this guide, we saw everything that goes into creating a simple sanity
problem. Besides the challenge files, the Dockerfile and problem.md are the most
important files.

We also demonstrated some basic testing practices by proving that an incorrect
flag is incorrect, a correct flag is correct, and that the player can get the
correct flag from the materials given.

This is the simplest challenge in a series designed to familiarize new authors
with the cmgr format for picoCTF problems. Other guides here will demonstrate
generating a dynamic flag, creating challenges for other traditional CTF
categories and more!

Check out [forensics grep](/example-problems/forensics-grep/) to learn how to
create and use dynamic flags!
