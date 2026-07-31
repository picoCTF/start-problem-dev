FROM ubuntu:24.04 AS base

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    --no-install-recommends \
    python3 \
    socat && \
    rm -rf /var/lib/apt/lists/*

RUN install -d -m 700 /challenge
WORKDIR /app/

# Copy app + setup
COPY perceptron_gate.py setup-challenge.py /app/
COPY start.sh /opt/
RUN chmod +x /opt/start.sh

# Package artifacts for players to download (source only)
RUN tar czf /challenge/artifacts.tar.gz perceptron_gate.py

FROM base AS challenge
ARG FLAG

# Bake the final flag + metadata
RUN python3 setup-challenge.py

EXPOSE 5555
# PUBLISH 5555 AS socat
CMD ["/opt/start.sh"]

