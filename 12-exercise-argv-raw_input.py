# -*- coding: utf-8 -*-
#Todo script lo abrimos con el string de utf8 para evitar problemas con los caracteres raros, como ñ etc


from sys import argv
script, argumento = argv
PREGUNTA = raw_input("El argumento usado es tu edad?")
print " Veo que respondiste: %s.Ok, Gracias" % PREGUNTA

