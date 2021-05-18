# Sanity Problem Creation Walkthrough

This walkthrough will step you through what's needed to get a working sanity 
problem on a `cmgr` challenge server.

A sanity problem is one of the easiest problems in any CTF that is given as a
sanity check that your internet connection is working as intended, etc.



# Pre-requisites:

1. You have setup `cmgr`.
  - Refer to [the README](https://github.com/syreal17/start-problem-dev#setup)
    if this is not the case for you.



# Overview

We are going to create a "sanity check" problem, often refered to simply as
"sanity". This problem would be one of the easiest in the CTF and would act
as proof that at least your computer can talk to CTF web pages.

We're starting with the sanity problem with this walkthrough series because it
is one of the simplest real world challenges that exist in every CTF.

Using `cmgr`, the Sanity Download problem is just 2 files, 1. `problem.md`, 
and, 2. `Makefile`:

  1. `problem.md` specifies the name of the problem, the description, and other
      metadata about the problem.

  2. `Makefile` specifies the creation of the 'artifacts' or files associated
      with the problem, including the flag.
