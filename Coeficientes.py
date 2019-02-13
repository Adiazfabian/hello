#Importamos todo el modulo sympy
from sympy import *
#ademas importamos las variables simbolicas 'n' y 't'
from sympy.abc import t, n
#import matplotlib.pyplot as plt
#import numpy as np


ao = integrate(2 / pi, (t, 0, pi / 2))
#integramos la funcion (2/pi) cuya variable es 't'
#y limites de integracion entre 0 y pi/2

print ("a0 = ")
pprint(ao)
#Usamos la funcion pprint para mostrar ao


an = integrate((2 / pi) * cos(2 * n * t), (t, 0, pi / 2))
#integramos la funcion (2/pi)*cos(2nt)
#Su variable es 't' y sus limites de integracion son 0 y pi/2

print ("an = ")
pprint(an)
#Usamos la funcion pprint para mostrar an

bn = together(integrate((2 / pi) * sin(2 * n * t), (t, 0, pi / 2)))
#integramos la funcion (2/pi*cos(2nt)
#Su variable es 't' y sus limites de integracion
#son 0 y pi/2. Ademas usamos la funcion "together"
#para simplificar la expresion

print ("bn = ")
pprint(bn)
#Usamos la funcion pprint para mostrar bn

print ("f(x) = ")

Armonica_1 = ((an*cos(2*n*t)).subs(n,1))+ \
((bn*sin(2*n*t)).subs(n,1))

#pprint(Armonica_1)
#plotting.plot(Armonica_1, ylim=(-0.5, 1.5), xlim=(-0.5,5))

armonicos = 10
Armonica_suma14 = (0)
for i in range(1, armonicos + 1):
    Armonica_suma14 = Armonica_suma14 + (an*cos(2*n*t)).subs(n, i)
for j in range(1, armonicos + 1):
    Armonica_suma14 = Armonica_suma14 + (bn*sin(2*n*t)).subs(n, j)

#pprint(Armonica_suma14)
plotting.plot(Armonica_suma14, Armonica_1, line_color= "green", ylim=(-0.5, 1.5), xlim=(-0.5,5))


#plot((Armonica_1), (Armonica_suma14))







