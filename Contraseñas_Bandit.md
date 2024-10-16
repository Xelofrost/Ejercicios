#PROCESO WARGAME BANDIT

##LEVEL 0:
Conexión con ssh a bandit0@bandit.labs.overthewire.org -p 2220
Investigar el archivo readme y obtener la contraseña para lvl 1
###CONTRASEÑA OBTENIDA: ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

##LEVEL 1:
Conexión con ssh a bandit1@bandit.labs.overthewire.org -p 2220
Usar la contraseña del nivel 0
PROBLEMA: El archivo a leer se llama "-" lo que impide usar el cd - o el cat - ya que se entiende como parte de un comando
SOLUCIÓN: Utilizar la dirección absoluta del archivo en vez de la relativa con un cat para ver el contenido ( cat ./-)
###CONTRASEÑA OBTENIDA: 263JGJPfgU6LtdEvgfWU1XP5yac29mFx

##LEVEL 2:
Conexión con ssh a bandit2@bandit.labs.overthewire.org -p 2220
Usar la contraseña del nivel 1
PROBLEMA: El archivo a abrir contiene espacios en el nombre
SOLUCIÓN: Poner el nombre del archivo entrecomillado ("ejemplo ejemplo") lo que hace que la terminal lo cuente como cadena de texto
###CONTRASEÑA OBTENIDA: MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

##LEVEL 3:
Conexión con ssh a bandit3@bandit.labs.overthewire.org -p 2220
Usar la contraseña del nivel 2
PROBLEMA: El archivo a leer está invisible dentro de una carpeta
SOLUCIÓN: Para averiguar el nombre del archivo, primero entramos en la carpeta con "cd inhere" y, una vez dentro, utilizamos "ls -a" para listar todos los archivos, visibles e invisibles. Finalmente, usamos cat + el nombre del archivo oculto para desvelar la contraseña.
###CONTRASEÑA OBTENIDA: 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

##LEVEL 4:
Conexión con ssh a bandit4@bandit.labs.overthewire.org -p 2220
Usar la contraseña del nivel 3
PROBLEMA: En el directorio inhere se encuentran varios archivos pero solo uno es leíble por humanos.
SOLUCIÓN: Tras entrar en el directorio, debemos usar un "file" para ver el tipo de datos de los archivos y, en vez de ir de uno en uno, usamos un *, el cual hace referencia a todos los archivos del directorio. Tras eso, descubrimos que el archivo 7 es el ASCII, el único leíble por humanos. Finalmente le hacemos un cat a este y sacamos la contraseña.
###CONTRASEÑA OBTENIDA: 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

##LEVEL 5:
Conexión con ssh a bandit5@bandit.labs.overthewire.org -p 2220
Usar la contraseña del nivel 4
PROBLEMA:Tras entrar en el directorio principal, encontramos un grupo de directorios con varios archivos en el interior de cada uno, debemos de buscar un archivo leíble por un humano, que no sea ejecutable y que pese 1033 bytes.
SOLUCIÓN: Tras establecer conexión, lo primero que haremos será ejecutar `find . -size 1033c ! -executable` lo cual nos permitirá buscar donde indiquemos( . ) mediante la función find lo que indiquemos, en este caso, buscamos un archivo que sea de 1033 bytes y que, además, no sea ejecutable (por eso la "!", para negar la condición). Tras eso solo debemos hacer un cat al archivo indicado y obtener la contraseña.
###CONTRASEÑA OBTENIDA: HWasnPhtq9AVKe0dmk45nxy20cvUa6EG

##LEVEL 6:
Conexión con ssh a bandit6@bandit.labs.overthewire.org -p 2220
Usar la contraseña del nivel 5
PROBLEMA:La contraseña se esconce en un archivo cuyo usuario propietario es bandit7 y está en el grupo bandit6 y, además, pesa 33 bytes.
SOLUCIÓN: Igual que antes debemos usar un find para encontrar el archivo correcto, al menos para empezar (find / -size 33c -group bandit6 -user bandit7) sin embargo con esto recibiremos muchos errores que complicarán la lectura, así que podemos añadir 2>/dev/null para enviar los errores al vacío, quedando algo así: `find / -size 33c -group bandit6 -user bandit7 2>/dev/null` lo que nos deja solo con el archivo que contiene la contraseña: /var/lib/dpkg/info/bandit7.password, el cual leemos con un cat para obtener nuestra recompensa
###CONTRASEÑA OBTENIDA: morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj

##LEVEL 7:
Conexión con ssh a bandit7@bandit.labs.overthewire.org -p 2220
Usar la contraseña del nivel 6
PROBLEMA: Nuestra contraseña está escrita en el archivo data.txt junto a la palabra millionth
SOLUCION: EN este caso vale con hacer un `cat data.txt | grep millionth` , de esta forma podemos filtrar la contraseña real del resto de texto del archivo
###CONTRASEÑA OBTENIDA: dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc

##LEVEL 8:
Conexión con ssh a bandit8@bandit.labs.overthewire.org -p 2220
Usar la contraseña del nivel 7
PROBLEMA: La contraseña está almacenada en el archivo data.txt y es la única que no se repite nunca.
SOLUCION: Tenemos que escanear el texto en data.txt y descartar los que se repiten, para eso usé `cat data.txt | sort | uniq -u`
###CONTRASEÑA OBTENIDA:4CKMh1JI91bUIZZPXDqGanal4xvAg0JM

##LEVEL 9:
Conexión con ssh a bandit9@bandit.labs.overthewire.org -p 2220
Usar la contraseña del nivel 8
PROBLEMA: La contraseña está en uno de los pocos string leíbles por humanos precedido de muchos =
SOLUCION:  En este caso, simplemente debemos hacer un `strings data.txt | grep  '='` siendo strings un comando que filtra todos los strings leíbles y, finalmente, el grep para buscar lo que tenga muchos = cerca.
###CONTRASEÑA OBTENIDA: FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey

##LEVEL 10:
Conexión con ssh a bandit10@bandit.labs.overthewire.org -p 2220
Usar la contraseña del nivel 9
PROBLEMA: La contraseña está en data.txt que usa datos codificados en base64
SOLUCION:
###CONTRASEÑA OBTENIDA: