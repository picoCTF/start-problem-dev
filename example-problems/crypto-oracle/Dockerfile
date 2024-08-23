FROM alpine@sha256:b93f4f6834d5c6849d859a4c07cc88f5a7d8ce5fb8d2e72940d8edd8be343c04 AS base

RUN apk update && apk add openssl socat python3

RUN mkdir /challenge && chmod 700 /challenge

COPY helper.py encr.py flag.py decr.py /challenge/

FROM base AS challenge
ARG FLAG

RUN python3 /challenge/flag.py
RUN python3 /challenge/encr.py

RUN tar czvf /challenge/artifacts.tar.gz secret.enc password.enc

CMD socat TCP4-LISTEN:4242,reuseaddr,fork exec:'python3 /challenge/decr.py'

EXPOSE 4242
# PUBLISH 4242 AS socat
