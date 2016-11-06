# -*- coding: utf-8 -*-
#Todo script lo abrimos con el string de utf8 para evitar problemas con los caracteres raros, como ñ etc

#Definimos la funcion cheese and crackers, que tomara dos argumentos. Esos argumentos seran referidos como variablesm, en este caso cheese_count y boxes_of_crackers, dentro de la funcion
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	#Imprimimos haciendo referencia al primer argumento, tomando la variable cheese_count. La imprimimos con el formatter %d para numero (Signed integer decimal).	
	print "You have %d cheeses!" % cheese_count
	#Lo mismo pero con la variable boxes_of_cracker
	print "You have %d boxes of crackers!" % boxes_of_crackers
	#Imprimimos text
	print "Man that´s enough for a party!"
	#Imprimimos texto con salto de linea al final \n
	print "Get a blanket.\n"

#Imprimimos texto
print "We can just give the function numbers directly:"
#Llamamos a la funcion dandole como argumentos dos numeros "hardcodeados"
cheese_and_crackers(20, 30)

#Imprimimos texto
print "OR, we can use variables from our script"

#Definimos las variables amount_of_cheese y amount_of_crackers con los valores 10 y 50 respectivamente

amount_of_cheese = 10
amount_of_crackers = 50


#Llamamos a la funcion cheese_and_crackers pasandole como argumento las dos variables declaradas recien
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#Imprimimos texto
print "We can even do math inside too:"
#Llamamos a la funcion cheese_and_crackers pasandole como argumentos valores "harcodeados" En este caso el primer argumento será el resultado de la suma antes de la coma (10 + 20, es decir, el primer argumento sera 30) y el segundo argumento sera el resultado de 5 + 6, es decir 11
cheese_and_crackers(10 + 20, 5 + 6)

#Imprimimos texto
print "And we can combine the two, variables and math"

#Llamamos a la funcion pasandole como argumento el resultado de la suma entre las variables y un numero que definimos. En este caso, amount_of_cheese era 10 y le sumamos 100, por lo que el argumento primero sera 110. En el segundo caso amount_of_crackers lo definimos como 50, por lo que el argumento que tomara la funcion sera 1050
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print "--------------------\n"
print "\n"
print " Ahora vos batime la justa amigo\n"
print "\n"

#O podriamos hacer que el usuario ponga cual es la cantidad de queso que tiene
# Dado que lo que queremos es que ponga un valor y despues  haremos sumas y restas, tenemos que aclarar que el raw_input es un numero y no un string
# Esto no funcionara porque cuando trate de sumarlo lo tomara como texto
#       amount_of_cheese = raw_input("Cuanto queso tenes?")
#Hay que llamarlo así, encerrado en  int( ):

amount_of_cheese1  = int(raw_input("Cuanto queso tenes?"))
amount_of_crackers1 =  int(raw_input("Cuantas crackers tenes?"))

#Llamamos a esa funcion con el valor que introdujo el usuario
cheese_and_crackers (amount_of_cheese1, amount_of_crackers1)

print "\n"
print "LA MULTIPLICACION DE LOS PANES, por un milagro ahora tenes"
cheese_and_crackers(amount_of_cheese1 * 100, amount_of_crackers1 * 500)


#Ahora para el ejercicio escribimos una nueva funcion

#Funcion hecha para el ejercicio.

#Definimos funcion, toma un solo argumento
def preguntarausuario(pregunta):
	#Imprimimos al usuario
	print "Por favor responda la siguiente pregunta:\n"
	# con raw_input Hacemos que la variable respuesta sea la respuesta del usuario al argumento que se le envio a la funcion. Lo tomara como string, no como valor decimal ya que sino deberiamos usar int(raw_input(pregnta))
	respuesta = raw_input(pregunta)
	#Imprimimos texto y la variable con la respuesta del usuario
	print "no, no son %s" % respuesta
	#Imprimimos texto
	print "Igual vamos a guardar tu respuesta en nuestra super base de datos para sacar estadisticas"
	#Definimos la variable base, que es el archivo donde guardaremos la variable respuesta. En este caso el archivo es base.txt
	base = "base-curso-python-ej19.txt"
	#Creamos el file object dbfile, lo abrimos con append para que agregue el valor y no borre lo que ya existe
	dbfile = open(base, 'a')
	#Escribimos la respuesta del user en el archivo como string de texto. Ponemos tambien un salto de linea porque sino todas las respuestas se van poniendo en el mismo renglon.
	dbfile.write("%s\n" % (respuesta))
	#Cerramos el archivo para guardar los cambios
	dbfile.close()

#Definimos el argumento que le pasaremos a la funcion

argumento = "Cuantos pares son tres botas?"

# Y llamamos a la variable con esa pregunta.
preguntarausuario(argumento)

