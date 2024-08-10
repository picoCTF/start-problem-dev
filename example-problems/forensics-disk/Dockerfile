# References base image by SHA to avoid drift. This is Python 3.12. You will
# probably want to update the hash when working on a new challenge.
FROM ubuntu@sha256:e3f92abc0967a6c19d0dfa2d55838833e947b9d74edbcb0113e48535ad4be12a AS base

# Install python3
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y python3

# Challenge metadata and artifacts go here. Only root has access
RUN mkdir /challenge && \
    chmod 700 /challenge

# * Copy script and search media to the image
COPY byteblast.py disk.img.gz /app/
WORKDIR /app

FROM base AS challenge
# Bring in the pre-generated flag from cmgr. FLAG_FORMAT and SEED are also
# available but not used in this problem.
ARG FLAG

# * Use the randomness from the cmgr flag to construct our own instanced flag
# * byteblast.py is a script that overwrites bytes at an offset for a file
RUN echo $FLAG | sed "s/.*{/picoCTF{d15k_513uth_/1" > flag.txt && \
    cp disk.img.gz disk.flag.img.gz && \
    gunzip disk.flag.img.gz && \
    python3 byteblast.py disk.flag.img flag.txt 509014036 && \
    gzip -c disk.flag.img > disk.flag.img.gz

# * Creates /challenge/artifacts.tar.gz which cmgr uses to offer artifact
#   downloads in problem.md.
# * Creates /challenge/metadata.json which defines the flag and potentially
#   other metadata.
RUN tar czvf /challenge/artifacts.tar.gz disk.flag.img.gz && \
    echo "{\"flag\":\"$(cat flag.txt)\"}" > /challenge/metadata.json

# This is a dummy command that keeps the container running. cmgr will keep
# trying to restart the container if it exits.
CMD ["tail", "-f", "/dev/null"]
