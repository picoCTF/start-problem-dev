# LAUNCH ssh_host challenge

FROM ubuntu@sha256:da5fdf346e5313bef2a3dd2476c0251d48103213a5e3a0cb3afbb8909f3cf50f AS builder_base

# Install challenge dependencies within the image
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3

# Create challenge dir for metadata.json and other file artifacts
RUN mkdir /challenge && chmod 700 /challenge
COPY config-builder.py /challenge/

FROM builder_base as builder
# Bring in cmgr args
ARG SEED
ARG FLAG

RUN python3 /challenge/config-builder.py

#######################
#### Host: sshHost ####
#######################
FROM ubuntu@sha256:da5fdf346e5313bef2a3dd2476c0251d48103213a5e3a0cb3afbb8909f3cf50f AS ssh_host_base

# Install challenge dependencies within the image
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    openssh-server \
    python3 \
    iputils-ping \
    socat

COPY config-sshhost.py /challenge/
COPY start.sh /opt/
COPY profile /home/ctf-player/.profile
COPY instructions-to-2of3.txt /home/ctf-player/drop-in/
COPY instructions-to-3of3.txt /
COPY --from=builder /challenge/1of3.flag.txt /home/ctf-player/drop-in/
COPY --from=builder /challenge/2of3.flag.txt /

FROM ssh_host_base AS ssh_host
COPY --from=builder /challenge/password.txt /tmp/

RUN python3 /challenge/config-sshhost.py && \
    rm -rf /challenge/

COPY --from=builder /challenge/3of3.flag.txt /home/ctf-player/

EXPOSE 5555
# PUBLISH 5555 AS ssh
CMD ["/opt/start.sh"]

#######################
#### Host: challenge ##
#######################
FROM ubuntu@sha256:da5fdf346e5313bef2a3dd2476c0251d48103213a5e3a0cb3afbb8909f3cf50f AS challenge

CMD ["tail", "-f", "/dev/null"]
