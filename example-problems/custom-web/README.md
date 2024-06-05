# Custom Web Problem Creation Walkthrough

## Pre-requisites

1. You have `cmgr` installed and configured.
    - Refer to the [setup page](/setup-cmgr.md) if this is not the case for you.

2. You have done the [Sanity Problem Creation
   Walkthrough](/example-problems/sanity-static-flag/README.md). You do not have
   to do every walkthrough that is listed as easier than this one, but you must
   at least do the Sanity Problem Creation Walkthrough. This walkthrough is
   presented as a set of changes from the sanity problem. The sanity problem
   walkthrough is the core of cmgr challenges, and this problem presents what
   must be added on top of that for a more complicated challenge.

## Overview

This problem demonstrates using a custom problem type for a web challenge.
There are a handful of prefabricated means of writing a web challenge, but
none of these allow us to put the flag in a CSS file. Writing our own
Dockerfile for this web challenge gives us much more freedom to work, but
relinquishes the ease of just using one of the prefab web challenge types.
Since we want to put the flag in a CSS file, using the custom problem type is
recommended.

## Walkthrough

### File Listing

1. Besides problem details, the most important change in
   [problem.md](/example-problems/custom-web/problem.md) is changing Type to
   "custom".

2. [public-html](/example-problems/custom-web/public-html) this directory holds
   all the files that our web server hosts.

3. [config-box.py](/example-problems/custom-web/config-box.py) This script
   generates the flag and appends it to the end of the stylesheet as well as
   generating metadata.json that holds the flag's correct value.

4. [Dockerfile](/example-problems/custom-web/Dockerfile) this file is quite
   involved as it pulls a linux image with Apache, updates the container,
   installs addtional packages and runs the config-box.py Python script to
   ready the container to be the Custom Web challenge. Please view the file
   directly to view more specific comments on its functionality.

### Other helpful references

We aren't going to go to any more depths in this tutorial, but for typical
problem playtest deployment and testing strategy, see [this
section](/example-problems/sanity-static-flag#Deployment) and for debugging
your Dockerfile, see [this section](/example-problems/custom-ssh#debugging-your-dockerfile).

## Conclusion

With this walkthrough, we demonstrated creating a web challenge without using
a web challenge type. By using the custom challenge type instead, this let us
have more freedom in where to put the flag, but required developing a
Dockerfile that spun up a web server.

[Return to the index](/README.md#walkthroughs)
