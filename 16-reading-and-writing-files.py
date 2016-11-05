# -*- coding: utf-8 -*-
#Todo script lo abrimos con el string de utf8 para evitar problemas con los caracteres raros, como ñ etc


#Metodos o funciones que podemos darle a un fileobject

# - close: Cierra el archivo. Similar a guardar/save
# - read: Lee el contenido de un archivo. Se puede asignar el resultado a una variable
# - readline: Lee solo una lina de un archivo de texto
# - truncate: Vacia el archivo, lo deja en blanco. 
# - write('sarasa'): escribe "sarasa" en el archivo-


#Importamos los argumentos con el package sys
from sys import argv

#El nombre del archivo lo referenciaremos con la variable script y con filename el primer argumento.
script, filename = argv

#Imprimimos y usamos la variable filename como raw que se usa para debuging (%r)
print "We're going to erase %r." % filename
#Imprimimos texto
print "If you dont want that, hit CTRL-C ¨(^C)."
#Imprimimos texto
print "If you do want that, hit RETURN."
#Pedimos accion del usuario con raw input. el prompt será ?. No se guarda en ninguna variable. Es solo para que pueda cancelar o seguir. Apretemos lo que apretemos seguirá
raw_input("?")

#Imprimimos texto
print "Opening the file..."
#Creamos el fileobject en la variable target. EL w es para que podamos escribir en el archivo, sin declarar la w abrira el archivo como read only y no podremos hacer write. Esto se supone que ya por default hace un truncate al archivo si existe..
#Podriamos hacer (filename, 'a') para hacer append.
#Di no declaramos el modo, el default es 'r' o Read only
#Si quisieramos abrir un binario, seria con 'b'
#Si quisieramos abrir un fileobject como readwrite, no solo write, deberiamos agregarle un mas
# Es decir 'w+' o 'a+' )

target = open(filename, 'w') #Para borrar y escribir (como > en bash)
#target = open(filename, 'a') # Para seguir escribiendo un archivo que exista ( como >> en bash)

#Imprimimos texto
print "Truncating the file. Goodbye"

#Borramos todo lo que tenga el archivo llamando el motodo o funcion truncate al fileobject target. Si el archivo no existe, lo creara. Si abrimos el fileobject con (filename, 'w') ya le hace un truncate, y si elegimos append (filename, 'a') no tiene sentido borrarlo. Por lo que esta linea esta medio al pedo...
target.truncate()

#Imprimimos texto
print "Now i'm going to ask you for three lines."

# Tomamos del usuario a traves de raw_input los contenidos que volcaremos al archivo. Los guardarmos en las variables line1 line2 y line3
line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

#Imprimimos texto en pantalla.
print "I'm going to write these to the file." 

#Escribimos en el fileobject las variables que tomamos y \n para salto de linea. Si no ponemos salto de linea quedara todo en el mismo renglon (como en el ejemplo)

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
target.write("esto es ")
target.write("una prueba para ver ")
target.write("si queda en el mismo renglon \n ")

#Ahora hacemos lo mismo pero llamnando el write una sola vez. 
#Primero delaramos la variable salto para el satlo de linea
SALTO = "\n"

#Y ahora llamamos el  target write con 3 comillas. Prestar mucha atencion a los parentesis. Los parentesis de llamado de las variables quedan adentro del parentesis del target.write.
target.write("%s Contenido del target.write en una sola linea: %s %s %s %s %s %s %s" % (SALTO, SALTO,line1, SALTO, line2, SALTO, line3, SALTO))


#Imprimios texto en pantalla
print "And finally, we close it"

#Y cerramos.
target.close()

#Agregamos una muestra al final con el contenido del archivo. 
#Como lo cerramos (ademas de que lo habiamos abierto como w sin el +, por lo que no ibamos a poder leerlo) tenemos que crear el fileobject de nuevo con permiso de lectura.
target = open(filename)
print " "
print "-----------"
print "EL archivo quedo así"
#Llamamos al fiileobject con la funcion read.

print target.read()
#Y cerramos el fileobjet de nuevo.
target.close()