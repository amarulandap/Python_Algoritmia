# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

""" EJERCICIOS CON LA INSTRUCCIÓN IF ELSE"""

""" 1. Determinar si un número entero entrado por pantalla es
divisible por otro número entrado también por pantalla.

a = 0
b = 0

print("ES A DIVISIBLE POR B")
a = int(input("Ingrese el primer número entero: "))
b = int(input("Ingrese el segundo número entero: "))

if a % b == 0:
    print("\nSi es divisible")
else:
    print("\nNo es divisible")"""
    
    
""" 2. Leer tres números enteros y determinar si la suma de dos de
ellos da el tercero.

c = 0
d = 0
e = 0

print("\nES A LA SUMA DE B + C")
c = int(input("Ingrese el primer número entero: "))
d = int(input("Ingrese el segundo número entero: "))
e = int(input("Ingrese el tercer número entero: "))

if c == d + e:
    print(f"\nla suma de {d} + {e} es igual {c} ") 
elif d == c + e:
    print(f"\nla suma de {c} + {e} es igual {d} ")
elif e == c + d:
    print(f"\nla suma de {c} + {d} es igual {e} ")
else:
    print("\nNo son suma")"""
    
"""3. Leer tres números enteros y determinar si con ellos se puede
construir un triángulo o no

f = 0
g = 0
h = 0

print("\nSE PUEDE CONSTRUIR UN TRIANGULO?")
f = int(input("Ingrese el primer número entero: "))
g = int(input("Ingrese el segundo número entero: "))
h = int(input("Ingrese el tercer número entero: "))

if f != 0 and g != 0 and h != 0:
    
    if f + g > h or f + h > g or g + h > f :
        print("\nSi se puede construir un triagulo")
    else:
        print("\nNo se puede construir un triagulo")
else:
    print("\nNo se puede construir un triangulo")"""
    

"""4. Elaborar un algoritmo que lea el salario actual de 
un empleado y que calcule e imprima el nuevo salario con base en 
la siguiente condición: si el salario es menor que 1000000 pesos, 
aumente el 10%; de lo contrario, no haga aumento.

salario = 0
incremento = 0.0
nuevo_salario = 0

print("\nCALCULO DEL NUEVO SALARIO")
salario = int(input("Ingrese salario del empleado: "))

if salario < 1000000 :
    incremento = 0.1
    nuevo_salario = salario + incremento * salario
    print("\nSu salario es: $", nuevo_salario)
else: 
    print("\nSu salario es: $", salario)"""


""" 5. Elaborar un algoritmo que lea dos datos numéricos enteros y
 que los imprima ordenados ascendentemente.


int1 = 0
int2 = 0

print("\nORGANIZAR LOS NÚMEROS DE MANERA ASCENDENTE")
int1 = int(input("Ingrese el primer número entero: "))
int2 = int(input("Ingrese el segundo número entero: "))

if int1 < int2 :
    print(int1, int2)
else:
    print(int2, int1)"""

""" 6. Construya un programa de computador que lea tres números enteros
y los escriba ordenados ascendentemente."""

num1 = 0
num2 = 0
num3 = 0

print("\nORGANIZAR LOS NÚMEROS DE MANERA ASCENDENTE")

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num3 = int(input("Ingrese el tercer número entero: "))

if num1 <= num2 :
    if num1 <= num3 :
        if num2 <= num3 :
            print(num1, num2, num3)
        else:
            print(num1, num3, num2)
    else:
        if num2 <= num1 :
            print(num3, num2, num1)
        else:
            print(num3, num1, num2) 
else:
    if num2 <= num3 :
        if num1 <= num3 :
            print(num2, num1, num3)
        else:
            print(num2, num3, num1)
    else: 
        print(num3, num2, num1)
        

        
    
       

















