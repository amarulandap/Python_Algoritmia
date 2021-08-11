# -*- coding: utf-8 -*-
"""
Created on Sat May 29 07:55:51 2021

@author: Andres Marulanda
"""

""" EJERCICIOS INSTRUCCIÓN FOR"""

"""1. Indicar si un numero es primo, teorema de wilson"""

factorial = 1
multiplo = 0
primo = 0

n = int(input("Ingrese un número entero: "))

for i in range(1, n, 1) :
    factorial = factorial * i

multiplo = factorial + 1
primo = multiplo % n

if primo == 0:
    print(n, "es primo")
else:
    print(n, "no es primo")
    
    
"""2. Ciclos para generar listados de números en escalera"""

n = 0

n = int(input("Ingrese un número entero: "))

for i in range(1, n+1, 1):
    for j in range(1, i+1, 1):
        print(i, end="")
    print("")
print("")

for i in range(1, n+1, 1):
    for j in range(1, i+1, 1):
        print(j, end="")
    print("")
print("")

for i in range(n, 0, -1):
    for j in range(1, i+1, 1):
        print(i, end="")
    print("")
print("")

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print("")
print("")"""
    



    