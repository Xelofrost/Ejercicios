# Python

## Ejercicios prácticos

### API Call

Vamos a realizar un script que realice peticiones a una API pública.

Esto te servirá para entender cómo funcionan las peticiones HTTP y cómo manejar las respuestas.

En ciberseguridad, es importante entender cómo funcionan las APIs para poder analizarlas. Muchas veces, las APIs muestran información sensible que puede ser utilizada para realizar ataques, cuando no son el vector de ataque en sí mismas.

Saber llamar a APIs también te ayudará a automatizar tareas, crear diccionarios y entenderás mejor algunas técnicas de pen testing para web.

Con Python podemos realizar peticiones HTTP utilizando el módulo `requests`, y luego analizar las respuesta que nos da el servidor, igual que haríamos con las developer tools de un navegador, o con herramientas como Postman, con la diferencia de que podemos automatizar todo el proceso y scriptar las peticiones y como responder a ellas.

Este endpoint devuelve una lista de usuarios en formato JSON:

[Este endpoint](https://dummyjson.com/users)

Tu tarea es realizar un script que haga una petición a este endpoint y muestre en pantalla el nombre de todos los usuarios, luego, guarda esos nombres en un archivo.


