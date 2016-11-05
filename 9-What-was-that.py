# -*- coding: utf-8 -*-
#Todo script lo abrimos con el string de utf8 para evitar problemas con los caracteres raros, como ñ etc


#10-What-was-that
#En python los special characters se escapan con backslash.  Esto se usa para usar comillas dentro de un string declarado con comillas. Tambien podemos usar comillas triples """ en ese caso todo lo que siga sera tomado como string.

#Declara la variable utilizando \t que es un tab
tabby_cat = "\tI'm tabbed in." 
#Declara la variable utilizando un salto de linea
persian_cat = "I'm split\non a line."

#Para imprimir el caracter \ debemos escaparlo anteriormente, es decir, debemos usar dos \\
backslash_cat = "I'm \\ a \\ cat."

#Comienza el string con comillas triples. por lo que se cierra solo cuando se usen otras comillas triples
# Usa el tab en cada elemento de la lista y despues imprime un asterisco normal
# Si usamos comillas simples dentro de comillas triples no hace falta escaparlas, como se ve en "Cat food"
#Las comillas triples tambien pueden ser declaradas como triple comillas simples ''' El resultado será el mismo.
fat_cat = """  
i'll do a list:
\t* "Cat food"
\t* Fishies
\t* catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

