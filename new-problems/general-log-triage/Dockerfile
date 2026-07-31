FROM ubuntu:24.04 AS base

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    python3 && \
    rm -rf /var/lib/apt/lists/*

RUN install -d -m 700 /challenge
WORKDIR /app

COPY build-challenge.py /app/

FROM base AS challenge
ARG FLAG

RUN python3 /app/build-challenge.py "$FLAG"
