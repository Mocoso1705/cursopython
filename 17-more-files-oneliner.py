# -*- coding: utf-8 -*-
#Todo script lo abrimos con el string de utf8 para evitar problemas con los caracteres raros, como ñ etc

#Importamos los argumentos del MODULO  sys
from sys import argv
script, from_file, to_file = argv

#En este ejercicio aprendemos que podemos poner ; en vez de lineas nuevas

#Creamos el fileobject in_file, abriendo como solo leactura el parth del archivo contenido en la variable from_file
#Hacemos que la variable indata sea el contenido del archivo, haciendo que el valor de indata sea un metodo o funcion de lectura sobre el fileobject in_file
#Creamos el fileobject to_file en modo write para poder escribir.
#escribimos en out_file (que es un fileobject en modo w creado con la variable to_file) el contenido de indata (que era un read del fileobject in_file creado con la variable from_file)
#Cerramos los fileobjects para que se guarde todo.

in_file = open(from_file); indata = in_file.read(); out_file = open(to_file, 'w'); out_file.write(indata); out_file.close(); in_file.close()



#Imprimimos texto a consola
print "Alright, all done"



