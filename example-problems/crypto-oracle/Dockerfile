FROM alpine

RUN apk update
RUN apk add openssl socat python3

RUN mkdir /challenge

ARG FLAG

COPY helper.py /challenge/helper.py
COPY encr.py /challenge/encr.py
COPY flag.py /challenge/flag.py

RUN python3 /challenge/flag.py
RUN python3 /challenge/encr.py

RUN tar czvf /challenge/artifacts.tar.gz secret.enc password.enc
COPY decr.py /challenge/decr.py

CMD socat TCP4-LISTEN:4242,reuseaddr,fork exec:'python3 /challenge/decr.py'

EXPOSE 4242
# PUBLISH 4242 AS socat
