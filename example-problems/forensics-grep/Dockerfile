# References base image by SHA to avoid drift. This is Python 3.12. You will
# probably want to update the hash when working on a new challenge.
FROM python@sha256:2fba8e70a87bcc9f6edd20dda0a1d4adb32046d2acbca7361bc61da5a106a914 AS base

# Challenge metadata and artifacts go here. Only root has access
RUN mkdir /challenge && \
    chmod 700 /challenge

# * Copy script and search media to the image
COPY byteblast.py war-and-peace.txt /app/
WORKDIR /app

FROM base AS challenge
# Bring in the pre-generated flag from cmgr. FLAG_FORMAT and SEED are also
# available but not used in this problem.
ARG FLAG

# * Use the randomness from the cmgr flag to construct our own instanced flag
# * byteblast.py is a script that overwrites bytes at an offset for a file
RUN echo $FLAG | sed "s/.*{/picoCTF{gr3p_15_4_5up3rp0w3r_/1" > flag.txt && \
    cp war-and-peace.txt war-and-peace.flag.txt && \
    python3 byteblast.py war-and-peace.flag.txt flag.txt 49998

# * Creates /challenge/artifacts.tar.gz which cmgr uses to offer artifact
#   downloads in problem.md.
# * Creates /challenge/metadata.json which defines the flag and potentially
#   other metadata.
RUN tar czvf /challenge/artifacts.tar.gz war-and-peace.flag.txt && \
    echo "{\"flag\":\"$(cat flag.txt)\"}" > /challenge/metadata.json

# This is a dummy command that keeps the container running. cmgr will keep
# trying to restart the container if it exits.
CMD ["tail", "-f", "/dev/null"]
