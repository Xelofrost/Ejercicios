const express = require('express');
const {exec} = require('child_process');
const { stdout, stderr } = require('process');
const app = express();

app.use(express.static("public"))
app.use(express.urlencoded({extended:true}))
app.use(express.json())

app.post("/ping", (req, res) => {
    const host = req.body.host
    exec(`ping -c 4 ${host}`, (error, stdout, stderr) => {
        if (error) {
            console.log("Se produjo un error al ejecutar el comando");
            return res.status(500).send("Se produjo un error al ejecutar el comando");
        }
        
        if (stderr) {
            console.log(`Se produjo un error en la salida estándar: ${stderr}`);
            return res.status(500).send(`Se produjo un error en la salida estándar: ${stderr}`);
        }

        // Si todo va bien, devuelve el resultado del ping
        res.send(stdout);
    });
});

app.listen(3000,() => {
    console.log("Servidor iniciado en el puerto 3000")
})