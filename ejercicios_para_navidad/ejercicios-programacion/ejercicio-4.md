# Python

## Ejercicios prácticos

### Brute Ping

Vamos a realizar un script que intente estresar un servidor con peticiones `ping`.

Puedes usar un comando como `ping -i 0.1 -c 1000 -s 1000 example.com` para simular un ataque de denegación de servicio, sin embargo, este comando no es lo suficientemente rápido para realizar un ataque efectivo.

Tenemos **muchas** formas de lanzar pings automatizados desde Python, pero vamos a utilizar el módulo `subprocess` para lanzar el comando `ping` desde el sistema operativo.

#### Entrada

El script debe recibir los siguientes argumentos posicionales:

1. Dirección IP del servidor
2. Número de peticiones

#### Flood de peticiones

El script debe enviar un número de peticiones `ping` al servidor especificado.

#### Control

Debemos poder tener control sobre aspectos granulares del ataque, ¿que se te ocurre que podemos añadir?

Asegúrate de añadir estos controles a la entrada de datos de usuario.