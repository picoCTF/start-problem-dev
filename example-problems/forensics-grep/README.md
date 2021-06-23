# Grep Problem Creation Walkthrough


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

This problem is the perennial grep problem. We have a problem like this almost
every year. It is different from Sanity because though it is still simple, it
does teach a computer skill: using grep.

There are 3 main changes in this problem that make it more interesting:

1. The addition of 3 new files: packages.txt, war-and-peace.txt, and 
   byteblast.py.

2. Makefile has more targets.

3. Problem is marked as Templatable in problem.md. This means that multiple
   instances of this problem can be ran, each having a different flag.

By these changes we go from giving the flag out to anyone who can download it
to hiding it deep within a large classic novel.



## Walkthrough


### File Listing

1. There's not much new in 
   [problem.md](/example-problems/forensics-grep/problem.md). The only major
   difference between this problem.md and the static sanity's problem.md is
   that we specify that this problem is Templatable
   [in this section](/example-problems/forensics-grep/problem.md#forensics-grep).
   This means that multiple instances of this problem can be ran and each will
   have a different flag. Having multiple instances of the same problem gives
   many benefits. Most importantly for problem developers, it means we can
   detect cheating and regenerate flags on the fly.
   
2. There's a bit more new in 
   [Makefile](/example-problems/forensics-grep/Makefile). Since we are not just
   immediately handing over the flag like in the sanity problem, we create a
   target for a challenge artifact that contains the flag, namely 
   `war-and-peace.flag.txt`. This file is `war-and-peace.txt` with the flag
   inserted in it 50,000 bytes into the file, which ends up only being roughly
   1,600 lines in.
   
3. [war-and-peace.txt](/example-problems/forensics-grep/war-and-peace.txt) is
   just a large, public domain, literary work that assures the CTF player needs
   to use grep or some other finding tool in order to get the flag. The file is
   66,000 lines long, so it accomplishes this purpose well!
   
4. [packages.txt](/example-problems/forensics-grep/packages.txt) is a list of
   packages that the cmgr build environment must install for problem creation
   to work. For this grep problem, we only need `python3` in order for this
   problem to build correctly.
   
5. [byteblast.py](/example-problems/forensics-grep/byteblast.py) is a script
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
2. `$ cd start-problem-dev/example-problems`
3. Update cmgr with the grep problem:
    - `$ cmgr update forensics-grep/`
4. Ensure problem appears in cmgr list:
    - `$ cmgr list`
    - Expected output should include: `syreal/examples/forensics-grep`
5. Build two instances of the problem:
    - `cmgr build syreal/examples/forensics-grep 9001 9002`
    - This builds two instances of the grep problem. One is seeded with 9001
      and the other is seeded with 9002.
    - Expected output:
```
Build IDs:
    1
    2
```
6. Dump build info and verify flags are different for each build:
    - `cmgr system-dump --json | grep \"flag\"`
    - Expected output:
```
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

[Return to the index](/)

