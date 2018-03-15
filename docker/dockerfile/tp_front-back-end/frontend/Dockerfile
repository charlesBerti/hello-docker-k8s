FROM ubuntu:xenial

RUN apt update && \
    apt install -y nodejs-legacy

COPY ./vm1_server.js /tmp/vm1_server.js
WORKDIR /tmp

EXPOSE 8888

CMD ["node", "vm1_server.js"]