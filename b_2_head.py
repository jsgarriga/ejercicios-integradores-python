#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Jess Garriga

"""
    El siguiente código ejecuta un programa que recibe un archivo *.txt junto a un número N e imprime las primeras N líneas del documento.
"""

from itertools import islice #  importamos la librería externa

def leer_n_lineas(archivo, n=11):

    with open(archivo, 'r') as f:
        for l in islice(f, n):
            print(l, end='')

nombre_archivo = 'zen.txt'
n = 5

leer_n_lineas(nombre_archivo, n)
