# -*- coding: utf-8 -*-
""" Este ejercicio esta diseñado para que este archivo sea un modulo
Los modulos no pueden comenzar con numeros, por lo que debemos renombrar el file a algo que comience con letras, como ex25
La idea es cargarlo desde el interptrete de python haciendo \n
\t import ex25 \n
y llamando cada modulo funcion por separado con \n
\t ex25.sort_words() \n
Al final nos dira que podemos cargar todas las funciones de una y cargarlas directamente con\n
\t from ex25 import all.\n
En este ejercicio veremos varios metodos sobre strings. Podemos encontrar mas informacion en 
https://www.tutorialspoint.com/python/python_strings.htm

ESto deberiamos poder leerlo haciendo \n
\t help(ex25) \n
desde el interprete, luego de cargarlo con \n
\timport ex25\n

Lo que recomienda el curso hacer desde la terminal del interprete es:

import ex25
sentence = "All good things come to those who wait."
words = ex25.break_words(sentence)
words
sorted_words = ex25.sort_words(words)
sorted_words
ex25.print_first_word(words)
ex25.print_last_word(words)
words
ex25.print_first_word(sorted_words)
ex25.print_last_word(sorted_words)
sorted_words
sorted_words = ex25.sort_sentence(sentence)
sorted_words
ex25.print_first_and_last(sentence)
ex25.print_first_and_last_sorted(sentence)

----
Besitos
"""
#Definimos la funcion break_words, toma un argumento (stuff)
def break_words(stuff):
	#Comentario de Documentacion
	"""This funcition will break up words for us."""
	#La variable words es el resultado de usar el metodo split sobre la variable stuff. Le decimos que el split lo haga con ' '

	words = stuff.split(' ')
	#Lo que devuelve la variable es el valor de words, es decir stuff pasado por split
	return words

#Definimos la funcion sort_words, toma un argumento que se llamara con la variable words dentro de la funcion
def sort_words(words):
	#Comentario de documentacion
	"""Sorts the words."""
	#La funcion devolvera el contenido de words ordenado alfabeticamente, que es lo que hace la builtin function "sorted". Mas info en https://docs.python.org/2/library/functions.html#sorted
	return sorted(words)

#Definimos la variable print_first_word. Acepta un argumento (words)
def print_first_word(words):
	#Documentacion tecnica
	"""Prints the first word after popping it off."""
	#La variable word sera el resultado de aplicar el metodo pop sobre la variable words, que borra el item en la posicion dada como argumento y devuelve el ultimo item de la lista. Mas informacion en https://www.tutorialspoint.com/python/list_pop.htm
	word = words.pop(0)
	print word

#Definimos la variable, acepta un argumento que sera la variable words
def print_last_word(words):
	#Documentacion tecnica
	"""Prints the last word after popping it off."""
	#Llamamos al mismo metodo que en la funcion anterior pero cambiando el valor que se le pasa. Si ponemos numeros toma la lista en orden empezando de 0 (3 elimina la 4ta palabra, etc). -1 es el ultimo
	word = words.pop(-1)
	#Imprime valor word
	print word
#Definimos funcion, tomara un argumento guardad en la variable sentence
def sort_sentence(sentence):
	#Documentacion tecnica
	"""Takes in a full sentence and returns the sorted words."""
	#El valor de words será igual a llamar a la funcion break_words (que declaramos al principio) . Luego utilizaremos la otra funcion que declaramos (sort_words) sobre la variable words y nos devolvera eso como salida de la funcion
	words = break_words(sentence)
	return sort_words(words)

#Definimos la funcion print_first_and_last, que tomara un argumento guardado en la variable sentence
def print_first_and_last(sentence):
	#Documentacion tecnica
	""" Prints the first and last words of the sentence."""
	#La variable words sera el resultado de llamar la funcion break_words que declaramos antes sobre el argumento
	words = break_words(sentence)
	#Aplicamos dos funciones que declaramos antes
	print_first_word(words)
	print_last_word(words)

#Muy similar a la anterior. Seteamos variable y llamamos funciones desde esta misma funcion
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)



