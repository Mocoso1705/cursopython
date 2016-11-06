# -*- coding: utf-8 -*-
#Todo script lo abrimos con el string de utf8 para evitar problemas con los caracteres raros, como ñ etc

#La idea es lanzar este script utilizando como argumento un archivo de texto, 20-lista.txt compuesto de 5 lineas que dicen "Esta es la linea 1" "Esta es la linea 2" y así.

#Del modulo sys importamos los argumentos
from sys import argv

# Definimos que el nombre del arhivo sera referido con la variable script y que se espera un argumento, al que se hacer referencia con la variable  input_file
script, input_file = argv

#Definimos la primera funcion, llamada print all. Esta tomara un argumento al que nos referiremos con la variable f
def print_all(f):
	# Lo que espera como argumento es un fileobject. En este caso imprimiremos el contenido del fileobject ejecutanddo un print y dandole la funcion read al fileobject
	print f.read()

# Igual que el caso anterior, definimos la funcion rewind, espera un argumento que se guarda con la variable f
def rewind(f):
	#Utilizamos la funcion seek sobre el fileobject que viene como argumento de la funcion, dandole un valor de 0 
	f.seek(0)

#Definimos la funcion print_a_line que tomara dos argumentos. Se guardaran como Line_count y 
def print_a_line(line_count, f):
	#Hacemos un print llamando a readline, esto  leera la linea en la que actualmente esta abierto el archivo. En python los archivos se leen de forma lineal, es decir, se lee de donde esta abierto para adelante... Explicamos esto mas abajo.  La variable line_count solo imprime un numero, no modifica de ninguna manera lo que hace el readline.
	print line_count, f.readline()
	# Seria lo mismo si hicieramos lo siguiente, solo que no imprimiria un numero adelante de la linea.
	# print  f.readline()


#Ahora empezaremos a declarar variables que se usaran como argumentos como funciones.
#La primero que haremos sera crear el fileobject current_file, que sera el archivo que se paso como argumento al script y esta contenido en la variable input_file despues del unpack de argv que hicimos al principio
current_file = open(input_file)

#Imprimimos texto
print "first let's print the whole file:\n"

#Llamamos a la funcion print_all dandole como argumento el fileobject current_file
print_all(current_file)

#Imprimimos texto
print "Now let's rewind, kind of like a tape."


#En python los fileobjects son algo asi como un tape, es decir, cada vez que leemos avanzamos hasta cierta posicion dentro del archivo y lo que hagamos sera a partir de ahi. Es decir que si le hacemos un print  read a un fileobject, llegaremos al final y no podremos hacer mucho mas a partir de ahi. Cada lectura fallara. Es por eso que tendremos que decirle a python que vuelva al principio del archivo.

#Primero veamos en que posicion esta el archivo. Como hicimos un read, deberiamos estar al final.
linea = "-----------------"
print linea
print "Ahora estamos en"
print current_file.tell()
#Llamamos a la funcion rewind dandole como argumento el fileobject current_file. Esto pondra el offset en 0, pusiendo volver a leer el archivo desde el principio
print "Rebobinamos..."
rewind(current_file)

print "Y ahora estamos en..."
print current_file.tell()
print linea

#Imprimimos texto
print "let's print three lines:"

#Seteamos la variable current_line a 1, este sera el primer argumento para la funcion print_a_line y se pasara en un print antes de  un readline sobre el fileobject.
current_line = 1

#Llamamos a la funcion print_a_line, primer argumento es current_line (en este momento 1) y current_file, es decir el fileobject creado a partir del argumento pasado al script
print_a_line (current_line, current_file)

#Ahora le agregamos un 1 a current_line, de tal manera que será dos
current_line = current_line + 1

#Llamamos a la funcion print_a_line, el primer argumento sera current_line (ahora 2 ya que le sumamos uno en la linea anterior) y el fileobject current_file.
print_a_line(current_line, current_file)

# le sumamos otro uno a current_line. Ahora quedará en 3
current_line = current_line +1 
#Volvemos a llamar a la funcion print_a_line. El primer argumento será 3 ahora, y el segundo sigue siendo el mismo fileobject.
print_a_line(current_line, current_file)


print "Ahora estamos en"
print current_file.tell()
#Para averiguar
# que hace el seek
# print_a_line, al readline se le pasa un numero antes?

print  current_file.readline()

print "Rebobinamos..."
rewind(current_file)


print  current_file.readline()

# si a readline le damos un argumento en numero, le estaremos diciendo cuantos caracteres queremos que lea. 
print "Imprimamos solo 10 caracteres de la proxima linea"
print  current_file.readline(10)
#readline funciona leyendo desde la posicion en la que este en ese momento hasta que encuentre el proximo salto de linea. Por lo que si lanzamos un readline entero desde aca veremos desde la mitad de la linea hasta su final.
print "Y si llamamos un readline completo desde la mitad de una linea lo que veremos sera"

print  current_file.readline()

#En vez de  aumentar los numeros de las variables llamando a la misma variable y sumandole uno como hacemos aca:
# current_line = current_line +1 
# Podriamos usar shorthand notation. De esa forma le diriamos directamente que haga determinada operacion aritmetica sobre la variable sin tener que llamarla de nuevo. En el caso de current_line hariamos

print "\n"
print "%s\n" % linea
print "Usando Shorthand"
print "%s\n" % linea
print "Valor de currentline ahora es: %r" % current_line
current_line += 1
print "Usamos shorthand. El Valor de currentline ahora es:  %r" % current_line
current_line += 3
print "Usamos shorthand de nuevo. El Valor de currentline ahora es:  %r" % current_line
current_line -= 2
print "Y usamos shorthand otra vez... El Valor de currentline ahora es:  %r" % current_line


