const express = require('express');

const app = express();

app.use(express.static("public"))

app.use(express.urlencoded({extended:true}))

let lista = ["test"]

app.get("/metodos", (req, res)=> {
    console.log("Hola mundo")
    res.send(lista)
})

app.post("/metodos", (req, res)=> {
    lista.push("hola mundo")
    res.send(lista)
})

/*
app.get("/metodos", (req, res) => {
    lista.push(req.query.test); // Añadir el parámetro 'test' directamente a la lista
    res.send(lista); // Devolver la lista actualizada
});
*/



app.delete("/metodos", (req, res)=> {
    lista=[]
    res.send(lista)
})

app.get("/headers", (req, res)=> {
    console.log(req.headers)
    res.send(req.headers)
})


app.get("/url_query", (req, res) => {
    const nombre = req.query.nombre
    const edad = req.query.edad
    const respuesta ={
    nombre, 
    edad
    }
    res.json(respuesta)
})

app.post("/pregunta", (req, res)=>{
    //este endpoint se asegura que el usuario responde 2
    if(req.body.respuestaUsuario == 2){
        res.send("Respuesta correcta")
    }else{
        res.send("Eres mas tonto que las piedras")
    }
        
    console.log("El formulario ha llegado")
})

app.listen(3000,() => {
    console.log("Servidor iniciado en el puerto 3000")
})