# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
""" EJERCICIOS CICLO WHILE"""

""" 1. Elabora run programa para calcular y mostrar el factorial de un entero
entrado por teclado ( 6! = 6*5*4*3*2*1)"""

numero = 0
factorial = 1
contador = 1

numero =int(input("Ingrese un numero entero: "))

while contador <= numero:
    factorial = factorial * contador
    contador = contador + 1
    
print("El factorial es: ",factorial)


"""2. Calcular una nueva nomina"""

nombre = "" 
salario = 0
incremento = 0.0

numero_empleados = 0             #personas a las que se les hizo el cálculo
nuevo_salario = 0                #Incremento salarial
aumentos = 0                     #Acumulador de personas que reciben un aumento
total_salarios_anteriores = 0    #Total nomina actual
total_aumentos = 0               #Variación total en la nomina
total_nuevos_salarios = 0        #Total de la nueva nomina

prom_salarios_anteriores = 0
prom_aumentos = 0
prom_nuevos_salarios = 0

incremento = float(input("Aumento para este año: "))
nombre = input("Nombre del empleado: ")

while nombre != "" :
    
    salario = int(input("Salario del empleado: $"))
    total_salarios_anteriores = total_salarios_anteriores + salario
    numero_empleados += 1
    
    if salario <= 1000000 :
        nuevo_salario = salario + salario * incremento
        aumentos += 1
        
        total_aumentos = total_aumentos + nuevo_salario - salario
        total_nuevos_salarios = total_nuevos_salarios + nuevo_salario
        
    else:
        nuevo_salario = salario
        total_nuevos_salarios = total_nuevos_salarios + salario
    
    print("\nEmpleado ", nombre, "\tSalario anterior: $", salario, "\tNuevo salario: $", nuevo_salario)
    nombre = input("Nombre del empleado: ")
    
prom_salarios_anteriores = total_salarios_anteriores / numero_empleados

if aumentos != 0: 
    prom_nuevos_salarios = total_nuevos_salarios / numero_empleados
    prom_aumentos = total_aumentos / aumentos       
else:
    prom_nuevos_salarios = prom_salarios_anteriores
    
print("\nINFORME")
print("\nTotal empleados: ", numero_empleados)

print("\nEmpleados con aumento: ", aumentos)
print("\nNomina anterior: $", total_salarios_anteriores, "\tNueva nomina: $", total_nuevos_salarios, "\tTotal aumentos: $", total_aumentos,)
print("\nPromedio salarial anterior: $", prom_salarios_anteriores, "\tNuevo promedio salarial: $", prom_nuevos_salarios)
print("\nPromedio de aumentos: $", prom_aumentos)



 




    




