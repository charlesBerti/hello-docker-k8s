FROM ubuntu:xenial

RUN apt update && \
    apt install -y nodejs-legacy

COPY ./* /tmp/

EXPOSE 8888

WORKDIR /tmp

CMD ["node", "vm2_server.js"]