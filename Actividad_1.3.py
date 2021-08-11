# -*- coding: utf-8 -*-
"""
Created on Sat May 22 08:27:45 2021

@author: Andres Marulanda
"""

""" Actividad 1.3."""

#Definicion de variables
capital_total = 0
ganancia = 0
total_ventas = 0
inversion = 0

nombre_producto_1 = ""
unidades_producto_1 = 0
unidades_compradas_1 = 0
valor_compra_producto_1 = 0
valor_total_compra_producto_1 = 0
precio_de_venta_1 = 0
unidades_vendidas_1 = 0
valor_total_ventas_producto_1 = 0
unidades_sobrantes_1 = 0

nombre_producto_2 = ""
unidades_producto_2 = 0
unidades_compradas_2 = 0
valor_compra_producto_2 = 0
valor_total_compra_producto_2 = 0
precio_de_venta_2 = 0
unidades_vendidas_2 = 0
valor_total_ventas_producto_2 = 0
unidades_sobrantes_2 = 0

nombre_producto_3 = ""
unidades_producto_3 = 0
unidades_compradas_3 = 0
valor_compra_producto_3 = 0
valor_total_compra_producto_3 = 0
precio_de_venta_3 = 0
unidades_vendidas_3 = 0
valor_total_ventas_producto_3 = 0
unidades_sobrantes_3 = 0

capital_total = int(input("Ingrese el capital total: "))

#producto_1
nombre_producto_1 = input("Ingrese el nombre del producto: ")
unidades_producto_1 = int(input("Ingrese el numero de cantidades iniciales: "))
unidades_compradas_1 = int(input("Ingrese el numero de unidades compradas: "))
valor_total_compra_producto_1 = int(input("Ingrese el valor pagado por la compra del producto: "))
valor_compra_producto_1 = valor_total_compra_producto_1 / unidades_compradas_1
print("\nValor de compra unitario: " + str(valor_compra_producto_1))

precio_de_venta_1 = int(input("Ingrese el precio de venta: "))
unidades_vendidas_1 = int(input("Ingrese el numero de unidades vendidas: "))
valor_total_ventas_producto_1 = precio_de_venta_1 * unidades_vendidas_1
unidades_sobrantes_1 = unidades_producto_1 + unidades_compradas_1 - unidades_vendidas_1
print("\nValor de compra del producto: " + str(valor_total_compra_producto_1))
print("Existencias del producto: " + str(unidades_sobrantes_1))

if valor_total_ventas_producto_1 > valor_total_compra_producto_1 :
    print("El producto generó ganancias")
else:
    print("El producto generó perdidas")
    
#producto_2
nombre_producto_2 = input("Ingrese el nombre del producto: ")
unidades_producto_2 = int(input("Ingrese el numero de cantidades iniciales: "))
unidades_compradas_2 = int(input("Ingrese el numero de unidades compradas: "))
valor_total_compra_producto_2 = int(input("Ingrese el valor pagado por la compra del producto: "))
valor_compra_producto_2 = valor_total_compra_producto_2 / unidades_compradas_2
print("\nValor de compra unitario: " + str(valor_compra_producto_2))

precio_de_venta_2 = int(input("Ingrese el precio de venta: "))
unidades_vendidas_2 = int(input("Ingrese el numero de unidades vendidas: "))
valor_total_ventas_producto_2 = precio_de_venta_2 * unidades_vendidas_2
unidades_sobrantes_2 = unidades_producto_2 + unidades_compradas_2 - unidades_vendidas_2
print("\nValor de compra del producto: " + str(valor_total_compra_producto_2))
print("Existencias del producto: " + str(unidades_sobrantes_2))

if valor_total_ventas_producto_2 > valor_total_compra_producto_2 :
    print("El producto generó ganancias")
else:
    print("El producto generó perdidas")
    
#producto_3
nombre_producto_3 = input("Ingrese el nombre del producto: ")
unidades_producto_3 = int(input("Ingrese el numero de cantidades iniciales: "))
unidades_compradas_3 = int(input("Ingrese el numero de unidades compradas: "))
valor_total_compra_producto_3 = int(input("Ingrese el valor pagado por la compra del producto: "))
valor_compra_producto_3 = valor_total_compra_producto_3 / unidades_compradas_3
print("\nValor de compra unitario: " + str(valor_compra_producto_3))

precio_de_venta_3 = int(input("Ingrese el precio de venta: "))
unidades_vendidas_3 = int(input("Ingrese el numero de unidades vendidas: "))
valor_total_ventas_producto_3 = precio_de_venta_3 * unidades_vendidas_3
unidades_sobrantes_3 = unidades_producto_3 + unidades_compradas_3 - unidades_vendidas_3
print("\nValor de compra del producto: " + str(valor_total_compra_producto_3))
print("Existencias del producto: " + str(unidades_sobrantes_3))

if valor_total_ventas_producto_3 > valor_total_compra_producto_3 :
    print("El producto generó ganancias")
else:
    print("El producto generó perdidas\n")
    
#balance_general
inversion = valor_total_compra_producto_1 + valor_total_compra_producto_2 + valor_total_compra_producto_3
total_ventas = valor_total_ventas_producto_1 + valor_total_ventas_producto_2 + valor_total_ventas_producto_3
capital_total = capital_total + total_ventas - inversion
ganancia = total_ventas - inversion

print("\nInversión total: " + str(inversion))
print("Total ventas: " + str(total_ventas))
print("Capital final: " + str(capital_total))

if ganancia > 0:
    print("Ganancias totales: " + str(ganancia))
else:
    ganancia = ganancia * (-1)
    print("Perdidas totales: " + str(ganancia))
    

    




