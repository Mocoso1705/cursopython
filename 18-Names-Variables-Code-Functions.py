# -*- coding: utf-8 -*-
#Todo script lo abrimos con el string de utf8 para evitar problemas con los caracteres raros, como ñ etc

#Funciones!!!
#Un poco de teoria.
#Una funcion hace tres cosas.
#Le dan nombre a un pedazo de codigo asi como las variables le dan nombre a los valores string y numericos
#Toman argumentos como los scrits toman argv
#Usando el pedazo de codigo y el argumento que le pasamos funcionan como si fueran un mini-script o un pequeño comando

#En python la funcion se crea declarandola con "def"
#El comentario de abajo es del curso, no mio.

#this one is like your scripts with argv

#Le decimos a python que queremos hacer una funcion usando "def" que viene de define
#en la misma linea que def le damos nombre a la funcion, aca se llama print_two.
# Despues le decimos que¨queremos que el argumento sea *args, es decir, todo lo contenido en la variable args, que como veremos abajo es mas de un elemento. Tiene que ir entre parentesis.
#La linea debe terminar con dos puntos, y ahi empezamos a "indentar" es decir, a escribir con sangria
#La funcion termina cuando deidentamos, es decir, cuando dejamos de escribir con esos cuatro espacios
def print_two(*args):
	#el codigo que es parte de la funcion se escribe con 4 espacios (o un tab) debajo de la declaracion de la funcion	
	#La variable args esta compuesta de dos variables. arg1 y arg2. Hacemos un "unpack" como hacemos con los scripts. Es decir, la funcion espera recibir como argumentos dos elementos.
	 arg1, arg2 = args
	 #Imprimimos en pantalla arg1 y arg2.
	 print "arg1: %r, arg2: %r" % (arg1, arg2)



#El comentario de abajo es del curso, no mio.
#ok, that *args is actually pointless, we can just do this

#Esta funcion es igual a la anterior, pero sin necesidad de hacer un unpack ya que los dos elementos a imprimir estan dentro del parentesis.
#REcordemos el dos puntos despues del cierre del parentesis

def print_two_again(arg1, arg2):
 print "arg1: %r, arg2: %r" % (arg1, arg2)


#El comentario de abajo es del curso, no mio.
#this one takes one argument

#Esta funcion espera solo un argumento y lo imprime.
def print_one(arg1):
	 print "arg1: %r" % arg1

#El comentario de abajo es del curso, no mio.
# this one takes no arguments

#Y esta funcion solo imprime texto, no recibe argumentos.
def print_none():
	print "I got nothin'."

#Ahora le pasamos argumentos (entre parentesis) a las funciones que declaramos antes
#Le pasamos dos argumentos a las funciones que esperan dos argumentos, uno a la que esperan uno, y ninguno  a la que no espera argumentos.

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

#Imprimimos texto
print "Que pasa si le pasamos argumentos a algo que no lo espera?"
#Le pasamos el argumento sarasa a print_none que no espera argumentos. Los argumentos van entre parentesis
#print_none("sarasa")
print "FALLA!"


print "Y si le pasamos dos argumentos a algo que espera 1?"

#print_one("Tu vieja"," Tu hermana")
print "FALLA!"


print "Ahora le pasamos uno a algo que espera dos!"

#print_two("PepeLui")
print "FALLA!"




#Checklist  para ver si creamos una funcion correctamente

# - Empezamos la funcion con def ?
# - El nombre de la funcion tiene solo caracteres y _ (guion bajo / underscore)
# - Abrimos parentesis "(" despues del nombre de la funcion?
# - Pusimos argumentos despues del parentesis separados por comas en caso de que sea mas de uno?
# - Hicimos que cada argumento sea unico, es decir que no lo repetimos entre si o con otras variables del script o modulos que llamemos?
# - Cerramos el parentesis despues de declarar los argumentos?
# - Identamos (sangria) todas las lineas de codigo  que estan dentro de la funcion usando 4 espacios o un tab (no mas, no menos)
# - Terminamos la funcion volviendo a escribir sin sangria (deindent) ?

#Cuando usemos o "llamemos" a una funcion chequeemos lo siguiente

# - Llamamos o usamos la funcion tipeando su nombre?
# - Abrimos parentesis despues del nombre de la funcion para ejecutarla?
# - Pusimos el valor que queremos dentro del parentesis, encomillandolos y separandolos con comas si es mas de uno?
# - Cerramos el parentesis despues de listar los argumentos?

# Ejecutar, llamar o usar una funcion, quieren decir lo mismo.

