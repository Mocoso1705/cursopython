# -*- coding: utf-8 -*-
#Todo script lo abrimos con el string de utf8 para evitar problemas con los caracteres raros, como ñ etc

#El script necesita que se lo ejecute con un argumento, que debe ser un archivo de texto con algun contenido que imprimira en pantalla

#Importamos los argumentos utilizando el package sys
from sys import argv

# Seteamos que el script espera 1 agrumento (filename) y que el nombre de archivo del script sera referido con la variable script.
script, filename = argv

#Declaramos la variable txt, que lo que hara será crear un fileobject (algo asi como un contenedor del archivo, como si montaramos un dispositivo) al que luego podremos darle instrucciones como read, write, etc.
txt = open(filename)

#Imprimos texto y el valor de filename

print "Here's your file %r:" %filename

#Lllamamos al fileobject que creamos con  open declarada en txt pero con la funcion read. Esto mostrara el  contenido del archivo

print txt.read()

#Si estuvieramos en la consola de python, podemos acceder al contenido direactamente con
#txt.read()
#Pero imprimira de un modo medio "raw". es decir los saltos de linea serán ignorados y veremos \n etc. 

#Imprimimos
print "type the filename again:"

#Le pedimos al user que introduzca con raw_input otro nombre de archivo, lo guardamos en la variable file_again. El prompt que vera el user es un mayo (> )
file_again = raw_input("> ")

#Declaramos la variable txt_again, que lo que hara será crear un fileobject (algo asi como un contenedor del archivo, como si montaramos un dispositivo) al que luego podremos darle instrucciones como read, write, etc.

txt_again = open(file_again)

#Lllamamos al fileobject que creamos con  open declarada en txt_again pero con la funcion read. Esto mostrara el  contenido del archivo

print txt_again.read()

#Cerramos los archivos abiertos.
txt.close()
txt_again.close()
