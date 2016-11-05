# -*- coding: utf-8 -*-
#Todo script lo abrimos con el string de utf8 para evitar problemas con los caracteres raros, como ñ etc


#Declaro la variable "name" con mi nombre
name = 'Rodrigo Trigo'
#Declara la variable age y hace un comentario al lado
age = 32 #Not a lie
# Declara la variable altura en inches.
height = 68.5   #no acepta con coma,  el %d (como lo llamamos abajo) solo muestra el primer numero
#Declara la variable weight en pounds
weight = 178
#Declara la variable eyes, string de texto
eyes = 'Brown'
#Declara la variable theet, string de texto
theet = 'White'
#Declara la variable hair, string de texto
hair = 'Black'
#convierte la variable height de inches a centimetros  multiplicandolo por 2.54 y lo guarda como la variable en centimetros
en_centimetros = height * 2.54
#convierte la variable weight a kilos dividiendolo por 0.45.. lo guarda como la variable en_kilos
en_kilos = weight  / 0.45359237


#El chiste de este tutorial son los "formatters" characters, es decir esos %d o %s o %f que tenemos abajo. Son los que hacen que determinada variable se muestre de acuerdo a determinado formato, puede ser integro, decimal. 

# La lista completa de Formatrer characters
#  
#  d	Signed integer decimal.	
#  i	Signed integer decimal.	
#  o	Unsigned octal.	(1)
#  u	Unsigned decimal.	
#  x	Unsigned hexadecimal (lowercase).	(2)
#  X	Unsigned hexadecimal (uppercase).	(2)
#  e	Floating point exponential format (lowercase).	
#  E	Floating point exponential format (uppercase).	
#  f	Floating point decimal format.	
#  F	Floating point decimal format.	
#  g	Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise.	
#  G	Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise.	
#  c	Single character (accepts integer or single character string).	
#  r	String (converts any python object using repr()).	(3)
#  s	String (converts any python object using str()).	(4)
#  %	No argument is converted, results in a "%" character in the result.	


#El %r le dice a python "imprimi esto no importa lo que sea"

#Imprime el texto y llama a la variable name con un formatter de string
print "let's talk about %s." % name
#imprime el texto y llama a la variable % height con un formatter de  integro decimal (sin coma)
print "He's %d inches tall." % height

##imprime el texto y llama a la variable % height con un formatter que muestra floating point (con coma)
print "or %f centimeters" % en_centimetros #Si quisieramos que muestre con coma habria que poner %f
#imprime el texto y llama a la variable % height con un formatter de  integro decimal (sin coma)
print "He's %d pounds heavy" % weight
#imprime el texto y llama a la variable % height con un formatter de  integro decimal (sin coma)

print "or %d kilos" % en_kilos # Si quisieramos que sea con coma, pondramos %f
#Comentario texto
print "Esta engordando"
#Imprime el texto y llama dos variables, ambas como strings. Se declara primero una y despues la otra, entre parentesis y separadas por comas

print "He's got %s eyes and %s hair." % (eyes, hair)

#Imprime el texto y llama a la variable name con un formatter de string
print "His theet are usually %s depending on the coffee." % theet

#this line is tricky, and try to get it exactly right

#Imprime el texto y llama cuatro variables, todas como integros decimales. Se declara primero una y despues la otra, entre parentesis y separadas por comas. Luego, en el ultimo %d en realidad es la suma de las otras variables, es decir el ultimo %d es en realidad una operacion sobre variables que se llaman ahi mismo, el %d es el resultado de la operacion y no la variable en si


print "If i add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)


# Por ultimo, si quisieramos redondear un valor, deberiamos usar una funcion
#La funcion es round()  , entonces si quisieramos rendondear 1.7333 deberiamos poner round(1.7333) y el resultado sería 2.
