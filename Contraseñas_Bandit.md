# PROCESO WARGAME BANDIT

## LEVEL 0:
Conexión con ssh a bandit0@bandit.labs.overthewire.org -p 2220
Investigar el archivo readme y obtener la contraseña para lvl 1

**CONTRASEÑA OBTENIDA: ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If**

## LEVEL 1:
Conexión con ssh a bandit1@bandit.labs.overthewire.org -p 2220
Usar la contraseña del nivel 0

PROBLEMA: El archivo a leer se llama "-" lo que impide usar el cd - o el cat - ya que se entiende como parte de un comando

SOLUCIÓN: Utilizar la dirección absoluta del archivo en vez de la relativa con un cat para ver el contenido ( cat ./-)

 **CONTRASEÑA OBTENIDA: 263JGJPfgU6LtdEvgfWU1XP5yac29mFx**

## LEVEL 2:
Conexión con ssh a bandit2@bandit.labs.overthewire.org -p 2220
Usar la contraseña del nivel 1

PROBLEMA: El archivo a abrir contiene espacios en el nombre

SOLUCIÓN:: Poner el nombre del archivo entrecomillado ("ejemplo ejemplo") lo que hace que la terminal lo cuente como cadena de texto

**CONTRASEÑA OBTENIDA: MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx**

## LEVEL 3:
Conexión con ssh a bandit3@bandit.labs.overthewire.org -p 2220
Usar la contraseña del nivel 2

PROBLEMA: El archivo a leer está invisible dentro de una carpeta

SOLUCIÓN: Para averiguar el nombre del archivo, primero entramos en la carpeta con "cd inhere" y, una vez dentro, utilizamos "ls -a" para listar todos los archivos, visibles e invisibles. Finalmente, usamos cat + el nombre del archivo oculto para desvelar la contraseña.

**CONTRASEÑA OBTENIDA: 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ**

## LEVEL 4:
Conexión con ssh a bandit4@bandit.labs.overthewire.org -p 2220
Usar la contraseña del nivel 3

PROBLEMA: En el directorio inhere se encuentran varios archivos pero solo uno es leíble por humanos.

SOLUCIÓN:: Tras entrar en el directorio, debemos usar un "file" para ver el tipo de datos de los archivos y, en vez de ir de uno en uno, usamos un *, el cual hace referencia a todos los archivos del directorio. Tras eso, descubrimos que el archivo 7 es el ASCII, el único leíble por humanos. Finalmente le hacemos un cat a este y sacamos la contraseña.

**CONTRASEÑA OBTENIDA: 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw**

## LEVEL 5:
Conexión con ssh a bandit5@bandit.labs.overthewire.org -p 2220
Usar la contraseña del nivel 4

PROBLEMA:Tras entrar en el directorio principal, encontramos un grupo de directorios con varios archivos en el interior de cada uno, debemos de buscar un archivo leíble por un humano, que no sea ejecutable y que pese 1033 bytes.

SOLUCIÓN:: Tras establecer conexión, lo primero que haremos será ejecutar `find . -size 1033c ! -executable` lo cual nos permitirá buscar donde indiquemos( . ) mediante la función find lo que indiquemos, en este caso, buscamos un archivo que sea de 1033 bytes y que, además, no sea ejecutable (por eso la "!", para negar la condición). Tras eso solo debemos hacer un cat al archivo indicado y obtener la contraseña.

**CONTRASEÑA OBTENIDA: HWasnPhtq9AVKe0dmk45nxy20cvUa6EG**

## LEVEL 6:
Conexión con ssh a bandit6@bandit.labs.overthewire.org -p 2220
Usar la contraseña del nivel 5

PROBLEMA:La contraseña se esconce en un archivo cuyo usuario propietario es bandit7 y está en el grupo bandit6 y, además, pesa 33 bytes.

SOLUCIÓN:: Igual que antes debemos usar un find para encontrar el archivo correcto, al menos para empezar (find / -size 33c -group bandit6 -user bandit7) sin embargo con esto recibiremos muchos errores que complicarán la lectura, así que podemos añadir 2>/dev/null para enviar los errores al vacío, quedando algo así: `find / -size 33c -group bandit6 -user bandit7 2>/dev/null` lo que nos deja solo con el archivo que contiene la contraseña: /var/lib/dpkg/info/bandit7.password, el cual leemos con un cat para obtener nuestra recompensa

**CONTRASEÑA OBTENIDA: morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj**

## LEVEL 7:
Conexión con ssh a bandit7@bandit.labs.overthewire.org -p 2220
Usar la contraseña del nivel 6

PROBLEMA: Nuestra contraseña está escrita en el archivo data.txt junto a la palabra millionth

SOLUCIÓN:: EN este caso vale con hacer un `cat data.txt | grep millionth` , de esta forma podemos filtrar la contraseña real del resto de texto del archivo

**CONTRASEÑA OBTENIDA: dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc**

## LEVEL 8:
Conexión con ssh a bandit8@bandit.labs.overthewire.org -p 2220
Usar la contraseña del nivel 7

PROBLEMA: La contraseña está almacenada en el archivo data.txt y es la única que no se repite nunca.

SOLUCIÓN:: Tenemos que escanear el texto en data.txt y descartar los que se repiten, para eso usé `cat data.txt | sort | uniq -u`

**CONTRASEÑA OBTENIDA:4CKMh1JI91bUIZZPXDqGanal4xvAg0JM**

## LEVEL 9:
Conexión con ssh a bandit9@bandit.labs.overthewire.org -p 2220
Usar la contraseña del nivel 8

PROBLEMA: La contraseña está en uno de los pocos string leíbles por humanos precedido de muchos =

