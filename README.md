# Start picoCTF Problem Development

Hello and welcome to the official documentation for our Capture-The-Flag (CTF)
challenge manager! This guide is designed to help you navigate and utilize the
features of this powerful tool to create and configure your own CTF problems.

This documentation is currently maintained by Luke 'syreal' Jones. If you have
any questions, comments, or suggestions, feel free to reach out via email
[here](mailto:other@picoctf.org).

Our team has been exclusively using
[cmgr](https://github.com/picoCTF/cmgr/releases/latest) for problem development
over the past few years. This tool is tightly integrated with Docker, ensuring a
robust and flexible environment for your CTF challenges. With cmgr, you can
easily bring your challenge ideas to life and provide an engaging experience for
participants.

Whether you are a seasoned CTF organizer or new to the scene, this documentation
will guide you through every step of using cmgr, from installation and setup to
advanced customization and challenge configuration.

Let's get started on turning your CTF dreams into reality!

## Getting Started

- Install and [setup cmgr](/setup-cmgr.md)
    - Helpful cmgr commands are:
        - cmgr test challenges/yourchallenge (test build)
        - cmgr playtest namespace/to/yourchallenge (run a web server hosting your challenge)
        - cmgr update
        - cmgr update-schema schema.yaml
- Familiarize yourself with [Docker](https://www.docker.com/101-tutorial/)
    - Helpful docker commands are:
        - sudo docker build --build-arg FLAG="picoCTF{exampleflag}"
        - sudo docker run sha256:... (result of last command)
        - sudo docker ps
        - sudo docker exec -u root -it HEXSTRING bash (HEXSTRING from ps, gives root shell on Docker image)
- Look at some [example problems](/example-problems/)
- Peruse common [topics](/topics/README.md#topical-index) in cmgr problem dev
- Become aware of [common errors](/common-errors/) with cmgr
- Review extensive [problem developer advice](/dev-advice.md)
- BONUS: Review crucially relevant [CTF lore](https://web.archive.org/web/20201212081922/https://captf.com/maxims.html)

## Creating a challenge

This is an outline of a problem creation process that works and includes some of
the needs we have for picoCTF (like filling out the Use of Work form). This is
just a suggestion, feel free to develop challenges however feels right to you!

- Get an idea for a challenge
- Reach out to us via [email](mailto:other@picoctf.org) so we can review your
  problem idea
- Create a **private** GitHub repository for your challenge(s)
- Add `syreal17` as a collaborator on your repo
- Write a proof-of-concept challenge
- Theme or provide flavor for the challenge
- Package the challenge for cmgr
- Ensure the docker container builds correctly
- Test the challenge in cmgr
- Write a solve script
- Fill out and send the [Use of Work form](/Agreement%20for%20use%20of%20work_picoCTF.pdf)
- Receive feedback
- Observe your challenge in the next competition!
