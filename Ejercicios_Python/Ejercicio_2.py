import sys
#En el segundo ejercicio debemos de hacer un cifrado propio que siga las siguientes sustituciones:
#O-->0/I-->1/E-->3/A-->4/S-->5/G-->6/T-->7/B-->8/g-->9
'''
mensaje = str(sys.argv[1])
alfabeto="OIEASGTBg"
clave = "0123456789"
for i in range (len(clave)-1):
    mensaje_cifrado=mensaje.replace(alfabeto[i],clave[i])
 #   print(mensaje[i])
 #   print(clave[i])
print(mensaje_cifrado)
'''
mensaje = str(sys.argv[1])
diccionario_sust={'O': '0','I': '1','E': '3','A':'4','S':'5', 'G': '6', 'T':'7', 'B':'8', 'g':'9'}
def convertidor(texto):
    cifrado=""
    for letra in texto:
        if letra in diccionario_sust:
            cifrado += diccionario_sust[letra]
        else:
            cifrado += letra
    return cifrado

print(convertidor(mensaje))
