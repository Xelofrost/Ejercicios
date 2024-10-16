# Apuntes Docker
```
 Colocando 2222 como puerto ya que es el que hemos especificado en el archivo Dockerfile, el cual es necesario para crear el contenedor. Para crearlo y lanzarlo respectivamente, desde la carpeta en la que creamos el "**Dockerfile**" ejecutamos

```bash
docker build -t sshlab .
===========================================================
docker run -d -p 2222:22 sshlab
```

Para conectarnos por ssh en local usaremos 
```bash
ssh <usuario>@localhost -p <puerto>
```

Mientras que si queremos conectarnos de forma remota como, por ejemplo, desde nuestra maquina virtual de Kali lo conectaremos así:

```bash
ssh <usuario>@<IPHost> -p <puerto>
```

## Como usar hydra en nuestro Kali para aprovecharnos de esto

Hydra en Kali es una sencilla herramienta de la terminal que nos permite hacer ataques de fuerza bruta a una ssh en concreto haciendo uso de listas de usuarios y contraseñas.

Para lanzar hydra en la terminal se escribe de la siguiente forma:

```bash
hydra -L <ruta a la lista de usuarios> -P <ruta a la lista de contraseñas> <protocolo>://<Ip del docker>:<puerto>
```

-L en mayúscula nos permite buscar en una lista de usuarios mientras que en minúscula es para un usuario concreto

-P en mayúscula nos permite buscar en una lista de contraseñas mientras que en minúscula es para una contraseña concreta

Esto nos pemitirá comprobar todos los usuarios y contraseñas de ambas listas entre ellos y devolverá los resultados.