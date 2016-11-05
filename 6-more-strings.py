#"Imprime string de texto
print "Mary had a little lamb"
#"Imprime string de texto, llama al string "snow" que declaramos al final de la linea. No es una variable sino un string
print "Its fleece was white as %s." % 'snow'
# imprime texto
print "And everywhere that mary went"
#Imprime el string "." diez veces seuidas

print "." * 10 # what'd that do ?

#Declaramos 12 variables, una por cada caracter de la palabra cheese burguer
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#Whatch that comma at theend, try removing to see whathappens

# Y llamamos a cada una de esas variables todas juntas, formando la palabra.
# Con coma lo imprime todo en la misma linea "Cheese burger",  Sin coma lo imprime en lineas differentes 
#cheese
#burger

print end1 + end2 + end3 + end4 + end5 + end6
print end7 + end8 + end9 + end10 + end11 + end12

#Esto se hace así, en dos lineas, porque en python se considera un mal estilo hacer lineas de mas de 80 caracteres