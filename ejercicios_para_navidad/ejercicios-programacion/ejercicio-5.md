# Python

## Ejercicios prácticos

### Brute HTTP

¿Mandar pings masivos no es suficiente? Si el servidor tiene un servidor HTTP activo, podriamos añadir un flood al ataque para aumentar nuestras peticiones y la carga del mismo. 

Vamos a hacer un script utilizando python para saturar un servidor HTTP, será similar al `flood de ping`, pero utilizando peticiones `HTTP`.

Necesitarás el módulo `requests`, que ya viene por defecto en Python.

#### Entrada

El script sólo recibe un parametro `dominio`, donde el usuario podrá enviar o una IP o una url completa.

#### Flood de peticiones

El script hará uso de `requests` para realizar las peticiones.

Por ahora, haz un script simple que siempre haga una petición `/GET`.