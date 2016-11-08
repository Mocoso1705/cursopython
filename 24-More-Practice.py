# -*- coding: utf-8 -*-
#Todo script lo abrimos con el string de utf8 para evitar problemas con los caracteres raros, como ñ etc

#imprime texto
print "Let's practice everything."
#Juega con el escape de las comillas, ya que se abrio el string con comilla simple, las comillas simples van escapadas. Despues hace un salto de linea y un tab
print 'You\'d need to know \' bout escapes with \ that do \n newlines and \t tabs.'

#Declara la variable poem usando comillas triples, que toman el valor hasta que cierra. Juega con los tabs y los saltos de linea
poem = """
\tThe lovely world
with logic so firmly planted
cannot discenr \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twehere there is none.
"""
#Imprime linea
print "-----------"
#Imprime el contenido de la variable poema
print poem

#Imprime linea
print "-----------"

#Hace que el valor de la variable five sea el resultado de una operacion aritmetica.
five = 10 - 2 + 3 - 6
#Imprime un string llamando el valor de five como string de texto
print "This should be five: %s" % five

#Crea la funcion secret_formula que recibira un argumento, se guardara para la funcion como la variable started.
# Declara variables que seran el resultado del argumento pasado por alguna operacion. 
# La funcion Devuelve mas de un valor, en este caso devuelve 3 variables

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

#Define la variable start_point que sera el argumento de la funcion secret_formula
start_point = 10000

#Declara las 3 variables a la vez llamando a la funcion (que tiene como salida 3 resultados )
beans, jars, crates = secret_formula(start_point)

#Imprime y dice que startpoint es un valor decimal.
print "with a starting point of: %d" % start_point
#Imprime las variables que salieron de la funcion como decimales %d
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

#Hace que startpoint sea el mismo valor sobre 10. Podria hacerse con shorthand asi
#startpoint /= 10
start_point = start_point / 10
#Imprime texto
print "We can also do that this way:"
#Imprime, llama como valores decimales y en vez de variables llama a la funcion. Nice!
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)



