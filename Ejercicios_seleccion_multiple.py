# -*- coding: utf-8 -*-
"""
Created on Thu May 27 11:12:53 2021

@author: Andres Marulanda
"""

""" EJERCICIOS DE SELECCIÓN MULTIPLE"""

"""3. EMPRESA DE AVIACION PAJARO LOCO"""

origen = ""
destino = ""
nombre = ""
apellido = ""
edad = 0

sobrecosto_MB = 10000
sobrecosto_CB = 20000
sobrecosto_CBR = 10000
sobrescosto_BRB = 30000
descuento_MC = 0.1

costo_tiquete = 0

nombre =input("Ingrese el nombre del pasajero: ")
apellido =input("Ingrese el apellido del pasajero: ")
edad =int(input("Ingrese la edad del pasajero: "))

print("\nSELECCIONE LA RUTA: ")
print("1. Medellin")
print("2. Bogotá")
print("3. Cali")
print("4. Barranquilla")
print("5. Miami")

origen =input("Seleccione la ciudad origen: ")
destino =input("Seleccione la ciudad destino: ")

if origen == "5" or destino == "5":
    costo_tiquete = 980000
    
elif origen == "1":
    if destino == "2":
        if edad > 60:
            costo_tiquete = 200000
        else:
            #sobrecosto_MB = 10000
            costo_tiquete = 200000 + sobrecosto_MB
    elif destino == "3":
        #descuento_MC = 0.1
        costo_tiquete = 250000 - (edad * descuento_MC * 1000)  
    elif destino == "4":
        costo_tiquete = 300000 + (edad * 1000)    
        
elif origen == "2":
    if destino == "1":
        if edad > 80:
            costo_tiquete = 0
        else:
            costo_tiquete = 200000
    elif destino == "3":
        if edad >= 60:
            costo_tiquete = 200000
        else:
            costo_tiquete = 200000 + (1000 * (60 - edad))
    elif destino == "4":
        if edad >= 60:
            costo_tiquete = 400000
        else:
            costo_tiquete = 400000 + (0.5 * edad * 10000)
   
elif origen == "3":
    if destino == "1":
        costo_tiquete = 350000
    elif destino == "2":
        if edad < 60:
            #sobrecosto_CB = 20000
            costo_tiquete = 280000 + sobrecosto_CB
        else:
            costo_tiquete = 280000
    elif destino == "4":
        if edad < 60:
            #sobrecosto_CBR = 10000
            costo_tiquete = 190000 + sobrecosto_CBR
        else:
            costo_tiquete = 190000
    
else:
    if destino == "1":
        if edad < 10:
            costo_tiquete = 250000
        else: 
            costo_tiquete = 500000
    elif destino == "2":
        if edad >= 30:
            costo_tiquete = 210000
        else:
            costo_tiquete = 210000 + sobrescosto_BRB
    elif destino == "3":
        if edad < 60:
            costo_tiquete = 350000
        else:
            costo_tiquete = 350000 + (10000 * (edad - 60))
            
print("\nEl pasajero: ",nombre, apellido, "pagará un tiquete con costo de: $",costo_tiquete)


