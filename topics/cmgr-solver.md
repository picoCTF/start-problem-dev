# cmgr solver

## Writing your solver

cmgr has built in functionality to automatically test your challenges. It will
run a solve script on an adjacent container and make sure the flag found is the
flag expected. All you have to do is create a directory in the problem source
folder called `solver` and create a Python program called `solve.py` in that
directory.

The cmgr docs on the solvers are [at this
page](https://github.com/picoCTF/cmgr/blob/master/examples/solvers.md) and in
this [section](https://github.com/picoCTF/cmgr/tree/master?tab=readme-ov-file#challenges). A custom Dockerfile can be used for the solver
container as well, but so far, we've just used the default Dockerfile, found
[here](https://github.com/picoCTF/cmgr/blob/master/cmgr/dockerfiles/solver.Dockerfile).

First thing to know is that every challenge artifact is copied into our working
directory and is thus available to `solve.py`.
[Here](/example-problems/sanity-static-flag/solver/solve.py#L4) I access the
`flag.txt` challenge artifact from the solve script. Then I write the flag I
found to `flag`. This is the file the checker tests to make sure it matches the
expected flag.

Also available in the working directory of the solver is a file called
`metadata.json` which doesn't have the flag in it, but has every other instanced
value in it. We use this file to get the SSH password in [this solve script](/example-problems/general-ssh/solver/solve.py#L9).

To use `pwntools` with the typical `from pwn import *` import line, you must list the package in a `requirements.txt` in the `solver/` directory.

`solve.py` is ran from a container adjacent to the challenge container(s). If we
need to talk to the challenge containers we can use their Dockerfile stage names
as DNS names on the docker network. See this [line](/example-problems/web-css/solver/solve.py#L6). That DNS name comes from the [Dockerfile here](/example-problems/web-css/Dockerfile#L22).

Your solver doesn't have to solve the problem in the way a player would.
Sometimes like in [this
solver](/example-problems/forensics-disk/solver/solve.py#L9), we sort of cheat
to get the flag. The point of a solve script is to prove that a challenge is
solvable given the challenge artifacts. More testing is required to make sure
the solution is reasonable (read "not guessy").

## Using your solver

To use your solver, copy your problem to your cmgr directory:

```terminal
$ cp -r sanity-static-flag/ $CMGR_DIR/
$ cmgr test $CMGR_DIR/sanity-static-flag/
```

Unfortunately, what you're hoping for is no output. That means that your solver
got the right flag, but no output also happens when you don't have a solver. If
`solver/solve.py` exists in your problem source, then it would give an error if
the flags didn't match, but if you want to be sure that your solver is running,
you can add a bogus string to your `flag` file and force some output.

## Conclusion

Every example problem has a solver. Please feel free to explore. We've made an
attempt to draw out the most interesting features of solvers here, but we're
always innovating on problems, so we always need to innovate with solvers!
