# Web CSS Problem Creation Walkthrough

## Pre-requisites

1. You have `cmgr` installed and configured.
    - Refer to the [setup page](/setup-cmgr) if this is not the case for you.

1. You have done the [Forensics Disk
   Walkthrough](/example-problems/forensics-disk/).

## Overview

This is a fairly basic Web Exploitation problem. It uses an nginx Docker image
as a base to host a tiny website. The flag is hidden in the stylesheet used by
the index page. This is the first example problem to use Python to configure the
challenge.

## Walkthrough

### File Listing

1. [Dockerfile](/example-problems/web-css/Dockerfile). The only new aspect of
   this Dockerfile is the `EXPOSE` and `# PUBLISH` directives, and also using
   Python to configure the challenge instead of doing it with `RUN` commands in
   the Dockerfile directly. `EXPOSE` and `# PUBLISH` work in tandem in cmgr.
   `EXPOSE` is a Docker directive that makes a port accessible from outside a
   container. `# PUBLISH` lets this port be referenced in your `problem.md`.
   Please view the file directly to view more specific comments on its
   functionality.

1. [problem.md](/example-problems/web-css/problem.md). Note line 15. This is
   how we present our website to the player. Since we only publish one port in
   the Dockerfile, we can omit the port name in the "link_as" template function,
   see this
   [doc](https://github.com/picoCTF/cmgr/blob/master/examples/specification.md#details).
   This is actually the first time that "Challenge Options" will be used since
   the player interacts with a running container in this challenge.

1. [public-html](/example-problems/web-css/public-html) this directory holds
   all the files that our web server hosts.

1. [setup-challenge.py](/example-problems/web-css/setup-challenge.py) This
   script generates the flag and appends it to the end of the stylesheet as well
   as generating metadata.json that holds the flag's correct value. In previous
   challenges, this was done in the Dockerfile, but this example shows how to
   use Python instead, which opens up some doors to creativity.

### Python container configuration

In this example, we use Python to do some basic configuration of the challenge
container. Even for this basic configuration, using Python gives us some great
benefits. First, we can check our assumptions on the given FLAG variable. We can
check that it actually exists, and we can check that it has the standard format
we're expecting (includes a curly-braced section). For both of these scenarios,
our previous implementation of using sed in a Dockerfile will fail silently.

Python is also helpful for writing `metadata.json`. Even writing one line for
the flag is clunky using `echo` in the Dockerfile. Doing this is much cleaner
in Python, and necessary if we end up writing more variables than just the flag,
such as in this [config](/example-problems/general-ssh/config-builder.py#L70).

Everything that can be done in the Dockerfile, can be done in Python, though
usually more verbosely, but with better error handling and friendlier syntax.
Here's an [example](/example-problems/general-ssh/config-sshhost.py#L24) of
running an arbitrary shell command in Python.

## Conclusion

With this walkthrough, we demonstrated creating a simple web challenge using
nginx as a base image. This allowed us to use custom HTML and CSS very simply in
order to hide the flag in one of these files. We used Python to configure this
container which leads to a cleaner implementation.

[Next problem](/example-problems/reversing-python)

[Return to the index](/example-problems#example-problems)
