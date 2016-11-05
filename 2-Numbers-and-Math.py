#Simple print, dice que va a contar sus gallinas
print "I will now count my chickens:" 

#imprime Hens y luego hace 26 mas la division de 30 sobre 6
print "Hens", 25 + 30 / 6  # imprimimos, luego hacemos la operacion. Se imprime al lado del print en pantalla

#Imprime Roosters y despues utiliza modulus. No es porcentaje, sino que lo que hace
# es devolver lo que "sobra" de la operacion entre dos operandos. Dado que python no maneja floating point
# por defecto, no da resultados con coma. Es decir, si hacemos 27 / 5 el resultado sera 5. Si hacemos 11 / 5 el resultado sera 2
# el modulos nos dara lo que sobra, es decir si hacemos 27%5 el resultado sera 2 y con 11%5 el resutado sera 1
print "Roosters", 100 - 25 * 3 % 4

# Imprime que va a contar los huevos
print "Now i will count the eggs:"

#Hace toda la cuenta
#La forma de procesar las cuentas es
# PEMDAS which stands for Parentheses Exponents Multiplication Division Addition Subtraction. (en ese orden)
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

#Imprime la pregunta
print "Is it true that 3 + 2 < 5 - 7 ?"
#Cuando la operacion es si algo es < o > o <= >=, la salida es true
print 3 + 2 < 5 - 7  

#Imprime la pregunta en texto y mestra el resultado de la operacion aritmetica
print "What is 3 + 2 ?", 3 + 2 
#Lo mismo que el anterior
print "What is 5 - 7?", 5 - 7

#Imprime texto
print "Oh, that's why it's false."

#Imprime mas texto
print "How about some more."

#Imprime el texto y luego el resultado del mayor que (true en pantalla)
print "Is it greater?", 5 > -2
#Imprime el texto y luego el resultado del mayor o igual (True en pantalla)
print "Is it greater or equal?", 5 >= -2
#Imprime el texto y luego el resultado del menor o igual (False en pantalla)
print "Is it less or equal?", 5 <= -2

