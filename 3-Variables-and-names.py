# -*- coding: utf-8 -*-
#Todo script lo abrimos con el string de utf8 para evitar problemas con los caracteres raros, como ñ etc



#Declara la variable cars con un valor de 100
cars = 100
#Declara la variable con un valor de 4.0 (con floating point) para que despues no de error cuando use operaciones aritmeticas. Aunque en este caso no seria necesario porque solo multiplica por cars, que no puede ser con coma
space_in_a_car = 4.0
#Declara la variable drivers con  un valor de 30
drivers = 30
#Declara la variable passangers con un valor de 90
passangers = 90
#Declara que cars not driver en igual al resultado de cars menos drivers
cars_not_driven = cars - drivers
#Declara que cars_driven es igual a drivers
cars_driven = drivers
#Declara que carpool_capacity es igual al resultad de cars_driven multiplicado por space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
#Declara que average passangers_per_car es igual al resultado de passangers dividido cars_driven
average_passangers_per_car = passangers / cars_driven

#Imprime texto, variable numerica (sea declarada o resultado), texto (En todos los casos)
print "There are", cars, "cars available"
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today"
print "We have", passangers, "to carpool today."
print "We need to put about", average_passangers_per_car, "in each car."


#Un solo igual asigna un valor, es decir dice que lo que esta a la izquierda del igual es lo mismo que lo que esta a la derecha del igual. Suele usarse para declarar variables.
# Dos iguales se usa para hacer un test de si un valor es igual a otro, como en un if

# Si bien puede declararse una variable sin espacios, es decir, x=100, esta mal visto porque lo hace menos legible


