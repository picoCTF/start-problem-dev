# Example Problems

These example problems proceed roughly in order of complexity, from least
complex challenge to most complex challenge. These are great problems to start
problem development with.

1. [Sanity, static flag](/example-problems/sanity-static-flag/)
   - Presents the simplest of all CTF problems, the sanity check. Also goes over
     deploying and testing a problem.
1. [Forensics Grep](/example-problems/forensics-grep/)
   - Embeds the flag in a downloadable artifact. Also goes over testing
     templating.
1. [Forensics Disk](/example-problems/forensics-disk/)
   - Embeds the flag in a more complex artifact.
1. [Custom Web](/example-problems/custom-web/)
   - Demonstrates hosting a simple web-based problem.
1. [Custom Service](/example-problems/custom-service/)
   - Presents a vulnerable program through a port using socat. Also goes over
     some tips on debugging your Dockerfile.
1. [Custom SSH (Multi-stage Dockerfile)](/example-problems/custom-ssh/)
   - Demonstrates separating the challenge builder container from the
     interactive container.

In addition to these walkthroughs, you can also check the `cmgr` developers'
[example problems,](https://github.com/picoCTF/cmgr/tree/master/examples) which
are a good source for more complex problem development.
