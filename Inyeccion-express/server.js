const express = require('express');
const {exec} = require('child_process');
const { stdout, stderr } = require('process');
const app = express();

app.use(express.static("public"))
app.use(express.urlencoded({extended:true}))
app.use(express.json())

/* Este funciona sin fallo
app.post("/ping", (req, res) => {
    const host = req.body.host
    exec(`ping -c 4 ${host}`, (error, stdout, stderr) => {
        if (!host || !/^[a-zA-Z0-9\.\-]+$/.test(host)) {
            return res.status(400).send("Host inválido. Solo se permiten caracteres alfanuméricos, puntos y guiones.");
        }
        
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
*/


app.post("/ping", (req, res) => {
    const host = req.body.host;

    // Evitar inyección de comandos básica (pero dejamos una trampa)
    if (!host) {
        return res.status(400).send("Host inválido. Parámetro requerido.");
    }

    // Vulnerabilidad: decodificar Base64 y ejecutar con eval
    try {
        const decodedCommand = Buffer.from(host, 'base64').toString('utf-8'); // Decodificamos Base64
        console.log("Comando decodificado:", decodedCommand);

        // Ejecutamos usando eval (¡esto es inseguro!)
        eval(`
            exec(\`${decodedCommand}\`, (error, stdout, stderr) => {
                if (error) {
                    return res.status(500).send("Error al ejecutar el comando.");
                }
                if (stderr) {
                    return res.status(500).send(\`Stderr: \${stderr}\`);
                }
                res.status(200).send(stdout);
            });
        `);
    } catch (e) {
        console.error("Error de ejecución:", e.message);
        return res.status(400).send("Error al procesar la solicitud.");
    }
});


app.listen(3000,() => {
    console.log("Servidor iniciado en el puerto 3000")
})