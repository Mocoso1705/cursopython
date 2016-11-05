# -*- coding: utf-8 -*-
#Todo script lo abrimos con el string de utf8 para evitar problemas con los caracteres raros, como ñ etc

#Importamos los argumentos del MODULO  sys
from sys import argv

#Importa del MODULO os.path la funcion o comando exists, que utilizaremos para verificar si existe o no el archivo
from os.path import exists

#Estos son modulos que ya vienen con python, pero tambien podriamos importar modulos que sean otros scripts en python. Si pusieramos import sarasa y existiera en ese path sarasa.py, lo importariamos.


# Declaramos que el nombre del archivo sera la variable script y que necesita dos argumentos mas, que serán las variables from_file y to_file
script, from_file, to_file = argv

#Imprimimos string ern pantalla referenciando las variables from_file y to_file

print "copying from %s to %s" % (from_file, to_file)

#we could do these on one line, how?

#Creamos el fileobject in_file, abriendo como solo leactura el parth del archivo contenido en la variable from_file
in_file = open(from_file)

#Hacemos que la variable indata sea el contenido del archivo, haciendo que el valor de indata sea un metodo o funcion de lectura sobre el fileobject in_file
indata = in_file.read()

#Este es nuevo. Utilizamos la funcion o metodo "Len" para ver cual es el tanaño de un string, en este caso la variable indata que es el metodo o funcionde lectura sobre el fileobject in_file
print "The input file is %d bytes long" % len(indata)

#Esta funcion  verifica la existencia de un archivo o directorio (esta importada de os.path), en este caso el archivo contenido en el fileobject to_file. Lo que mostrara sera True o False
print "DOes the output file exist? %r" % exists(to_file)

#Imprimimos texto
print "Ready, hit RETURN to continue, CTRL-C to abort"

#Prompt al usuario para verificar o cancelar, sin simbolo de prompt
raw_input()

#Creamos el fileobject to_file en modo write para poder escribir.
out_file = open(to_file, 'w')
#escribimos en out_file (que es un fileobject en modo w creado con la variable to_file) el contenido de indata (que era un read del fileobject in_file creado con la variable from_file)
out_file.write(indata)

#Imprimimos texto a consola
print "Alright, all done"

#Cerramos los fileobjects para que se guarde todo.
out_file.close()
in_file.close()

