
FROM ubuntu:18.04


# Install challenge dependencies within the image
RUN apt-get update && apt-get install -y \
    openssh-server \
    socat


# Create challenge dir for metadata.json
RUN mkdir /challenge

ARG FLAG_FORMAT
ARG FLAG

RUN echo "{\"flag\":\"$FLAG\"}" > /challenge/metadata.json
# TODO : call to Python script that parses and splits $FLAG


# Create new dirs for flag parts
RUN mkdir /home/ctf-player
RUN mkdir /home/ctf-player/.ssh
RUN mkdir /home/ctf-player/drop-in


# TODO : remove key stuff (was originally for ssh-based port forwaring)
# Create ctf-player user
RUN useradd -U ctf-player -d /home/ctf-player -s /bin/bash && \
    echo "ctf-player:{{password}}" | chpasswd && \
    ssh-keygen -f /home/ctf-player/.ssh/id_rsa -C ctf-player@target -P "" && \
    cat /home/ctf-player/.ssh/id_rsa.pub > /home/ctf-player/.ssh/authorized_keys && \
    chown -R ctf-player:ctf-player /home/ctf-player/.ssh && \
    chmod -R 600 /home/ctf-player/.ssh/


COPY .profile /home/ctf-player/.profile
COPY 1of3.flag.txt /home/ctf-player/drop-in/1of3.flag.txt
COPY instructions-to-2of3.txt /home/ctf-player/drop-in/instructions-to-2of3.txt
COPY 2of3.flag.txt /2of3.flag.txt
COPY instructions-to-3of3.txt /instructions-to-3of3.txt
COPY 3of3.flag.txt /home/ctf-player/3of3.flag.txt


RUN chown -R ctf-player:ctf-player /home/ctf-player/


COPY start.sh /opt/start.sh
EXPOSE 5555
CMD ["/opt/start.sh"]

