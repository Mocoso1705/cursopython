# -*- coding: utf-8 -*-
#Todo script lo abrimos con el string de utf8 para evitar problemas con los caracteres raros, como ñ etc



#Printing-Printing

#Declaramos una variable llamada formatter, compuesta de cuatro tipos de formatter characters. En este caso todos %r

formatter = "%r %r %r %r"

#Ahora le vamos a pasar a formatter, que define 4 formatters, 4 strings diferentes para que imprima con ese formato
#El primero es numerico
print formatter % (1, 2, 3, 4)
#El segundo strings de texto
print formatter % ("one", "two", "three", "four")
#El tercero es True y False, es reconocido como argumentos por python y pueden usarse para operaciones logicas, por eso no esta entre comillas.
#Si le pusieramos comillas lo convertimos en strings de texto y python lo interpretara como eso.
print formatter % (True, False, False, True)
#el cuarto... formatter! lo que imprimira sera el valor "raw" de la variable, es decir %r %r %r %r
print formatter % (formatter, formatter, formatter, formatter)
#Y el quinto es un array, es decir en realidad declaramos 4 strings distintos compuestos por cuatro palabras. Cada uno de esos strings sera tomado como un string unico e impreso
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	 "But i didn't sing.",
	  "So i said goodnight."
	  )


#  %r da una version raw de una variable. Suele usarse solo para debug. Para el usuario final siempre debe usarse el tipo correcto de formatter (%s, %f, %d) etc

