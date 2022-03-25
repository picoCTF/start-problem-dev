
FROM nginx@sha256:1c13bc6de5dfca749c377974146ac05256791ca2fe1979fc8e8278bf0121d285


# Install challenge dependencies within the image
RUN apt-get update && apt-get install -y \
    python3


COPY ./public-html/ /usr/share/nginx/html/



# Bring in all environment vars from cmgr
ARG SEED
ARG FLAG_FORMAT
ARG FLAG

# Create challenge dir for metadata.json and other file artifacts
RUN install -d -m 0700 /challenge/
COPY config-box.py /challenge/
WORKDIR /challenge/
RUN python3 config-box.py


EXPOSE 80
# PUBLISH 80 AS web
