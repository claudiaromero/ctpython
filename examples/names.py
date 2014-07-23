#!/usr/bin/env python 
# -*- coding: utf-8 -*-


#PROPONGA MEJORAS PARA QUE EL CODIGO SEA MAS LEJIBLES POR HUMANOS

#ejercicio 1
#Queremos tener una variable para almacenar nos colores de una bandera
a=[]

#a la que le vamos a poner los colores azul y amarillo
c1="azul"
c2="amarillo"

a.append(c1)
a.append(c2)

print "la bandera tiene estos colores"+str(a)

#extra, construya otra bandera y agregue otros colores





#ejercicio 2

#armamos una lista con 10 numeros 
a=range(10)

#la desordenamos
import random
random.shuffle(a)


#los elevamos al cuadrado los elementos y los guardamos en una lista de cuadrados
b=[e**2 for e in a]

#convertimos la lista b en una lista de numpy
import numpy
b=numpy.array(b)

#pedimos el minimo
c=b.min()







#ejercicio 3 
#tenemos a maria y a jose de las cuales almacenamos su edad y sexo
p1Edad= 22
p1Sexo="d"# en catalan mujer es dona

p2Edad=33
p2Sexo= "v"

#ahora queremos calcular el promedio de edad de nuestra población
p=(p1Edad+p2Edad)/2










