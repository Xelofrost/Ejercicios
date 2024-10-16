#Iniciamos importando las librerías que necesitamos para este ejercicio.
import sys
import subprocess

#Primero, construiremos la función que nos permitirá estresar al servidor elegido pidiendo la IP y la cantidad de paquetes para mandar

def estresar_servidor(direccion,paquetes):
#Creamos un bucle for, el cual lanzará el ping el numero de veces que especifiquemos
    for i in range(paquetes):
#El comando se crea usando f-strings que permite insertar variables en una cadena de texto. Insertamos la dirección IP y los parámetros
#-i 0.1 -c 1 -s 1000, los cuales especifican el intervalo(-i), el número de peticiones(-c) y el tamaño del paquete (-c).
        comando = f"ping -i 0.1 -c 1 -s 1000 {direccion}"
#El subprocess.run se utiliza para ejecutar nuestro comando y la opción de shell indica que este comando debe ejecutarse en un shell
        subprocess.run(comando, shell=True)

direccion =sys.argv[1]
paquetes =int(sys.argv[2])

estresar_servidor(direccion,paquetes)