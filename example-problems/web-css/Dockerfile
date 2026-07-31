FROM ubuntu:24.04 AS base

# Install challenge dependencies within the image
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    --no-install-recommends \
    nginx \
    python3 && \
    rm -rf /var/lib/apt/lists/*

# Create challenge dir for metadata.json and other file artifacts
RUN install -d -m 700 /challenge

# Copy website source to nginx html directory
COPY ./public-html/ /var/www/html/

# Copy box configuration script to challenge directory
COPY setup-challenge.py /challenge/

WORKDIR /challenge/

# Specify a new stage for the challenge. Everything previous to this can be
# reused for every instance.
FROM base AS challenge
# Bring in FLAG from cmgr. Busts the cache every time.
ARG FLAG

# Configuring the box can be nicer in Python rather than in Docker RUN commands,
# but this particular config just does stuff (creating the flag and
# metadata.json) that we have been doing in the Dockerfile so far.
RUN set -eu; \
    python3 setup-challenge.py

# Open up this port for the web server
EXPOSE 80

# The comment below is parsed by cmgr. You can reference the port by the name
# given, but if there is only one port published, you don't have to use the name
# PUBLISH 80 AS web

# Run nginx in the foreground.
CMD ["nginx", "-g", "daemon off;"]