# -*- coding: utf-8 -*-
#Todo script lo abrimos con el string de utf8 para evitar problemas con los caracteres raros, como ñ etc


#Del builtin module "sys" hacemos un import de argv, que es "argument variables" Esta variable captura los argumentos que le pasamos al script de python al correr
#En otros casos (otros lenguajes) a los modulos se los llaman librerias
#Este script debe correrse con 3 argumentos, de lo contrario fallará
from sys import argv

#Aca hacemos un "unpack" de argv de tal manera que en vez de terner en argv todo un string largo podamos trabajar con 4 variables distintas
#Estos nombres son aleatorios, podriamos usar otros si quisieramos
script, first, second, third = argv

#Imprimimos cada una de las variables
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

