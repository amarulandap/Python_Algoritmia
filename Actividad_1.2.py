# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
""" Actividad 1.2"""

#Definicion de variables

problema_1 = ""
problema_2 = ""
problema_3 = ""

#Cultivo 1
nombre_cultivo_1 = ""
cantidad_cultivo_1 = 0
tiempo_cultivado_en_meses_1 = 0
problema_cultivo_1 = ""


#Cultivo 2
nombre_cultivo_2 = ""
cantidad_cultivo_2 = 0
tiempo_cultivado_en_meses_2 = 0
problema_cultivo_2 = ""

#Cultivo 3
nombre_cultivo_3 = ""
cantidad_cultivo_3 = 0
tiempo_cultivado_en_meses_3 = 0
problema_cultivo_3 = ""

#Recepcion de datos

#Cultivo 1
nombre_cultivo_1 = input("Ingrese el nombre del cultivo: ")
cantidad_cultivo_1 = int(input("Ingrese el numero de arboles sembrados: "))
tiempo_cultivado_en_meses_1 = int(input("Ingrese el tiempo del cultivo en meses: "))
problema_cultivo_1 = input("Tiene algun problema con el cultivo? S/N ")

if problema_cultivo_1 == 'S':
    problema_1 = input("Cual es el problema? ")

#cultivo 2
nombre_cultivo_2 = input("Ingrese el nombre del cultivo: ")
cantidad_cultivo_2 = int(input("Ingrese el numero de arboles sembrados: "))
tiempo_cultivado_en_meses_2 = int(input("Ingrese el tiempo del cultivo en meses: "))
problema_cultivo_2 = input("Tiene algun problema con el cultivo? S/N ")

if problema_cultivo_2 == 'S':
    problema_2 = input("Cual es el problema? ")

#cultivo 3
nombre_cultivo_3 = input("Ingrese el nombre del cultivo: ")
cantidad_cultivo_3 = int(input("Ingrese el numero de arboles sembrados: "))
tiempo_cultivado_en_meses_3 = int(input("Ingrese el tiempo del cultivo en meses: "))
problema_cultivo_3 = input("Tiene algun problema con el cultivo? S/N ")

if problema_cultivo_3 == 'S':
    problema_3 = input("Cual es el problema? ")
    
#Imprimir los datos

print("Sus cultivos son:")
print("El cultivo de: " + nombre_cultivo_1 + " tiene " + str(cantidad_cultivo_1) + " matas sembradas en " + str(tiempo_cultivado_en_meses_1) + " meses")
print("El cultivo tiene problemas de: " + problema_1)
if problema_cultivo_1 == 'N':
    print("El cultivo no tiene problemas")

print("El cultivo de: " + nombre_cultivo_2 + " tiene " + str(cantidad_cultivo_2) + " matas sembradas en " + str(tiempo_cultivado_en_meses_2) + " meses")
print("El cultivo tiene problemas de: " + problema_2)
if problema_cultivo_2 == 'N':
    print("El cultivo no tiene problemas")

print("El cultivo de: " + nombre_cultivo_3 + " tiene " + str(cantidad_cultivo_3) + " matas sembradas en " + str(tiempo_cultivado_en_meses_3) + " meses")
print("El cultivo tiene problemas de: " + problema_3)
if problema_cultivo_3 == 'N':
    print("El cultivo no tiene problemas")








 
