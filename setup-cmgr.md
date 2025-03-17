# Install and Setup cmgr

## Install [Docker Desktop](https://docs.docker.com/engine/install/)

- If you're running a supported distro of Linux, you may want to install
  [Docker Engine](https://docs.docker.com/engine/install/#supported-platforms)
  instead of Docker Desktop for just command-line tools.

## Install [cmgr](https://github.com/picoCTF/cmgr/releases/latest)

- There are pre-built binaries for Mac and Linux
- For Windows, we recommend enabling and installing
  [WSL](https://learn.microsoft.com/en-us/windows/wsl/setup/environment) and
  using the Linux pre-built binaries.
  - For WSL, we recommend using the default distro (Ubuntu).
  - If you can't run `docker` within WSL Ubuntu, follow [these
    instructions](https://docs.docker.com/desktop/settings/windows/#wsl-integration).
  - Proceed with the following instructions from within your Ubuntu machine.
    - Find and start the "Ubuntu" app using the start menu search
- Download the appropriate archive and decompress
  - Linux example commands:
  - `$ cd ~/Downloads`
  - `$ wget <url-of-release-tarball>` such as:
    - `$ wget https://github.com/picoCTF/cmgr/releases/download/v1.2.1/cmgr_linux_amd64.tar.gz`
  - `$ tar xzvf cmgr_linux_amd64.tar.gz`
  - Make sure the binaries run:
    - `$ ./cmgr`
    - Should print cmgr help text. If it prints exec format error, you'll need to pick a
      different tarball from the [cmgr release page](https://github.com/picoCTF/cmgr/releases/latest)
- Put `cmgr` in your path so it can be easily accessed on the command line
  - `$ mkdir ~/cmgr`
  - `$ mkdir ~/cmgr/bin`
  - `$ cp cmgr ~/cmgr/bin/`
  - Add `~/cmgr/bin/` to your path in a shell setup script
    - Example Linux command:
      - `$ echo "export PATH='$PATH:$HOME/cmgr/bin'" >> ~/.bashrc`
    - To make these changes apply to your current shell:
      - `$ source ~/.bashrc`
    - If you're on a recent version of Mac, you may need to add this
      configuration to `~/.zshrc` instead of `~/.bashrc`

## Configure cmgr

- cmgr is configured using environment variables, see this
  [page](https://github.com/picoCTF/cmgr?tab=readme-ov-file#configuration) for
  more information.
- In these next steps, we create directories to separate our cmgr challenges.
  cmgr will traverse all subdirectories looking for challenges or updated
  challenges. It's good practice to keep your working directory distinct from
  your deploy directory. We want our deploy directory to be like a practice
  for production, and usually a working directory for a CTF challenge will
  have many files that you don't want to include in the deployment. Especially
  if you're working with multiple challenges, you must keep these challenges
  in a single, shared directory tree.
  - `$ mkdir ~/cmgr/challenges`
  - `$ mkdir ~/cmgr/artifacts`
- Next, we set some cmgr enviroment variables in a persistent place
  - `$ echo "export CMGR_DB=~/cmgr/cmgr.db" >> ~/.bashrc`
    - This file is cmgr's SQLite database. It contains everything cmgr knows
      about your challenges. If cmgr gets in a bad state, you can delete this
      file to *hard* reset cmgr.
  - `$ echo "export CMGR_DIR=~/cmgr/challenges" >> ~/.bashrc`
    - This is where you'll put all your challenges, in separate directories.
  - `$ echo "export CMGR_ARTIFACTS_DIR=~/cmgr/artifacts" >> ~/.bashrc`
    - This is mostly behind the scenes, but this is where cmgr saves each
      challenge's artifacts.tar.gz, renamed with the cmgr ID of the challenge.
  - `$ source ~/.bashrc` (Loads these changes to your current shell)

## Test cmgr

- `$ mkdir ~/examples`
- `$ cd ~/examples`
- `$ git clone https://github.com/picoCTF/start-problem-dev.git`
- `$ cd start-problem-dev/example-problems/`
- `$ cp -r sanity-static-flag/ ~/cmgr/challenges/`
- `$ cmgr update`
  - Expected output:

      ```terminal
      Added:
          picoctf/examples/sanity-download
      ```

- `$ cmgr playtest picoctf/examples/sanity-download`
  - This might take a few minutes, it's building a container.
  - Expected output:

      ```terminal
      cmgr: [WARN:  disk quota for picoctf/examples/sanity-download container 'challenge' ignored (disk quotas are not enabled)]
      challenge information available at: http://localhost:4242/
      ```

- Once cmgr launches the challenge, navigate to `http://localhost:4242/` with
  a browser
  - Expected output:

    ![Sanity playtest page](/img/sanity-download-playtest.png)
