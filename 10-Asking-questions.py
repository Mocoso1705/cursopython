# -*- coding: utf-8 -*-
#Todo script lo abrimos con el string de utf8 para evitar problemas con los caracteres raros, como ñ etc
#
#
#Imprime la pregunta
print "How old are you?"
#Hace que la variable age tenga el valor tomado de lo que ponga el usuario (funcion raw_input)
age = raw_input()
#Imprime la pregunta
print = "How tall are you?"
#Hace que la variable height tenga el valor tomado de lo que ponga el usuario (funcion raw_input)
height = raw_input()
print "How much do you weight?"
#Hace que la variable weight tenga el valor tomado de lo que ponga el usuario (funcion raw_input)
weight = raw_input()

#Imprime el texto utilizando las variables que puso en usuario en raw, sino deberia ser %s. Luego llama a las variables a imprimir.

print "So, you are %r old, %r tall and %r heavy" % ( 
	age, height, weight)

#Por default raw_input toma el input del usuario como string. Si quisieramos hacer operaciones aritmeticas con el dato introducido por el user tendriamos que poner int(raw_input()). Sigue tomando el string como string, pewro lo convierte a int con la funcion int()

print "POne un numero"
numero1 = int(raw_input())
print "Ahora pone otro numero"
numero2 = int(raw_input())
print "Si los sumamos da", numero1 + numero2
print "Si los restamos da" numero1 - numero2
