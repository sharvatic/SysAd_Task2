FROM ubuntu:latest
RUN apt-get -y update && apt-get -y install apache2
COPY ./default.conf /etc/apache2/sites-available/000-default.conf
COPY ./server1 /var/www/html
