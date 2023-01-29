# Set base image and make sure everything is updated
FROM linode/lamp:latest
RUN sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list&&\
    sed -i 's/mirrors.aliyun.com/mirrors.aliyun.com/g' /etc/apt/sources.list

RUN apt-get update -y && apt-get upgrade -y

# Remove example files
RUN rm -rfd /var/www/example.com
RUN rm /etc/apache2/sites-enabled/example.com.conf
RUN rm /etc/apache2/sites-available/example.com.conf
RUN rm /var/www/html/index.html

# Add our source files
RUN echo "<VirtualHost *:80>\r\nServerName NUAAACTF2020-ezlogin\r\nDocumentRoot /var/www/html\r\n</VirtualHost>" > /etc/apache2/sites-enabled/000-default.conf
ADD ./src /var/www/html
ADD ./dir /

# Copy and define entrypoint
COPY ./setup.sh /
RUN chmod 777 /setup.sh
ENTRYPOINT ["/setup.sh"]

EXPOSE 80
