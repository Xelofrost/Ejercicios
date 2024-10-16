# Pruebas cybsec en DVWA
## Baja seguridad
### Fuerza Bruta

Para realizar esta primera prueba empezaremos con algo sencillo, siendo esto una prueba para iniciar sesión en la página. Para esto, deberemos hacer uso de la aplicación **BurpSuite** para realizar los ataques por diccionario.

Iniciamos activando nuestro proxy de Burp en nuestro navegador y el interceptor  de la aplicación. Luego, nos dirigimos a la página de inicio de sesión de DVWA en el apartado de fuerza bruta y probamos cualquier usuario  y contraseña.

Tras esto, deberemos darle a login y volver a Burp para ver en qué parte del GET se envía el usuario y contraseñas escritors, tras lo cual simplemente deberemos localizarlos, enviarlos al intruder y, usando la **cluster bomb** como método y dos diccionarios uno de usuarios y otro de contraseñas atacaremos a fuerza bruta para tratar de dar con las credenciales para poder entrar que, en este caso, son

**Usuario** = *Admin*  y **Contraseña** = *password*.

### Inyección de comandos en linea

Para esta práctica no necesitaremos más que la propia página web de DVWA en el ejercicio pertinente y algo de conocimientos bash.

Al inspeccionar este elemento desde la página web, monitorizando la red y viendo como se envía el ping a realizar, podemos ver que separando la IP inicial de otro comando mediante **;** podemos introducir código para, por ejemplo, ver archivos dentro de donde se hace el ping con un **ls**, entre otros.

### Cross Site Request Forgery

En esta ocasión nos aprovecharemos de la confianza que el desarrollador tuvo en el usuario y en que nadie podría acceder al cambio de contraseña más que el dueño de la cuenta.

Haciendo uso de BurpSuite, podemos ver el URL en el que la nueva contraseña es mostrada sin nada de seguridad (no piden ni el usuario), lo cual nos permite disfrazar el enlace y, al enviarselo a otra persona, esta al clickar se le cambiará su contraseña automáticamente a la que nosotros dejemos preparada en el url.

### Subida de archivos

Para esta prueba simplemente necesitaremos crear un archivo con algo de código básico de php o JS, en este caso, PHP. Al subir el archivo, lo que escribamos dentro de este se guardará en el servidor y lo interpretará como código normal, por lo que podemos hacer uso de esto para subir un script malicioso y acceder a él escribiendo la ruta de nuestro archivo en nuestro servidor, en este caso siendo:

- **http://172.17.0.2/hackable/uploads/<nombre_del_archivo>**

### Inyección SQL

