FROM php:5.3-apache

# Instalar la extensión mysqli (si es necesario en PHP 5.3)
RUN docker-php-ext-install mysqli

# Copiar los archivos del proyecto al contenedor
COPY . /var/www/html
