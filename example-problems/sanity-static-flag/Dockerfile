# References base image by SHA to avoid drift. This is Ubuntu 24.04. You will
# probably want to update the hash when working on a new challenge.
FROM ubuntu:24.04@sha256:e3f92abc0967a6c19d0dfa2d55838833e947b9d74edbcb0113e48535ad4be12a AS challenge

# Challenge metadata and artifacts go here. Only root has access.
RUN install -d -m 700 /challenge

WORKDIR /app

# * Copy flag.txt to the image
COPY flag.txt ./

# * Creates /challenge/artifacts.tar.gz which cmgr uses to offer artifact
#   downloads in problem.md.
# * Creates /challenge/metadata.json which defines the flag and potentially
#   other metadata.
RUN set -eu; \
    tar -czf /challenge/artifacts.tar.gz flag.txt; \
    flag="$(tr -d '\n' < flag.txt)"; \
    printf '{"flag":"%s"}\n' "$flag" > /challenge/metadata.json

# This is a dummy command that keeps the container running. cmgr will keep
# restarting the container if it exits.
CMD ["tail", "-f", "/dev/null"]
