# -*- coding: utf-8 -*-
#Todo script lo abrimos con el string de utf8 para evitar problemas con los caracteres raros, como ñ etc


#Declaramos cuatro funciones similares
#Toman ds argumentos. Los declaran como variables a y b dentro de la funcion. Luego imprimen que operacion van a usar usando strings decimales (%d)
#Finalmente hacen que nos retorne el valor de la operacion aritmetica entre a y b. Cuando llamemos a esta funcion desde una variable, ese return sera lo que se convierta en el valor de la variable. Es la "salida" de la funcion
def add(a,b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a,b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

#Imprimimos texto

print "Let's do some math with just functions!"

#LLamamos a las distintas funciones desde las variables. Lo que pasara es que el valor que de el return se convertira en el valor asignado a la variable.
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100,2)

#Imprimimos esas variables que son el resutlado de la funcion
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

#A puzzle for the extra credit, type it anyway.

#Imprimimos
print "Here is a puzzle."

# El valor de what se sacara siguiendo los parentesis. 

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
#Si podemos, hay que seguir los parentesis. seria iq ( que era 50) / 2 = 25. Despues wheight (180) * el resultado anterior (50)
#Eso da 4500, Despues le sacamos height (74 ), dando negativo 4426 y le sumamos age (35). Eso da 4391

# Imprime texto con el valor de what en el medio
print "That becomes: ", what, "Can you do it by hand?"

#Test mio, imprimimos texto
print "Y aca deveriamos ver un 35"
#Y imprimimos el return de la funcion.
print add(30, 5)


#Escribiendo funciones propias

def pedirinputnumero():
	print "\nPor favor ingresa un numero"
	arg = int(raw_input(">"))
	return arg

def pedirinputnumeroflotante():
	print "\nPor favor ingresa un numero con coma" 
	print "(y cuando digo coma es un punto, viscomo es la dominacion cultural)"
	arg = float(raw_input(">"))
	# print "TEST ARG %f" % arg la funcion define oka el numero con coma
	return arg

def pedirinputstring():
	print "\nPor favor ingresa un string de texto"
	arg = raw_input(">")
	return arg


def mayorigual(arg):
	print "el argumento recibido es %f, y es un numero porque sino se hubiese colgado" % arg
	print " A mi me gusta mucho el numero 100"
	print "veamos si %f es mayor o igual que 100" % arg
	return arg >= 100.0


usuario = pedirinputnumero()
resultado = mayorigual(usuario)
print resultado

usuario = pedirinputnumeroflotante()
resultado = mayorigual(usuario)
print resultado

print "\n"
print "\n Terminamos, queres decirme algo?"
usuario = pedirinputstring()

print "Eso que me decis, a saber:"
print "%s" % usuario
print " Habla mas de vos que de mi"
