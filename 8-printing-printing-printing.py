# -*- coding: utf-8 -*-
#Todo script lo abrimos con el string de utf8 para evitar problemas con los caracteres raros, como ñ etc


#Comentario
#Here's some new strange stuff, remember type it exactly

#Declara la variable Days, es un string largo con espacios
days = "Mon Tue Wed Thu Fri Sat Sun"

#Lo mismo pero con saltos de linea, el \n imprimira en un nuevo renglon cada string.
#El \ sirve en python tambien para escapar caracteres especiales.
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

#Imprimimos texto y las variables, con el coma hara que se imprima en el mismo renglon

print "Here are the days: ", days
print "Here are the months: ", months

#Con tres comillas dobles abrimos un texto de multiples lineas. Termina cuando tiramos otras 3 comillas para cerrar.
print """
There's something going on here
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
