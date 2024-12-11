# Retos en el Docker Vulnerable (Orden de Acceso)

## 1. **Acceder al archivo de pista con el usuario `guest`**
   - **Descripción**: El archivo `pista.txt` en el directorio de `guest` contiene los nombres de los usuarios en el sistema.
   - **Acción**: Iniciar sesión como `guest` y leer el archivo `pista.txt` en `/home/guest/`.

## 2. **Comando oculto en `.bashrc` de `user1`**
   - **Descripción**: El archivo `.bashrc` de `user1` tiene un comando oculto que se ejecuta al iniciar sesión.
   - **Acción**: Iniciar sesión como `user1` y ver el mensaje de bienvenida. Revisa también el archivo `trampa.txt` en `/home/user1/`.

## 3. **Acceso al archivo secreto de `user2`**
   - **Descripción**: El usuario `user1` puede acceder a un archivo secreto en el directorio de `user2`.
   - **Acción**: Iniciar sesión como `user1` y leer el archivo `secreto.txt` en `/home/user2/`.

## 4. **Acceder al archivo oculto con la flag en `user2`**
   - **Descripción**: El archivo `.hidden_flag.txt` en el directorio de `user2` contiene una flag secreta.
   - **Acción**: Iniciar sesión como `user2`, listar los archivos ocultos con `ls -a` y leer el archivo `.hidden_flag.txt`.

## 5. **Explotación del archivo de configuración (`important_config.txt`)**
   - **Descripción**: El archivo `/etc/important_config.txt` contiene información sensible accesible para todos los usuarios.
   - **Acción**: El usuario debe ser capaz de acceder al archivo `important_config.txt` y leer su contenido con un comando como `cat /etc/important_config.txt`.

