#!/bin/bash

# Eliminar informe.pdf si existe
rm -f informe.pdf

# Declarar array con los nombres de los capítulos
capitulos=("intro.md" "ejemplo1.md" "ejemplo2.md")
margen="2cm"

# Convertir cada archivo markdown a PDF
for capitulo in "${capitulos[@]}"; do
    echo "Creando PDF de $capitulo"
    pandoc "$capitulo" -o "${capitulo%.md}.pdf" --variable classoption=oneside --variable fontsize=12pt --variable linkcolor=blue --variable urlcolor=blue --variable geometry:margin="$margen" --include-in-header config.tex
done

# Crear el PDF del informe completo
echo "Creando PDF de todo el informe"
#pdftk 1_ejercicio.pdf 2_ejercicio.pdf 3_ejercicio.pdf cat output informe.pdf
pdftk intro.pdf ejemplo1.pdf ejemplo2.pdf cat output informe.pdf

# Eliminar PDFs temporales
for capitulo in "${capitulos[@]}"; do
    rm "${capitulo%.md}.pdf"
done

# Concatenar los archivos markdown en README.md
> README.md
for capitulo in "${capitulos[@]}"; do
    cat "$capitulo" >> README.md
done

echo "Informe creado en informe.pdf"

# ejecutar con bash generar-pdf.sh