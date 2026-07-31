FROM ubuntu:24.04 AS base

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    --no-install-recommends \
    python3 \
    socat \
    && rm -rf /var/lib/apt/lists/*

RUN install -d -m 700 /challenge

COPY picker-I.py setup-challenge.py /app/
COPY start.sh /opt/
WORKDIR /app/
RUN set -eu; \
    tar -czf /challenge/artifacts.tar.gz picker-I.py

FROM base AS challenge
ARG FLAG

RUN python3 setup-challenge.py

# The start.sh script starts a socat listener on port 5555, that connects to the
# python script.
EXPOSE 5555
# PUBLISH 5555 AS socat
CMD ["/opt/start.sh"]
