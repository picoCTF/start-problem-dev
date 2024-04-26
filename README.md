# Start Problem Development

Welcome! At the time of writing, this documentation is maintained by Luke
'syreal' Jones. Feel free to reach out with questions, comments or suggestions
[here](mailto:other@picoctf.org).

## Setup

- Install [Docker Desktop](https://docs.docker.com/engine/install/).
  - If you're running a supported distro of Linux, you may want to install
    [Docker Engine](https://docs.docker.com/engine/install/#supported-platforms)
    instead of Docker Desktop for just command-line tools.
- Install [cmgr](https://github.com/picoCTF/cmgr/releases/latest).
  - There are pre-built binaries for Mac and Linux
  - For Windows, we recommend enabling and installing
    [WSL](https://learn.microsoft.com/en-us/windows/wsl/setup/environment) and
    using the Linux pre-built binaries.
    - For WSL, We recommend using the default distro (Ubuntu).
    - If you can't run `docker` within WSL Ubuntu, follow [these
      instructions](https://docs.docker.com/desktop/settings/windows/#wsl-integration).
    - Proceed with these instructions from within your Ubuntu machine.
      - Find and start the "Ubuntu" app using the start menu search
  - Download the appropriate archive and decompress.
    - Linux example commands:
    - `$ cd ~/Downloads`
    - `$ wget <url-of-release-tarball>` such as:
      - `$ wget https://github.com/picoCTF/cmgr/releases/download/v1.2.1/cmgr_linux_amd64.tar.gz`
    - `$ tar xzvf cmgr_linux_amd64.tar.gz`
  - Put `cmgr` and `cmgrd` in your path so they can be easily accessed on the
    command line.
    - `$ sudo cp cmgr /usr/local/bin/`
    - `$ sudo cp cmgrd /usr/local/bin/`
- Configure cmgr.
  - cmgr is configured using environment variables, see this
    [page](https://github.com/picoCTF/cmgr?tab=readme-ov-file#configuration) for
    more information.
  - In these next steps, we create directories to separate our cmgr challenges.
    cmgr will traverse all subdirectories looking for challenges or updated
    challenges. It's good practice to keep your working directory distinct from
    your deploy directory. Especially if you're working with multiple
    challenges, you must keep these challenges in a single, shared directory
    tree.
    - `$ mkdir ~/challenges`
    - `$ cd ~/challenges`
    - `$ mkdir cmgr`
    - `$ mkdir deploy`
    - `$ mkdir cmgr/artifacts`
  - Next, we set some cmgr enviroment variables in a persistent place.
    - `$ echo "export CMGR_DB='/challenges/cmgr/cmgr.db'" >> ~/.bashrc`
      - This file is cmgr's SQLite database. It contains everything cmgr knows
        about your challenges. If cmgr gets in a bad state, you can delete this
        file to *hard* reset cmgr.
    - `$ echo "export CMGR_DIR='/challenges/deploy'" >> ~/.bashrc`
      - This is where you'll put all your challenges, in separate directories.
    - `$ echo "export CMGR_ARTIFACTS_DIR='/challenges/cmgr/artifacts'" >>
      ~/.bashrc`
      - This is mostly behind the scenes, but this is where cmgr saves each
        challenge's artifacts.tar.gz, renamed with the cmgr ID of the challenge.
    - `$ source ~/.bashrc` (Loads these changes to your current shell)
- Test cmgr.
  - `$ mkdir ~/examples`
  - `$ cd ~/examples`
  - `$ git clone https://github.com/picoCTF/start-problem-dev.git`
  - `$ cd start-problem-dev/example-problems/`
  - `$ cp -r sanity-static-flag/ ~/challenges/deploy/`
  - `$ cmgr update`
  - `$ cmgr playtest picoctf/examples/sanity-download`
  - Once cmgr launches challenge, navigate to `http://localhost:4242/` with a
    browser

## Walkthroughs

These walkthroughs proceed roughly in order of complexity, from least complex
challenge to most complex challenge. These are great problems to start problem
development with.

1. [Sanity, static flag](/example-problems/sanity-static-flag/)
2. [Forensics Grep](/example-problems/forensics-grep/)
3. [Forensics Disk](/example-problems/forensics-disk/)
4. [Custom Service](/example-problems/custom-service/)
5. [Custom SSH (Multi-stage Dockerfile)](/example-problems/custom-ssh/)
6. [Custom Web](/example-problems/custom-web/)

In addition to these walkthroughs, you can also check the `cmgr` developers'
[example
problems,](https://github.com/ArmyCyberInstitute/cmgr/tree/master/examples)
which are a good source for more complex problem development.

## Problem Developer Guidance

### General Challenge Design

- Make challenges about security concepts that were fun to learn about, powerful
  in practice, or requiring cleverness to execute
- Difficulty is a fine-tuning process that can happen after you have a
  functional prototype
  - Guessing should not be a part of the difficulty. This isn't [National
    Treasure](https://www.youtube.com/watch?v=Wc3Q7tBS8Gc)
- Consider whether your problem is more pedagogical or more novel
  - More pedagogical problems are more towards 100 and 200 points
  - More novel problems are more towards 400 and 500 points
- Pedagogical problems should be solvable with the webshell
- It's ok if 400/500 point problems cannot be solved reasonably within the
  webshell, but it's really cool if they can!
- Avoid situations where “correct looking” or red herring flags can be found -
  this causes customer support issues later on.

### General Technical Concerns

- Please provide a commented solve script, or at least a walkthrough, explaining
  how the challenge is intended to be solved and what skills it is designed to
  teach
- Use the standard picoCTF{} flag wrapper. Even if the flag must be displayed
  differently within the challenge due to technical limitations (e.g. can only
  return integers), make sure that this is clearly explained in the challenge
  description and that the standard wrapped form is the accepted flag
  - See the [C3](https://play.picoctf.org/practice/challenge/407) challenge.
- Whenever possible, use templating so that challenge instances have unique
  flags (this should be possible except for certain types of forensics
  challenges)
  - If a challenge does have a static flag, please indicate this in the
    challenge files so that we can deploy only one instance
  - Add `Templatable: no` to the block immediately after the title in problem.md
    - [Example](https://github.com/picoCTF/start-problem-dev/blob/master/example-problems/sanity-static-flag/problem.md?plain=1#L7)
  - This is how the majority of our cheating detection functions
  - We typically make different instances of a problem by using the randomly
    generated string in the cmgr provided flag, see [this
    source](https://github.com/picoCTF/challenges/blob/main/cmgr/picoctf-2024/Reverse%20Engineering/classic-crackme-0x100/config-box.py#L14)
- When challenges use templating to have unique flags per-instance, make sure
  that the challenge is always solvable with a variety of generated flags
  (having a solve script is helpful for this)
- Ensure that challenges’ Markdown descriptions render properly
- For cmgr challenges, use challenge options to limit the challenge to the
  minimum necessary privileges/resources (we may make additional tweaks prior to
  deployment)
  - See this
    [problem.md](https://github.com/picoCTF/start-problem-dev/blob/master/example-problems/sanity-static-flag/problem.md?plain=1#L24)
- When writing custom Dockerfiles, reference base images by SHA to avoid drift
  - See this
    [Dockerfile](https://github.com/picoCTF/start-problem-dev/blob/master/example-problems/custom-service/Dockerfile#L1)

### Challenge Accessibility

- When possible, try to make sure challenges are solvable via open-source
  command line tools and other web resources, as some users will only be able to
  use the webshell
  - If a challenge requires an obscure command line tool to solve, let us know
    so that we can add it to the webshell
  - Our users with the most potential to learn use the webshell
  - Some previous winners have also used the webshell for certain problems
- Also try to avoid challenges that require excessive client-side computation
  (especially for crypto challenges etc.), as some players will be using our
  webshell environment which has restricted CPU capacity and runtime limits

### Challenge Interactivity

- Try to avoid excessive computational complexity in challenges, and/or limit
  bruteforceability (via PoW wrapper and provided solver binary, etc.)
  - The [Virtual Machine 1](https://play.picoctf.org/practice/challenge/386)
    challenge would be vulnerable to bruteforce if there wasn't heavy
    rate-limiting and variability of the requested output
- If a challenge contains mutable state (such as an exploitable SQL database),
  please make this clear somewhere in the challenge files as we will need to
  deploy these as on-demand challenges
- For challenges that run an interactive script that users interact with via
  netcat, please don’t wait indefinitely for user input, in case users leave
  connections open
  - Add a timeout that exits the process if the user does not respond
  - Automatically exit the process after printing the flag
- If a C program uses `scanf` make sure it handles EOF appropriately, see [this
  source](https://github.com/picoCTF/challenges/blob/main/cmgr/picoctf-2024/Binary%20Exploitation/heap-1/chall.c#L88)
- Avoid writing files to disk due to user interaction with challenges (treat the
  filesystem as read-only if possible, keep temporary files in memory or at
  least make sure they always get removed)
- Don’t include messages like “Flag file appears to be missing, please contact
  an admin!”. Operate under the assumption that the platform infrastructure is
  working correctly. These messages often lead to false reports from players
  running the challenge locally. In error cases like this, prefer a neutral
  message like “flag.txt not found in the current directory.”

### Web and Web Challenges

- For web challenges, make sure that it is not possible to read the flag via
  directory traversal
- For web challenges, include all vendor external scripts, stylesheets, etc.
  needed at runtime into the challenge source. We want to make sure files remain
  available and that players can access everything needed for a challenge via
  picoCTF-controlled domains.
- Do not make outbound Internet requests from challenges at runtime, as access
  will be blocked on our servers
- Assume that challenges will not have outbound Internet access at runtime. (We
  may be able to make exceptions in specific cases.) Note that you can add
  another container to the challenge’s network to support exfiltrating data to
  another host.
- Challenges should not rely on externally-hosted services (such as third-party
  APIs) at runtime. We cannot guarantee that these services will remain
  accessible or compatible, which can lead to challenges breaking over time.
