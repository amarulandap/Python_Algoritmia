# -*- coding: utf-8 -*-
"""
Created on Sun May 30 12:40:40 2021

@author: Andres Marulanda
"""

"""EJERCICIOS SEMANA 2"""

"""1. Elabore un programa en Python que lea un dato, 
    el cual es el valor de un ángulo en grados, 
    y que lo convierta e imprima en radianes.
    Use pi = 3.14

angulo = 0.0
pi = 3.14
radianes = 0.0

angulo = float(input("Valor del ángulo en grados: "))
radianes = angulo * pi / 180
print("valor del ángulo en radianes: ", radianes)"""


"""2. Elabore un programa en Python que lea un entero de dos dígitos
     y produzca como salida los dígitos del número leído con su correspondiente mensaje.    
     Por ejemplo, si el número leído es 27, la salida deberá ser:(sin texto adicional):
    2
    7

numero = ""

numero = input("Ingrese un entero de dos digitos: ")
for i in numero:
    print(i)"""
    

"""3. Elabore un programa en Python que lea un área en hectáreas y 
    la convierta en centímetros cuadrados y muestre el resultado 
    con un mensaje bien explicativo.
    
area = 0.0
metros_cuadrados = 0.0
centimetros_cuadrados = 0.0

area = float(input("Ingrese el número de hectareas: "))

metros_cuadrados = area * 10000
centimetros_cuadrados = metros_cuadrados * 10000

print(area, "Hectareas equivalen a ",metros_cuadrados, "metros cuadrados")
print(metros_cuadrados, "metros cuadrados aquivalen a", centimetros_cuadrados, "centímetros cuadrados")"""


"""4. Elabore un programa en Python que imprima la suma de 
    los números enteros de 300 hasta 5000"""

suma = 0    

for i in range(300, 5001, 1):
    suma += i 
    
print(suma)
    

    

    

    






