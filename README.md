# Start Problem Development

Welcome! At the time of writing, this documentation is maintained by LT
'syreal' Jones. Feel free to reach out with questions, comments or 
suggestions [here](mailto:other@picoctf.org).



## Setup

- Install [Docker](https://docs.docker.com/engine/install/).
- Install [cmgr](https://github.com/picoCTF/cmgr/releases/latest).
  - There are pre-built binaries for Mac and Linux
  - For Windows, we recommend enabling and installing [WSL](https://learn.microsoft.com/en-us/windows/wsl/setup/environment), but if for some reason you want to run `cmgr` "natively" you can follow [these alternate instructions](/cmgr-native-windows.md) to build `cmgr` on Windows.
    - For WSL, we recommend using the default distro (Ubuntu).
    - Follow [these instructions](https://docs.docker.com/desktop/settings/windows/#wsl-integration) to ensure `cmgr` can talk to Docker.
    - Proceed with these instructions from within your Ubuntu machine.
      - Find and start the "Ubuntu" app using the start menu search
  - Download the appropriate archive and decompress.
    - Linux example commands:
    - `cd ~/Downloads`
    - `wget <url-of-release>` such as:
      - `wget https://github.com/picoCTF/cmgr/releases/download/v1.2.1/cmgr_linux_amd64.tar.gz`
    - `tar xzvf cmgr_linux_amd64.tar.gz`
  - Put `cmgr` and `cmgrd` in your path so they can be easily accessed on the command line.
    - `cp cmgr /usr/local/bin/`
    - `cp cmgrd /usr/local/bin/`
- Configure cmgr.
  - cmgr is configured using environment variables, see this [page](https://github.com/picoCTF/cmgr?tab=readme-ov-file#configuration) for more information.
  - In these next steps, we create directories to separate our cmgr challenges. cmgr will traverse all subdirectories looking for challenges or updated challenges. It's good practice to keep your working directory distinct from your deploy directory. Especially if you're working with multiple challenges, you must keep these challenges in a single, shared directory tree.
    - `sudo mkdir /challenges`
    - `sudo chown yourUser:yourUser /challenges`
    - `cd /challenges`
    - `mkdir cmgr`
    - `mkdir deploy`
    - `mkdir cmgr/artifacts`
  - Next, we set some cmgr enviroment variables in a persistent place.
    - `echo "export CMGR_DB='/challenges/cmgr/cmgr.db'" >> ~/.bashrc`
    - `echo "export CMGR_DIR='/challenges/deploy'" >> ~/.bashrc`
    - `echo "export CMGR_ARTIFACTS_DIR='/challenges/cmgr/artifacts'" >> ~/.bashrc`
    - `source ~/.bashrc` (Loads these changes to your current shell)
- Test cmgr.
  - `git clone git@github.com:picoCTF/start-problem-dev`
  - `cd start-problem-dev/example-problems/`
  - `cp -r forensics-grep/ /challenges/deploy/`
  - `cmgr update`
  - `cmgr playtest picoctf/examples/forensics-grep`
  - Once cmgr launches challenge, navigate to it with a browser



## Walkthroughs

These walkthroughs proceed roughly in order of complexity, from least complex
challenge to most complex challenge. These are great problems to start problem
development with.

1. [Sanity, static flag](/example-problems/sanity-static-flag/)
2. [Forensics Grep](/example-problems/forensics-grep/)
3. [Forensics Disk](/example-problems/forensics-disk/)
1. [Custom Service](/example-problems/custom-service/)
4. [Custom SSH (Multi-stage Dockerfile)](/example-problems/custom-ssh/)
5. [Custom Web](/example-problems/custom-web/)

In addition to these walkthroughs, you can also check the `cmgr` developers'
[example problems,](https://github.com/ArmyCyberInstitute/cmgr/tree/master/examples)
which are a good source for more complex problem development.



## Problem Developer Guidance

- Try to avoid excessive computational complexity in challenges, and/or limit bruteforceability (via PoW wrapper and provided solver binary, etc.)
- Also try to avoid challenges that require excessive client-side computation (especially for crypto challenges etc.), as some players will be using our webshell environment which has restricted CPU capacity and runtime limits
- Whenever possible, use templating so that challenge instances have unique flags (this should be possible except for certain types of forensics challenges)
   - If a challenge does have a static flag, please indicate this in the challenge files so that we can deploy only one instance
   - Add Templatable: no to the block immediately after the title in problem.md.
- When possible, try to make sure challenges are solvable via open-source command line tools and other web resources, as some users will only be able to use the webshell.
   - If a challenge requires an obscure command line tool to solve, let us know so that we can add it to the webshell
- If a challenge contains mutable state (such as an exploitable SQL database), please make this clear somewhere in the challenge files as we will need to deploy these as on-demand challenges
- For challenges that run an interactive script that users interact with via netcat, please don’t wait indefinitely for user input, in case users leave connections open
   - Add a timeout that exits the process if the user does not respond
   - Automatically exit the process after printing the flag
- For web challenges, make sure that it is not possible to read the flag via directory traversal
- Avoid writing files to disk due to user interaction with challenges (treat the filesystem as read-only if possible, keep temporary files in memory or at least make sure they always get removed)
- Please provide a commented solve script, or at least a walkthrough, explaining how the challenge is intended to be solved and what skills it is designed to teach
- When challenges use templating to have unique flags per-instance, make sure that the challenge is always solvable with a variety of generated flags (having a solve script is helpful for this)
- Use the standard picoCTF{} flag wrapper. Even if the flag must be displayed differently within the challenge due to technical limitations (e.g. can only return integers), make sure that this is clearly explained in the challenge description and that the standard wrapped form is the accepted flag
- Ensure that challenges’ Markdown descriptions render properly
- Do not make outbound Internet requests from challenges at runtime, as access will be blocked on our servers
- When writing custom Dockerfiles, reference base images by SHA to avoid drift
- For cmgr challenges, use challenge options to limit the challenge to the minimum necessary privileges/resources (we may make additional tweaks prior to deployment)
- Avoid situations where “correct looking” or red herring flags can be found - this causes customer support issues later on.
- Don’t include messages like “Flag file appears to be missing, please contact an admin!”. Operate under the assumption that the platform infrastructure is working correctly. These messages often lead to false reports from players running the challenge locally. In error cases like this, prefer a neutral message like “flag.txt not found in the current directory.”
- For web challenges, include all vendor external scripts, stylesheets, etc. needed at runtime into the challenge source. We want to make sure files remain available and that players can access everything needed for a challenge via picoCTF-controlled domains.
- Assume that challenges will not have outbound Internet access at runtime. (We may be able to make exceptions in specific cases.) Note that you can add another container to the challenge’s network to support exfiltrating data to another host.
- Challenges should not rely on externally-hosted services (such as third-party APIs) at runtime. We cannot guarantee that these services will remain accessible or compatible, which can lead to challenges breaking over time.

