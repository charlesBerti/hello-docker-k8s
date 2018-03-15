FROM ubuntu:xenial

RUN apt update && \
    apt install -y nodejs-legacy

COPY ./vm1_server.js /tmp/vm1_server.js

EXPOSE 8888

WORKDIR /tmp

CMD ["node", "vm1_server.js"]