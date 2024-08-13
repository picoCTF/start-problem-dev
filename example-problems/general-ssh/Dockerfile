# LAUNCH sshHost

FROM ubuntu@sha256:626ffe58f6e7566e00254b638eb7e0f3b11d4da9675088f4781a50ae288f3322 AS builder


# Install challenge dependencies within the image
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3


# Create challenge dir for metadata.json and other file artifacts
RUN mkdir /challenge


# Bring in all environment vars from cmgr
ARG SEED
ARG FLAG_FORMAT
ARG FLAG


COPY config-builder.py /challenge/config-builder.py

RUN python3 /challenge/config-builder.py



#######################
#### Host: sshHost ####
#######################
FROM ubuntu@sha256:626ffe58f6e7566e00254b638eb7e0f3b11d4da9675088f4781a50ae288f3322 AS sshHost


# Install challenge dependencies within the image
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    openssh-server \
    socat \
    python3


COPY --from=builder /challenge/password.txt /tmp/password.txt
COPY config-sshhost.py /challenge/config-sshhost.py
COPY start.sh /opt/start.sh

RUN python3 /challenge/config-sshhost.py
RUN rm -rf /challenge/

COPY profile /home/ctf-player/.profile
COPY instructions-to-2of3.txt /home/ctf-player/drop-in/instructions-to-2of3.txt
COPY instructions-to-3of3.txt /instructions-to-3of3.txt
COPY --from=builder /challenge/1of3.flag.txt /home/ctf-player/drop-in/1of3.flag.txt
COPY --from=builder /challenge/2of3.flag.txt /2of3.flag.txt
COPY --from=builder /challenge/3of3.flag.txt /home/ctf-player/3of3.flag.txt

EXPOSE 5555
# PUBLISH 5555 AS ssh
CMD ["/opt/start.sh"]
