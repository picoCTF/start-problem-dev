
FROM ubuntu@sha256:626ffe58f6e7566e00254b638eb7e0f3b11d4da9675088f4781a50ae288f3322


# Install challenge dependencies within the image
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    openssh-server \
    socat \
    python3


# Create challenge dir for metadata.json and other file artifacts
RUN mkdir /challenge


# Bring in all environment vars from cmgr
ARG SEED
ARG FLAG_FORMAT
ARG FLAG


COPY config-box.py /challenge/config-box.py
COPY profile /challenge/profile
COPY instructions-to-2of3.txt /challenge/instructions-to-2of3.txt
COPY instructions-to-3of3.txt /challenge/instructions-to-3of3.txt
COPY start.sh /opt/start.sh

RUN python3 /challenge/config-box.py



EXPOSE 5555
# PUBLISH 5555 AS ssh
CMD ["/opt/start.sh"]
