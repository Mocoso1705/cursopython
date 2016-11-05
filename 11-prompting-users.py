# -*- coding: utf-8 -*-
#Todo script lo abrimos con el string de utf8 para evitar problemas con los caracteres raros, como ñ etc


# Otra forma de pedir input al usuario es generando un prompt
#Para hacerlo declaramos la variable y decimos que es igual a raw_input con el prompt dentro de la funcion.

age = raw_input("How olf are you?")
height = raw_input("How tall are you?")
weight = raw_input("How much do you wight?")

print "So, you're %r old, %r tall and %r heavy," % (age, height, weight)

OK = raw_input("ok>")
print "%s" %(OK)


#Con pydoc podemos ver una especia de "man" para funciones de python. Si quisieramos por ejemplo ver la documentacion de la funcion raw_input deberiamos ejecutar pydoc raw_input
