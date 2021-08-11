# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""1. promedio de dos numeros"""

numero_1 = float(input("Ingrese el primer numero: "))
numero_2 = float(input("Ingrese el segundo numero: "))

#calcular el promedio de dos numeros
promedio_numeros = (numero_1 + numero_2)/2

#imprimir el promedio
print("El promedio es = ",promedio_numeros)

"""2. Calcular el IMC"""

peso = float(input("Ingrese su peso en Kilogramos: "))
Estatura = float(input("Ingrese su estatura en metros: "))

#Cacular el IMC
indice_de_masa = peso / Estatura ** 2

#imprimir el IMC
print("su indice de masa muscular es= ",indice_de_masa)

"""3. Convertir pulgadas a centimetros"""

distancia = float(input("Ingrese la distancia en pulgadas: "))

#convertir a centimetros
distancia_1 = distancia * 2.54

#imprimir la distancia en centimetros
print("La distancia en centimetros es = ",distancia_1,"centimetros")

"""4. Convertir pies a centimetros"""

distancia_2 = float(input("Ingrese la distancia en pies: "))

#convertir a pulgadas
distancia_en_pulgadas = distancia_2 * 12
print("La distancia en pulgadas es= ",distancia_en_pulgadas,"pulgadas")

#convertir a centimetros
distancia_1 = distancia_en_pulgadas * 2.54
print("la distancia en centimetros es= ",distancia_1,"centimetros")

"""5. Distancia en pies y pulgadas convertida en centimetros"""

distancia_2 = float(input("Ingrese la distancia en pies: "))
distancia_en_pulgadas = distancia_2 * 12
distancia_1 = distancia_en_pulgadas * 2.54
print("la distancia de:",distancia_2,"pies equivale a:",distancia_1,"centimetros")

"""6. Convertir grados celsius a grados farenheit"""

temp_celsius = float(input("Ingrese la temperatura en grados centigrados: "))
temp_farenheit = 1.8 * temp_celsius + 32

print("La temperatura en grados farenheit es: " + str(temp_farenheit) + " grados farenheit")

"""7. Convertir grados farenheit a grados celsius""" 

temp_farenheit = float(input("Ingrese la temperatura en grados farenheit: "))
temp_celsius = (temp_farenheit - 32)/1.8

print("La temperatura en grados celsius es: " + str(temp_celsius) + " grados centigrados")

"""8. Convertir segundos a minutos"""

segundos = int(input("Ingrese el numero de segundos: "))
minutos = segundos // 60
aux_1 = minutos * 60
segundos_1 = segundos - aux_1

print(str(segundos) + " segundos equivale a " + str(minutos) + " minutos y " + str(segundos_1) + " segundos")


