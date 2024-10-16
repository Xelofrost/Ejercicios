import requests
import json

#Usamos el request con la página de usuarios
respuesta = requests.get('https://dummyjson.com/users')

#Comprobamos si  la respuesta fue exitosa 
if respuesta.status_code == 200:
    # Con esto recibimos una respuesta json a la api que queremos sacar
    data = respuesta.json()

    # Extraemos la lista de usuarios para un diccionario
    usuarios = data['users']

    #mostramos los nombres de los usuarios
    print("Users:")
    for user in usuarios:
        print(user['firstName'] + ' ' + user['lastName'])

    with open('usuarios.txt', 'w') as f:
        for user in usuarios:
            f.write(user["firstName"] + ' ' + user["lastName"] + '\n')
else:
    print("No se pudo conectar")