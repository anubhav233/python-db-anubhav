FROM ubuntu:18.04
#FROM ubuntu
LABEL maintainer="Merryl DMello mdmello@phoenixcontact-sb.io"
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential libpq-dev postgresql-client postgresql-client-common
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["scripts/entrypoint.sh"]
