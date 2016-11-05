
#Declaramos la variable x, luego imprimimos el texto llamando a una variable con un formatter de integro decimal. luego declara que la variable llamada es "10"
#string dentro de string
x = "There are %d types of people." % 10

#Declaramos la variable "binary" con el valor "binary"

binary = binary

#Declaramos la variable do_not con el valor "don't"

do_not = "don't"

#Declaramos la variable y con el texto del chiste, seteando dos formatters de string y llamando a las variables binary y do_not, que declaramos antes
#String dentro de string
y = "Those who know %s and those who %s." % (binary, do_not)

#imprimimos las variables x e y, haciendo efectivo el chiste

print x
print y


#Imprimimos texto y llamamos a la variable x, con el inicio del chiste, con un formatter que le dice que imprima el texto sea lo que sea (convierte los objetos de python usando repr). La salida sera igual a la que tuvimos antes  "I said: 'There are 10 types of people.'.""
#String dentro de string
print "I said: %r." % x

#Ahora algo muy similar pero con el formatter de string, llamamos a la variable "y"
#La salida será I also said: 'Those who know binary and those who don't.'.

#String dentro de string
print "I also said: '%s'." % y

#Declaramos la variable "hilarious" y le damos valor "False"

hilarious = False

#Declaramos la variable joke_evaluation, string de texto y una variable (no declarada aun) que se presentara con un formatter que imprimer de una ( %r  )

joke_evaluation = "isn't that joke so funny?! %r"

#Impromimos joke evaluation y le decimos que %r es la variable hilarious

print joke_evaluation % hilarious

#Declaramos las variables w y e, que mostraremos luego juntas con un print

w = "This is the left side of..."
e = "a string with a rigth side."

#Y finalmente lo imprimimos, la variable w saldra a la izquierda y e a la derecha, todo en un solo renglon.

print w + e