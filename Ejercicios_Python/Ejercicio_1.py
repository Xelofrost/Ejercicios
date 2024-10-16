import sys
#Para el primer ejercicio debemos convertir cadenas de ARN a cadenas de ADN. Para eso, debemos escribir un programa para
#sustituir las "U" por las "T" en un string gracias al .replace

arn = str(sys.argv[1])

if "U" and "G" and "C" and "A" in arn:
    adn= arn.replace("U", "T")
    print("El arn era: " + arn + "\n" + "El adn resultante es: "+ adn)
else:
    print("No se introdujo un ARN válido")