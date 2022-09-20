#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Jess Garriga

"""
    El siguiente código ejecuta un programa que pedirá el número de estudiantes que vamos a introducir, solicitará su nombre y calificaciones hasta que introduzcamos un número negativo. Nos mostrará la lista de estudiantes y la nota media obtenida por cada une de elles. Nota: si se introduce el nombre de une estudiante que ya existe el programa nos dará un error.
"""

#  iniciamos diccionario
estudiantes = {}

#  pedimos a user la cantidad
cantidad = int(input("Introduzca la cantidad de estudiantes a cargar: \n"))

#  iteramos la cantidad de estudiantes
for num in range(cantidad):
    estudiante = input("Nombre de estudiante: \n")
    while estudiante in estudiantes:
        print("Estudiante ya existe.")
        estudiante = input("Nombre de estudiante: \n")
    notas = []
    nota = int(input("Ingrese una calificación del estudiante (si el valor es negativo interrumpe la carga): \n"))
    while nota > 0:
        notas.append(nota)
        nota = int(input("Ingrese una calificación del estudiante (si el valor es negativo interrumpe la carga): \n"))
    estudiantes[estudiante] = notas.copy()

for estudiante, notas in estudiantes.items():
    print("%s ha obtenido un promedio de %.2f" % (estudiante,sum(notas)/len(notas)))
