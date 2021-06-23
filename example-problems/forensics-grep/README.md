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
   that we specify that this problem is Templatable on 
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
   

### Deployment

### Testing

## Conclusion

