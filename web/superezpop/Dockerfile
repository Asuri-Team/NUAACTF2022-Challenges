FROM php:7.2.2-apache
WORKDIR /var/www/html
#COPY www/ .

RUN rm -f /var/www/html/index.html
COPY html /var/www/html

EXPOSE 80