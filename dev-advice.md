# Problem Developer Guidance

## General Challenge Design

- Make challenges about security concepts that were fun to learn about, powerful
  in practice, or required cleverness to execute
- Difficulty is a fine-tuning process that can happen after you have a
  functional prototype
  - Guessing should not be a part of the difficulty. This isn't [National
    Treasure](https://www.youtube.com/watch?v=Wc3Q7tBS8Gc)
- Consider whether your problem is more pedagogical or more novel
  - More pedagogical problems are more towards 100 and 200 points
    - Such as the [Time
      Machine](https://play.picoctf.org/practice/challenge/425) problem
  - More novel problems are more towards 400 and 500 points
    - Such as the
      [high-frequency-troubles](https://play.picoctf.org/practice/challenge/441)
      problem
- Pedagogical problems should be solvable with the webshell
- It's ok if 400/500 point problems cannot be solved reasonably within the
  webshell, but it's really cool if they can!
- Avoid situations where “correct looking” or red herring flags can be found -
  this causes customer support issues later on
- Please provide a commented solve script, or at least a walkthrough, explaining
  how the challenge is intended to be solved and what skills it is designed to
  teach

## General Technical Concerns

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

## Challenge Accessibility

- When possible, try to make sure challenges are solvable via open-source
  command line tools and other web resources, as some users will only be able to
  use the webshell
  - If a challenge requires an obscure command line tool to solve, let us know
    so that we can add it to the webshell
  - Most users playing from school only have the webshell
  - Some previous winners have also used the webshell for certain problems
- Also try to avoid challenges that require excessive client-side computation
  (especially for crypto challenges etc.), as some players will be using our
  webshell environment which has restricted CPU capacity and runtime limits

## Challenge Interactivity

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
    - See [this source](https://github.com/picoCTF/challenges/blob/main/cmgr/2022-beginner-picomini/hashingjopapp/hashingjobapp.py#L47)
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

## Web

- For web challenges, make sure that it is not possible to read the flag via
  directory traversal
  - Unless that's the intention, like with [this
    problem](https://play.picoctf.org/practice/challenge/270)
- For web challenges, include all vendor external scripts, stylesheets, etc.
  needed at runtime into the challenge source. We want to make sure files remain
  available and that players can access everything needed for a challenge via
  picoCTF-controlled domains
- Do not make outbound Internet requests from challenges at runtime, as access
  will be blocked on our servers
- Assume that challenges will not have outbound Internet access at runtime. (We
  may be able to make exceptions in specific cases.) Note that you can add
  another container to the challenge’s network to support exfiltrating data to
  another host
- Challenges should not rely on externally-hosted services (such as third-party
  APIs) at runtime. We cannot guarantee that these services will remain
  accessible or compatible, which can lead to challenges breaking over time
