FROM ubuntu:18.04

RUN apt update && apt install python3-pip python3-dev -y

COPY . /srv/www/learnenjoy/

WORKDIR /srv/www/learnenjoy/

RUN pip3 install -r requirements.txt

EXPOSE 8000
