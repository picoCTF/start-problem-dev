
FROM ubuntu:20.04


# Install challenge dependencies within the image
RUN apt-get update && apt-get install -y \
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
