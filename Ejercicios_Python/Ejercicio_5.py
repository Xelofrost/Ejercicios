import requests
import sys

def estresar_servidor_get(direccion):
#Creamos un bucle while infinito para que nunca acabe a no ser que nosotros lo cancelemos
    while  True:
#Añadimos un nivel extra de seguridad para añadir un mensaje en caso de error
        try:
#Tras esto, simplemente ejecutamos el get a la dirección que hayamos especificado un número indefinido de veces y mostramos un mensaje cada vez
#que lo hayamos logrado o haya dado error
            respuesta=requests.get(direccion)
            print(f"Petición realizada con éxito. Código de estado: {respuesta.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error al realizar la petición: {e}")
#Finalmente llamamos  a la función con la dirección que queramos estresar
dominio =sys.argv[1]
estresar_servidor_get(dominio)