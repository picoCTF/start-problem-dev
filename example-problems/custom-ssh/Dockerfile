
FROM ubuntu:18.04


# Install challenge dependencies within the image
RUN apt-get update && apt-get install -y \
    openssh-server \
    socat \
    python3


# Create challenge dir for metadata.json
RUN mkdir /challenge


# Bring in env vars
ARG SEED
ARG FLAG_FORMAT
ARG FLAG


# Create challenge metadata
RUN echo "$FLAG" > /challenge/flag
RUN echo "$SEED" > /challenge/seed
COPY split-flag.py /challenge/split-flag.py
COPY gen-password.py /challenge/gen-password.py
WORKDIR /challenge
RUN python3 split-flag.py
RUN python3 gen-password.py
RUN echo "{\"flag\":\"$FLAG\"}" > metadata.json
RUN echo "{\"flag_1of3\":\"$FLAG_1OF3\"}" >> metadata.json
RUN echo "{\"flag_2of3\":\"$FLAG_2OF3\"}" >> metadata.json
RUN echo "{\"flag_3of3\":\"$FLAG_3OF3\"}" >> metadata.json
RUN echo "{\"password\":\"$PASSWORD\"}" >> metadata.json

WORKDIR /


# Create new dirs for flag parts
RUN mkdir /home/ctf-player
RUN mkdir /home/ctf-player/.ssh
RUN mkdir /home/ctf-player/drop-in


# Create ctf-player user
RUN useradd -U ctf-player -d /home/ctf-player -s /bin/bash && \
    echo "ctf-player:$PASSWORD" | chpasswd && \
    ssh-keygen -f /home/ctf-player/.ssh/id_rsa -C ctf-player@target -P "" && \
    cat /home/ctf-player/.ssh/id_rsa.pub > /home/ctf-player/.ssh/authorized_keys && \
    chown -R ctf-player:ctf-player /home/ctf-player/.ssh && \
    chmod -R 600 /home/ctf-player/.ssh/


# Copy flag parts and hints to filesystem
COPY .profile /home/ctf-player/.profile
COPY 1of3.flag.txt /home/ctf-player/drop-in/1of3.flag.txt
COPY instructions-to-2of3.txt /home/ctf-player/drop-in/instructions-to-2of3.txt
COPY 2of3.flag.txt /2of3.flag.txt
COPY instructions-to-3of3.txt /instructions-to-3of3.txt
COPY 3of3.flag.txt /home/ctf-player/3of3.flag.txt


RUN chown -R ctf-player:ctf-player /home/ctf-player/


COPY start.sh /opt/start.sh
EXPOSE 5555
# PUBLISH 5555 AS ssh
CMD ["/opt/start.sh"]
