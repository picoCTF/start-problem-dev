# References base image by SHA to avoid drift
FROM ubuntu@sha256:e3f92abc0967a6c19d0dfa2d55838833e947b9d74edbcb0113e48535ad4be12a

# Challenge metadata and artifacts go here. Only root has access
RUN install -d -m 0700 /challenge

# Copy all files from the build context to the image (just flag.txt in this case)
COPY . /app
WORKDIR /app

RUN tar czvf /challenge/artifacts.tar.gz flag.txt
RUN echo "{\"flag\":\"$(cat flag.txt)\"}" > /challenge/metadata.json

CMD tail -f /dev/null
