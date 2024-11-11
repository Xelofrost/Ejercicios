# Python

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