SOLUCIÓN:  En este caso, simplemente debemos hacer un `strings data.txt | grep  '='` siendo strings un comando que filtra todos los strings leíbles y, finalmente, el grep para buscar lo que tenga muchos = cerca.

**CONTRASEÑA OBTENIDA: FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey**

## LEVEL 10:
Conexión con ssh a bandit10@bandit.labs.overthewire.org -p 2220
Usar la contraseña del nivel 9

PROBLEMA: La contraseña está en data.txt que usa datos codificados en base64

SOLUCION: Abrimos el archivo .txt, tomamos su contenido y usamos una herramiento para decodificarlo. En mi caso he usado cyberchef, pero también se puede usar hydra.

**CONTRASEÑA OBTENIDA: dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr**

## LEVEL 11:
Conexión con ssh a bandit11@bandit.labs.overthewire.org -p 2220
Usar la contraseña del nivel 10

PROBLEMA: La contraseña está en un archivo donde todas las letras han rotado 13 posiciones.

SOLUCION: Al igual que en el ejercicio anterior, tenemos un .txt codificad, esta vez, con ROT13 o cifrado cesar. Para dehacerlo podemos simplemente descrifrarlo en programas como cyberchef o podemos hacer uso de la función "tr", quedando algo así: 
```bash
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```
**CONTRASEÑA OBTENIDA: 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4**

## LEVEL 12:
Conexión con ssh a bandit12@bandit.labs.overthewire.org -p 2220
Usar la contraseña del nivel 11

PROBLEMA: La contraseña está dentro de un .txt en forma de un hexdump que ha sido comprimido
varias veces por distintos metodos de compresión.

SOLUCION: Primero debemos convertir el hexdump de vuelta a los datos comprimidos, así que para ello usamos el comando "xxd" dejando algo así:

```bash
 xxd -r ~/data.txt datosdeshexados.txt
```

A continuación debemos empezar a desempaquetar los datos originales, para eso debemos descubrir que tipo de compresión lleva en cada parte, para eso debemos hacer un cat de los datos y fijarnos en los primeros bytes en el hexdump, utilizando una lista externa que nos ayude a identificarlo ( yo he usado esta: https://en.wikipedia.org/wiki/List_of_file_signatures ) y hemos ido descomprimiendo por pasos. El primer tipo de compresión es un gzip. Cambiamos el tipo de archivo de ".txt" a ".gzip" y descomprimimos.

```bash
mv datosdeshexados.txt datosdeshexados.gz
gzip -d datosdeshexados.gz
```

Para proseguir, tenemos que convertir estos datos de nuevo al hexdump y descubriremos que la proxima compresión fue hecha con BZIP2, una vez sabemos esto, solo repetimos el anterior proceso.

```bash
xxd datosdeshexados 
mv datosdeshexados datosdeshexados.bz2
bzip2 -d datosdeshexados.bz2
```

Y repetimos una vez más la misma operación con GZIP.

```bash
xxd datosdeshexados 
mv datosdeshexados datosdeshexados.gz
gzip -d datosdeshexados.gz
```

Al volver a realizar lo mismo una vez más, en el hexdump podemos ver que este archivo parece ser un archivo TAR porque contiene metadatos que son típicos de este formato. El encabezado muestra información como el nombre del archivo (data5.bin), los permisos del archivo (0644), el tamaño (0), y posibles marcas de tiempo, que son características comunes en los archivos TAR, así que a continuación extraemos el archivo

```bash
xxd datosdeshexados | head
mv datosdeshexados datosdeshexados.tar
tar -xf datosdeshexados.tar
```
Y al realizar lo mismo con este archivo nuevo, podemo ver que contiene otro archivo en su interior para extraer con TAR.
```bash
xxd data5.bin | head
tar -xf data5.bin
```

A continuación, comprobamos el hexdump del nuevo archivo y vemos que está comprimido con BZIP2 de nuevo, así que volvemos a descomprimirlo.
```bash
xxd data6.bin | head
bzip2 -d data6.bin
bzip2: Can't guess original name for data6.bin -- using data6.bin.out
```
En este hexdump volvemos a encontrar un archivo dentro, así que volvemos a usar TAR para extraerlo.
```bash
xxd data6.bin.out | head
tar -xf data6.bin.out
```
Y finalmente realizamos una última comprobación para ver que el archivo está comprimido con GZIP, así que hacemos una última descompresión y finalmente comprobamos con "cat" el contenido del último archivo para encontrar la contraseña.

```bash
xxd data8.bin
mv data8.bin data8.gz
gzip -d data8.gz
cat data8.bin
```
**CONTRASEÑA OBTENIDA: FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn**

## LEVEL 13:
Conexión con ssh a bandit13@bandit.labs.overthewire.org -p 2220
Usar la contraseña del nivel 12

PROBLEMA: La contraseña está guardada en /etc/bandit_pass/bandit14 y solo se puede leer desde el usuario bandit14. En este nivel no habrá contraseña, pero sí una sshkey para conectarse al siguiente nivel.

SOLUCIÓN: Comprobamos que ls sshkey.private está dentro con un ls. Tras eso, podemo cerrar la conexión ssh y utilizar un scp para quedarnos con la llave ssh.
```bash
scp -P 2220 bandit13@bandit.labs.overthewire.org:sshkey.private .
```

Tras eso trato de conectarme con la key, pero puedo ver que no me lo permite porque tiene demasiados permisos, así que lo reduzco con "chmod 700" para que solo yo pueda abrirlo y entonces sí me lo permite.
```bash
chmod 700 sshkey.private 
ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220
```
**CONTRASEÑA OBTENIDA: MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS**
