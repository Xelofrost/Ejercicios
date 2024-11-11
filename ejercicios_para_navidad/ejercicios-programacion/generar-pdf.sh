#!/bin/bash
# Eliminar informe.pdf si existe
rm -f informe.pdf

# Declarar array con los nombres de los capítulos
capitulos=("ejercicio-1.md" "ejercicio-2.md" "ejercicio-3.md" "ejercicio-4.md" "ejercicio-5.md" "ejercicio-6.md" "ejercicio-7.md")
margen="2cm"

# Convertir cada archivo markdown a PDF
for capitulo in "${capitulos[@]}"; do
    echo "Creando PDF de $capitulo"
    pandoc "$capitulo" -o "${capitulo%.md}.pdf" --variable classoption=oneside --variable fontsize=12pt --variable linkcolor=blue --variable urlcolor=blue --variable geometry:margin="$margen" --include-in-header config.tex
done

