# Ubuntu is used in the other example challenges; install Python for byteblast.
FROM ubuntu:24.04 AS base

# Install python3
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends python3 && \
    rm -rf /var/lib/apt/lists/*

# Challenge metadata and artifacts go here. Only root has access.
RUN install -d -m 700 /challenge

# * Copy script and search media to the image
COPY byteblast.py disk.img.gz /app/
WORKDIR /app

# We specify a new stage here so that base layers can be reused for every
# instance, but FLAG is always going to be different, so that will always bust
# the cache.
FROM base AS challenge
# Bring in the pre-generated flag from cmgr. FLAG_FORMAT and SEED are also
# available but not used in this problem.
ARG FLAG

# * Use the randomness from the cmgr flag to construct our own instanced flag
# * byteblast.py is a script that overwrites bytes at an offset for a file
RUN set -eu; \
    printf '%s\n' "$FLAG" | sed "s/.*{/academy{d15k_513uth_/1" > flag.txt; \
    cp disk.img.gz disk.flag.img.gz; \
    gunzip disk.flag.img.gz; \
    python3 byteblast.py disk.flag.img flag.txt 509014036; \
    gzip -c disk.flag.img > disk.flag.img.gz

# * Creates /challenge/artifacts.tar.gz which cmgr uses to offer artifact
#   downloads in problem.md.
# * Creates /challenge/metadata.json which defines the flag and potentially
#   other metadata.
RUN set -eu; \
    tar -czf /challenge/artifacts.tar.gz disk.flag.img.gz; \
    flag="$(tr -d '\n' < flag.txt)"; \
    printf '{"flag":"%s"}\n' "$flag" > /challenge/metadata.json

# This is a dummy command that keeps the container running. cmgr will keep
# trying to restart the container if it exits.
CMD ["tail", "-f", "/dev/null"]
