FROM ubuntu:20.04 AS base
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    build-essential
RUN install -d -m 0700 /challenge
# End of shared layers for all flask challenges

COPY Dockerfile packages.txt* ./
RUN if [ -f packages.txt ]; then apt-get update && xargs -a packages.txt apt-get install -y; fi

COPY . /app
WORKDIR /app

# End of share layers for all builds of the same flask challenge
FROM base AS challenge

ARG FLAG_FORMAT
ARG FLAG
ARG SEED

RUN make main
RUN make artifacts.tar.gz && mv artifacts.tar.gz /challenge || true
RUN make metadata.json && mv metadata.json /challenge

CMD tail -f /dev/null
