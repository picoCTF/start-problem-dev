FROM ubuntu:24.04 AS base

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends python3 && \
    rm -rf /var/lib/apt/lists/*

# Challenge metadata and artifacts go here. Only root has access.
RUN install -d -m 700 /challenge

# * Copy script and search media to the image
COPY byteblast.py war-and-peace.txt /app/
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
    printf '%s\n' "$FLAG" | sed "s/.*{/picoCTF{gr3p_15_4_5up3rp0w3r_/1" > flag.txt; \
    cp war-and-peace.txt war-and-peace.flag.txt; \
    python3 byteblast.py war-and-peace.flag.txt flag.txt 49998

# * Creates /challenge/artifacts.tar.gz which cmgr uses to offer artifact
#   downloads in problem.md.
# * Creates /challenge/metadata.json which defines the flag and potentially
#   other metadata.
RUN set -eu; \
    tar -czf /challenge/artifacts.tar.gz war-and-peace.flag.txt; \
    flag="$(tr -d '\n' < flag.txt)"; \
    printf '{"flag":"%s"}\n' "$flag" > /challenge/metadata.json
