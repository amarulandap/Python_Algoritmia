# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 11:07:02 2021

@author: Andres Marulanda
"""

""" TALLER MISIÓN TIC - ASIGNACION Y CONDICIONALES"""

import math

"""Calcular el salario bruto de un empleado teniendo en cuenta el salario base, 
el auxilio de transporte ($106.454) que se otorga si el salario es inferior a 2 salarios mínimos 
($908.526) y un descuento por seguridad social del 9%."""

salario_minimo = 0
salario_bruto = 0
salario_neto = 0
descuento_seguridad_social = 0.0
auxilio_transporte = 0
cedula = 0
nombre = ""

salario_minimo = int(input("Valor del salario mínimo: $"))

descuento_seguridad_social = float(input("Porcentaje de descuento por seguridad social: "))
descuento_seguridad_social /= 100

auxilio_transporte = int(input("Subsidio de transporte: $"))

controlador = 1
while controlador != 0:
    
   cedula = int(input("Ingrese el documento del empleado sin puntos o comas: ")) 
   nombre = input("Nombre del empleado: ")
   salario_bruto = int(input("Salario del empleado: $"))

   if salario_bruto < 2 * salario_minimo:
       salario_neto = salario_bruto - salario_bruto * descuento_seguridad_social + auxilio_transporte
   else:
       salario_neto = salario_bruto - salario_bruto * descuento_seguridad_social
        
   print("\n",cedula, nombre,":")
   print("Total a pagar: $", salario_neto)
   
   controlador = int(input("Ingrese 0 para terminar, 1 para continuar: "))
   


"""Calcular el área y el volumen de una esfera = 4/3 * PI * r3"""

radio = 0.0
area = 0.0
volumen = 0.0

radio = float(input("Ingrese el radio de la esfera en cms: "))

area = 4 * math.pi * radio**2
volumen = (4 * math.pi * radio**3)/3

print("\nArea de la esfera: ",area, "cms2")
print("\nVolumen de la esfera: ",volumen, "cms3")



"""Calcular el costo de las nueces. Si al fabricar barras de chocolate, 
cada una lleva tres cuartas partes onzas de nueces. El costo por onza de las nueces es de $500."""

numero_onzas = 0.0
costo_onza = 0
barras_chocolate = 0

costo_nueces = 0

costo_onza = int(input("Costo de la onza de nueces: $"))
barras_chocolate = int(input("¿Cuántas barras desea fabricar? "))

numero_onzas = (3 * barras_chocolate) / 4

costo_nueces = numero_onzas * costo_onza

print(f"\nNueces necesarias: {numero_onzas} Onzas, con un costo de: ${costo_nueces}")
   


"""Calcular el pago mensual de un préstamo hipotecario dado por la fórmula 
𝑃=𝑀𝑖1−(1+𝑖)−𝑛 Donde M= cantidad del préstamo, i = interés mensual, n = número de meses

P [(i (1 + i)**n) / ((1 + i)**n – 1)]"""

M = 0
i = 0.0
n = 0

pago_mensual = 0.0

M = int(input("Monto del prestamo: $"))

i = float(input("Tasa efectiva anual: "))
i /= 12
i /= 100

n = int(input("Número de meses: "))

cociente = i*((i + 1)**n) / ((1 + i)**n - 1)
pago_mensual = M * cociente
                           
print("\nValor cuota mensual: $",pago_mensual)



""" Elabore un programa que muestre los números impares anteriores a un número dado 
y que finalmente nos indique cuántos números mostró."""

numero = 0
contador_impares = 0

numero = int(input("ingrese un número entero: "))

for i in range(1, numero + 1):
    if i % 2 != 0:
        contador_impares += 1

print(f"El total de números impares antes de {numero} es {contador_impares}")
a = list(range(1, numero + 1, 2))
print("lista de números impares: ",a)



""" Elabore un programa que calcule el producto de dos números utilizando únicamente sumas y 
utilizando el ciclo mientras."""

multiplicando = 0
multiplicador = 0

resultado = 0

multiplicando =int(input("Ingrese un número entero: "))
multiplicador =int(input("Ingrese otro número entero: ")) 

if multiplicando == 0 or multiplicador == 0:
    print("\nEl resultado de la multiplicación es: ",resultado)
else:    
    contador = 0
    while contador < multiplicador:
        resultado += multiplicando
        contador += 1
    
    print("\nEl resultado de la multiplicación es: ",resultado)
    
    
   
"""Elabore un programa que calcule la suma de n números digitados desde el teclado, 
discriminando la suma de los números positivos y la de los números negativos, 
el algoritmo debe detenerse cuando se digite el 0."""

num = 0
contador_num = 0

suma_positivos = 0
suma_negativos = 0

num = int(input("Ingrese un número entero, mayor o menor que 0: "))

while num != 0:
    contador_num += 1
    if num < 0:
        suma_negativos += num
    else:
        suma_positivos += num
        
    num = int(input("Ingrese un nuevo número: "))

print(f"\nEl total de números ingresados fue: {contador_num}")  
print("Los números positivos suman: ",suma_positivos)
print("Los números negativos suman: ",suma_negativos)   
    
   
