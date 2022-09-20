#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Jess Garriga

"""
    El siguiente código ejecuta un programa donde se declara un diccionario para guardar el precio de distintos productos, en este caso frutas. El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final a partir de los datos guardados en el diccionario. Si la fruta no existe nos mostrará el error "El producto no existe".
"""

precios = {"banana": 200, 
			"naranja": 180, 
			"manzana": 160
			}

while True:
    fruta = input("¿Qué fruta(s) vendiste? \n")
    if fruta.lower() not in precios:
        print("El producto no existe. Por favor, intente otra vez.")
    else:
        cantidad = int(input("Introduzca la cantidad de frutas vendidas: \n"))
        print("El precio es de %.2f" % (cantidad * precios[fruta])) #  El formato "%f" viene heredado de C
    opcion = input("¿Querés cargar otra fruta? (s/n) \n")
    while opcion.lower() != "s" and opcion.lower() != "n":
        opcion = input("¿Querés cargar otra fruta? (s/n) \n")
    if opcion.lower() == "n":
        break
