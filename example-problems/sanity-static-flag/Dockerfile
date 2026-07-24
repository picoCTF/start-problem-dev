FROM ubuntu:24.04 AS challenge

# Challenge metadata and artifacts go here. Only root has access.
RUN install -d -m 700 /challenge

WORKDIR /app

# * Copy flag.txt to the image
COPY flag.txt ./

# * Creates /challenge/artifacts.tar.gz which cmgr uses to offer artifact
#   downloads in problem.md.
# * Creates /challenge/metadata.json which defines the flag and potentially
#   other metadata.
RUN set -eu; \
    tar -czf /challenge/artifacts.tar.gz flag.txt; \
    flag="$(tr -d '\n' < flag.txt)"; \
    printf '{"flag":"%s"}\n' "$flag" > /challenge/metadata.json
