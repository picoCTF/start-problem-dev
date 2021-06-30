
FROM ubuntu:18.04


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


# Create challenge metadata
RUN echo "$FLAG" > /challenge/flag # This is the pre-generated flag, which
RUN echo "$SEED" > /challenge/seed #   we use as a starting point in 
                                   #   split-flag
COPY split-flag.py /challenge/split-flag.py     # These python scripts create
COPY gen-password.py /challenge/gen-password.py #   and modify files to 
WORKDIR /challenge                              #   communicate to the Docker
                                                #   build process
RUN python3 split-flag.py # This modifies `flag` and creates flag_Xof3 files
RUN python3 gen-password.py # This creates `password` to be put in metadata
RUN echo "{\n\"flag\":\"$(cat flag)\",\n" > metadata.json
RUN echo "\"password\":\"$(cat password)\"\n}" >> metadata.json


WORKDIR /

# Create new dirs for flag parts
RUN mkdir /home/ctf-player
RUN mkdir /home/ctf-player/.ssh
RUN mkdir /home/ctf-player/drop-in


# Create ctf-player user
RUN useradd -U ctf-player -d /home/ctf-player -s /bin/bash
RUN echo "ctf-player:$(cat /challenge/password)" | chpasswd


# Copy profile, flag parts and hints to filesystem
COPY profile /home/ctf-player/.profile
RUN echo $(cat /challenge/flag_1of3) > /home/ctf-player/drop-in/1of3.flag.txt
COPY instructions-to-2of3.txt /home/ctf-player/drop-in/instructions-to-2of3.txt
RUN echo $(cat /challenge/flag_2of3) > /2of3.flag.txt
COPY instructions-to-3of3.txt /instructions-to-3of3.txt
RUN echo $(cat /challenge/flag_3of3) > /home/ctf-player/3of3.flag.txt


RUN chown -R ctf-player:ctf-player /home/ctf-player/


COPY start.sh /opt/start.sh
EXPOSE 5555
# PUBLISH 5555 AS ssh
CMD ["/opt/start.sh"]