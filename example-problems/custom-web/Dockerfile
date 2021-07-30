
FROM httpd:2.4


COPY ./public-html/ /usr/local/apache2/htdocs/


# Create challenge dir for metadata.json and other file artifacts
RUN mkdir /challenge


# Bring in all environment vars from cmgr
ARG SEED
ARG FLAG_FORMAT
ARG FLAG


EXPOSE 80
# PUBLISH 80 AS web
