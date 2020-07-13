FROM alpine:latest
LABEL maintainer="Nicolas"
LABEL description="My first docker file EVER!"
RUN apk add --update nginx && \
rm -rf /var/cache/apk/* && \
mkdir -p /tmp/nginx/
RUN apk add python3
COPY README.txt /home/nicolas/Desktop/DockerFiles
EXPOSE 80/tcp
ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]
