#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Jess Garriga

"""
    El siguiente código ejecuta un programa que recibe una expresión y un archivo e imprime las líneas del archivo que contienen la expresión recibida.
"""

archivo = "zen.txt" # también podría pasarse un input, quedando `input("¿Cómo se llama el archivo?\n")` que recibiría el archivo por le user

try:

	leer_archivo = open(archivo, "r")

	text = input("Ingrese la expresión a buscar:\n")

	lines = leer_archivo.readlines()

	lista = []
	indice = 0

	for line in lines:
		if text in line:
			lista.insert(indice, line)
			indice += 1

	leer_archivo.close()

	if len(lista)==0:
		print("\n\"" +text+ "\" no se encontró en \"" +archivo+ "\"!")
	else:
		lineLen = len(lista)
		print("\n**** Líneas que contiene \"" +text+ "\" ****\n")
		for i in range(lineLen):
			print(end=lista[i])
		print()

except :
    print("El archivo no existe")
