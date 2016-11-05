# -*- coding: utf-8 -*-
#Todo script lo abrimos con el string de utf8 para evitar problemas con los caracteres raros, como ñ etc


#Utilizamos el modulo sys e importamos los argumentos
from sys import argv
#Declaramos que el  nombre del script sera la variable "script" y el primer argumento "User_name"
script, user_name, apellido = argv
#Definimos la variable "prompt" como un mayor. Lo usaremos con raw_input
prompt = '> '
#Imprime tomando las variables user_name y script como string (%s)
print "Hi %s, I'm the %s script" % (user_name, script)
#imprime
print "I'd like to ask you a few questions."

#Para el Study drill, agregamos un argumento (apelido) y ahora la usamos para la pregunta. 
print "Es %s tu apellido, %s?" %(apellido, user_name)
respuesta = raw_input(prompt)
#Imprime usando la variable user_name como string (%s)
print "Do you like me %s?" % user_name

#Pide que el usuario teclee la respuesta. El prompt sera > por haber declarado la variable prompt asi y lo que ponga el user lo guardara en la variable likes
likes = raw_input(prompt)

#Imprime usando la variable user_name como string (%s)

print "Where do you live %s?" % user_name
#Pide que el usuario teclee la respuesta. El prompt sera > por haber declarado la variable prompt asi y lo que ponga el user lo guardara en la variable lives

lives = raw_input(prompt)

#Imprime 
print "What kind of computer do you have?"
#Pide que el usuario teclee la respuesta. El prompt sera > por haber declarado la variable prompt asi y lo que ponga el user lo guardara en la variable computer
computer = raw_input(prompt)

#Imprime un texto largo utilizando las triples comillas. Usa strings raw (%r) que se usan para debugin. LLama a las variables definidas por el prompt del user likes, lives y computer. Agregamos las lineas en espanol para el studydrill
print """
Alright, so you said %r about liking me.
Dijiste que %r  %r es tu apellido 
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, apellido, respuesta, lives, computer)
