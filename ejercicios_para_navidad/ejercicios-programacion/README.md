# Python

## Ejercicios prácticos

### Conversor ARN a ADN

Una cadena de ARN se compone de las letras `A`, `U`, `G` y `C`.

Una cadena de ADN se compone de las letras `A`, `T`, `G` y `C`.

Crea un script utilizando `python` que convierta cadenas de ARN a ADN.

### Entrada

Añade un argumento posicional para que el usuario pueda introducir la cadena de ARN a convertir con el módulo `sys.argv`.

### Validación

Asegúrate de que la cadena introducida sea válida, es decir, que sólo contenga las letras `A`, `U`, `G` y `C`.

Si la cadena no es válida, muestra un mensaje de error personalizado y finaliza el programa.

Intenta que el mensaje de error sea útil para que el usuario pueda corregir su entrada.

### Salida

Muestra la cadena de ADN resultante en la terminal.# Python

## Ejercicios prácticos

### Conversor 13375P34K

Los cifrados de sustitución son una forma de cifrado en la que los elementos del texto en claro (usualmente letras) son reemplazados por otros elementos.

13375P34K es una forma de escribir común en la red, donde se sustituyen letras por números y caracteres especiales.

Una sustitución básica de 13375P34K sería la siguiente:

```plaintext
O -> 0
I -> 1
E -> 3
A -> 4
S -> 5
G -> 6
T -> 7
B -> 8
g -> 9
```

Por ejemplo:

```plaintext
Texto: Hola Mundo
Resultado: H0l4 Mund0
```

Crea un script que convierta una cadena de texto a 13375P34K.

### Entrada

Añade un argumento posicional para que el usuario pueda introducir el texto a convertir.

### [EXTRA] Sustitución avanzada

El script es demasiado básico, nuestra abuela podría leer ese mensaje, añade más sustituciones para que sea más efectivo.# Python

## Ejercicios prácticos

### Cajas en la terminal

Crea un script utilizando `python` que imprima cajas de diferente tamaño.

Deberás utilizar los siguientes caracteres, pertenecientes a la tabla de caracteres ASCII:

- (U+250C) para la esquina superior izquierda
- (U+2510) para la esquina superior derecha
- (U+2514) para la esquina inferior izquierda
- (U+2518) para la esquina inferior derecha
- (U+2500) para las líneas horizontales
- (U+2502) para las líneas verticales

- (U+2554) para la esquina superior izquierda
- (U+2557) para la esquina superior derecha
- (U+255A) para la esquina inferior izquierda
- (U+255D) para la esquina inferior derecha
- (U+2550) para las líneas horizontales
- (U+2551) para las líneas verticales

El script debe cumplir las siguientes condiciones:

#### Entrada

El script debe recibir tres argumentos posicionales:

1. Ancho de la caja
2. Alto de la caja
3. Linea simple o doble

#### Salida

Deberás mostrar una caja en la terminal con las dimensiones y el tipo de línea especificado por el usuario.

Si el tercer argumento es `simple`, la caja debe ser de líneas simples, si es `doble`, la caja debe ser de líneas dobles, Si el usuario ingresa un valor distinto y es un string de un solo carácter, se debe utilizar ese carácter para dibujar la caja.

#### `[EXTRA]` Gestión de errores

Si el script no recibe los tres argumentos, debe mostrar un mensaje de error y mostrar al usuario un ejemplo de uso.

Si el script recibe argumentos no numéricos en los dos primeros argumentos, debe mostrar un mensaje de error y mostrar al usuario un ejemplo de uso.

Si el script recibe un argumento diferente de `simple`, `doble` o un string de un solo carácter, debe mostrar un mensaje de error y mostrar al usuario un ejemplo de uso.

#### `[EXTRA` Salida proporcional

Los caracteres ascii no tienen el mismo ancho que alto, por lo que las cajas no se verán proporcionales y el usuario deberá ajustar los valores de ancho y alto para que la caja se vea cuadrada. Consigue que la caja sea lo más cuadrada posible cuando el usaurio ingrese valores de ancho y alto iguales.

#### `[EXTRA]` Relleno

En lugar de de dejar la caja vacía, usa de caracteres aleatorios, utiliza **SOLO** el conjunto de caracteres ASCII para rellenar la caja.

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

Asegúrate de añadir estos controles a la entrada de datos de usuario.# Python

## Ejercicios prácticos

### Brute HTTP

¿Mandar pings masivos no es suficiente? Si el servidor tiene un servidor HTTP activo, podriamos añadir un flood al ataque para aumentar nuestras peticiones y la carga del mismo. 

Vamos a hacer un script utilizando python para saturar un servidor HTTP, será similar al `flood de ping`, pero utilizando peticiones `HTTP`.

Necesitarás el módulo `requests`, que ya viene por defecto en Python.

#### Entrada

El script sólo recibe un parametro `dominio`, donde el usuario podrá enviar o una IP o una url completa.

#### Flood de peticiones

El script hará uso de `requests` para realizar las peticiones.

Por ahora, haz un script simple que siempre haga una petición `/GET`.# Python

## Ejercicios prácticos

### API Call

Vamos a realizar un script que realice peticiones a una API pública.

Esto te servirá para entender cómo funcionan las peticiones HTTP y cómo manejar las respuestas.

En ciberseguridad, es importante entender cómo funcionan las APIs para poder analizarlas. Muchas veces, las APIs muestran información sensible que puede ser utilizada para realizar ataques, cuando no son el vector de ataque en sí mismas.

Saber llamar a APIs también te ayudará a automatizar tareas, crear diccionarios y entenderás mejor algunas técnicas de pen testing para web.

Con Python podemos realizar peticiones HTTP utilizando el módulo `requests`, y luego analizar las respuesta que nos da el servidor, igual que haríamos con las developer tools de un navegador, o con herramientas como Postman, con la diferencia de que podemos automatizar todo el proceso y scriptar las peticiones y como responder a ellas.

Este endpoint devuelve una lista de usuarios en formato JSON:

[](https://dummyjson.com/users)

Tu tarea es realizar un script que haga una petición a este endpoint y muestre en pantalla el nombre de todos los usuarios, luego, guarda esos nombres en un archivo.


