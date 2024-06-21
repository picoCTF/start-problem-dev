# Grep Problem Creation Walkthrough

## Pre-requisites

1. You have `cmgr` installed and configured.
    - Refer to the [setup page](/setup-cmgr.md) if this is not the case for you.

2. You have reviewed the [Sanity
   problem](/example-problems/sanity-static-flag/). This problem is presented as
   a set of changes from the sanity problem. The sanity problem walkthrough is
   the core of cmgr challenges, and this problem presents what must be added on
   top of that for a more sophisticated challenge.

## Overview

This problem is the perennial grep problem. We had a problem like this almost
every year before the Gym. It is different from Sanity because though it is
still simple, it does teach a computer skill: using grep.

There are 3 main changes in this problem that make it more interesting:

1. The addition of 2 new files: war-and-peace.txt, and byteblast.py.

1. Problem is marked as Templatable in problem.md. This means that multiple
   instances of this problem can be ran, each having a different flag. This is
   just a bookkeeping value.

1. All the mechanics of being Templatable (also referred to as having a dynamic
   flag) flag happen in the Dockerfile which we will go over in more detail
   during the File Listing below.

By these changes we go from giving the flag out to anyone who can download it
to hiding it deep within a large classic novel.

## Walkthrough

### File Listing

1. [Dockerfile](/example-problems/forensics-grep/Dockerfile). There are a few
   differences between this file and the
   [Dockerfile](/example-problems/sanity-static-flag/Dockerfile) for Sanity.
   - Right away, we're actually using a different base image for the container
     (python vs. ubuntu). Using this python image gives us Python in a Debian
     environment. If we had used ubuntu instead, we would've needed to `apt-get
     install` python. That's really not a big deal either way. This problem
     demonstrates how to minimize your docker commands, but
     [forensics-disk](/example-problems/forensics-disk/) demonstrates how to
     properly use `apt-get` for an ubuntu image.
   - Line 15 is how we start to create our dynamic flag. cmgr passes in a few
     build arguments to Docker. We ignore `SEED` and `FLAG_FORMAT`, but bring in
     `FLAG`. FLAG by default looks something like this: `flag{abcd1234}`. Where
     `abcd1234` is a string of random hex digits crafted specifically for the
     challenge instance. In the first step of our next Docker command, we
     replace the default flag prefix with our own 'picoCTF' prefix, plus a
     leetspeak phrase that relates to the challenge. Our flag is now
     `picoCTF{gr3p_15_4_5up3rp0w3r_abcd1234}` and we write this to `flag.txt`.
     In the next command, we create a copy of `war-and-peace.txt` to insert the
     flag into. Finally, we use our byteblast.py script to insert the flag into
     `war-and-peace.flag.txt` at an offset of 49998 bytes. This offset value was
     selected so that the flag would be at the start of a line and not inserted
     into the middle of a word which might be confusing.

1. There's not much new in
   [problem.md](/example-problems/forensics-grep/problem.md). The only major
   difference between this problem.md and the static sanity's problem.md is that
   we specify that this problem is Templatable [in this
   section](/example-problems/forensics-grep/problem.md#forensics-grep). This
   means that multiple instances of this problem can be ran and each will have a
   different flag. Having multiple instances of the same problem gives many
   benefits. Most importantly for problem developers, it means we can detect
   cheating and regenerate flags on the fly.

1. [war-and-peace.txt](/example-problems/forensics-grep/war-and-peace.txt) is
   just a large, public domain, literary work that assures the CTF player needs
   to use grep or some other finding tool in order to get the flag. The file is
   66,000 lines long, so it accomplishes this purpose well!

1. [byteblast.py](/example-problems/forensics-grep/byteblast.py) is a script
   that I use in many problems that can insert bytes at arbitrary points in a
   file. This comes in hand for inserting templated flags in artifacts
   programmatically at build-time.

### Testing Build Templating

For typical problem playtest deployment and testing strategy, see
[this section](/example-problems/sanity-static-flag#Deployment) in the Static
Sanity Walkthrough. The section in this walkthrough is going to demonstrate
obtaining proof that two different instances of the same challenge have
different flags.

1. Clone this repo.
1. `$ cd start-problem-dev/example-problems`
1. Update cmgr with the grep problem:
    - `$ cmgr update forensics-grep/`
1. Ensure problem appears in cmgr list:
    - `$ cmgr list`
    - Expected output should include: `syreal/examples/forensics-grep`
1. Build two instances of the problem:
    - `cmgr build syreal/examples/forensics-grep 9001 9002`
    - This builds two instances of the grep problem. One is seeded with 9001
      and the other is seeded with 9002.
    - Expected output:

      ```terminal
      Build IDs:
      1
      2
      ```

1. Dump build info and verify flags are different for each build:
    - `cmgr system-dump --json | grep \"flag\"`
    - Expected output:

      ```terminal
      "flag": "flag{gr3p_15_4_5up3rp0w3r_72dce069}",
      "flag": "flag{gr3p_15_4_5up3rp0w3r_5f54c69e}",
      ```

## Conclusion

With this walkthrough, we created a classic problem that teaches the player
about `grep`. Attempting to solve this problem manually is ill-advised, but it
can be quickly solved using a finding tool.

The Makefile of this problem is a bit more complex than the sanity check
problem. It takes the flag and incorporates it into a large text, making it
necessary to use a tool to efficiently solve this problem. We used a helper
script of mine that I call 'byteblast'. This script can overwrite bytes of the
file with the flag at arbitrary offsets. This script is useful (especially
for forensics problems) but somewhat overpowered and should be used with
caution.

We needed a programmatic way to write the flag in our large file because the
flag is templated and therefore different for each build of our problem.
Finally, we used some cmgr commands to build our problem twice and dump the
JSON information about each build to verify that the flags were different.

This is the first walkthrough (in order of ascending difficulty) in the cmgr
series to teach the player about a tool and technique. The rest of the
walkthroughs in this series will continue teaching the player about more and
more advanced computer science and security practices.

[Return to the index](/README.md#walkthroughs)
