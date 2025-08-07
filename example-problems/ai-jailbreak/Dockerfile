FROM ubuntu@sha256:626ffe58f6e7566e00254b638eb7e0f3b11d4da9675088f4781a50ae288f3322 AS base

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3 \
    python3-pip \
    socat


# Install Python dependencies
RUN pip3 install --no-cache-dir \
    transformers \
    torch

RUN mkdir /challenge && chmod 700 /challenge

COPY ai-interface.py setup-challenge.py /app/
COPY start.sh /opt/
WORKDIR /app/
RUN tar czvf /challenge/artifacts.tar.gz ai-interface.py

FROM base AS challenge
ARG FLAG

RUN python3 setup-challenge.py

# The start.sh script starts a socat listener on port 5555, that connects to the
# python script.
EXPOSE 5555
# PUBLISH 5555 AS socat
CMD ["/opt/start.sh"]
