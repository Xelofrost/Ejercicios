# Google Dorks

Estos son 5 de los google dorks más interesantes que he encontrado en Exploit Database.

## 1- intext:"siemens" & inurl:"/portal/portal.mwsl" 

Esta pequeña búsqueda nos permite encontrar páginas web de TIA portal, la herramienta principal de paneles de control de los PLCs de siemenes, que no hayan sido aseguradas correctamente, dandonos acceso a la configuración de los PLCs llegando incluso a permitirnos apgarlos remotamente.

Algunas de las webs más interesantes encontradas con este dork fueron:

- http://200kw-man01.dyndns.org/Portal/Portal.mwsl

- https://185.156.235.214/awp/mainPage.html

- https://gemeinschaftweener2.spdns.org/awp//index.html

## 2- intitle:index of /etc/ssh

Con esto encontramos directorios que tengan la configuración de su ssh en la carpeta /etc/ lo cual suele ser muy común, dandonos acceso a explorar estas configuraciones y sacar las llaves ssh y simplemente ver como tienen configurado su servidor ssh.

Algunas de las webs más interesantes encontradas con este dork fueron:

- http://www.vcebhopal.ac.in/a/-/-/etc/ssh/
- https://moocbash.univ-reunion.fr/sys/fs/etc/ssh/

## 3- intitle:"Webcam" inurl:WebCam.htm 

Este dork nos permite acceder a webcams públicas que contengan WebCam.htm en su nombre, permitiendonos ver lo que estas cámaras retransmiten.

Algunas de las webs más interesantes encontradas con este dork fueron:

- http://83.136.176.21/webcam.htm

- https://www.manlleu.cat/webcam.htm

- http://ohlonetrail.net/webcam.htm

## 4- inurl:pastebin intitle:mastercard

Este puede ser uno de lo más interesantes de la lista, ya que con esto buscamos en pastebin (paginas web donde se almacena información en texto plano) datos que contengan en el título "mastercard", llevandonos a información de tarjetas de crédito robadas y posteadas en estos sitios.

Algunas de las webs más interesantes encontradas con este dork fueron:

- https://pastebin.com/aTdetqBG
- https://pastebin.pl/view/af3cd274

## 5-  inurl:"folderview?id=" site:drive.google.com 

Finalmente, este dork nos permite buscar carpetas privadas en google drive.

Algunas de las webs más interesantes encontradas con este dork fueron:

- https://drive.google.com/drive/folders/0BxsQ108is142Q1dMcVNUc3J2U28?resourcekey=0-XwmgHFNhC8nD_H950uK1nA
- https://drive.google.com/drive/folders/0B87bmmJLaLIgfjcxYVVqSF9YVnpjcmh6M2dfVkRfYWNUb2tUNE5rRDl0QXR5bVpoa3hwTUk?resourcekey=0-daUOSJ8LWvKJIDh9byw7AQ