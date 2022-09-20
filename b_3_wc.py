#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Jess Garriga

"""
    El siguiente código ejecuta un programa que recibe un archivo, lo procesa e imprime su cantidad de líneas, palabras, espacios y caracteres. 
"""

import modulo_wc as wc # importamos el módulo donde definimos cómo contar cada criterio solicitado

fname = "zen.txt"

print("Los cálculos para su archivo ya están listos:\n")

contador = wc.counter(fname) # aplicamos el método "counter" para el archivo
