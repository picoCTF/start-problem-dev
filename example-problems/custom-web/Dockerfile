
FROM nginx@sha256:1c13bc6de5dfca749c377974146ac05256791ca2fe1979fc8e8278bf0121d285 AS base

# Install challenge dependencies within the image
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3

# Create challenge dir for metadata.json and other file artifacts
RUN mkdir /challenge && \
    chmod 700 /challenge

# Copy website source to nginx html directory
COPY ./public-html/ /usr/share/nginx/html/

# Copy box configuration script to challenge directory
COPY config-box.py /challenge/

WORKDIR /challenge/

# Specify a new stage for the challenge. Everything previous to this can be
# reused for every instance.
FROM base AS challenge
# Bring in FLAG from cmgr. Busts the cache every time.
ARG FLAG

RUN python3 config-box.py

EXPOSE 80
# PUBLISH 80 AS web
