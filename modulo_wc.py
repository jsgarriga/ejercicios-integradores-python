#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Jess Garriga

"""
    Módulo para contar líneas, palabras, espacios y caracteres del archivo que entregue user. 
"""

# Función para contar líneas, palabras, espacios y caracteres
def counter(fname):
    # variable para almacenar el recuento total de palabras
    num_words = 0
    # variable para almacenar el número total de líneas
    num_lines = 0
    # variable para almacenar el número total de caracteres
    num_charc = 0
    # variable para almacenar el recuento de espacio total
    num_spaces = 0

    # abrir el archivo usando el método with()
    # para que el archivo se cierre
    # después de completar el trabajo
    with open(fname, "r", encoding="utf8") as f: # en "utf8" por los caracteres latinos
        # bucle para iterar el archivo
        # línea por línea
        for line in f:
            # incrementando el valor de
            # num_lines con cada
            # iteración del bucle para
            # almacenar el recuento total de líneas
            num_lines += 1

            # declarando una palabra variable
            # y asignando su valor como Y
            # porque todo archivo se
            # debe comenzar con
            # una palabra o un carácter
            word = "Y"

            # bucle para iterar cada
            # línea por letra
            for letter in line:
                # condición para comprobar
                # que el carácter encontrado
                # no sea un espacio en blanco y una palabra
                if (letter != " " and word == "Y"):

                    # incrementando la palabra
                    # cuenta por 1
                    num_words += 1

                    # asignando el valor N a
                    # palabra variable porque hasta
                    # espacio no se encuentra
                    # una palabra no puede ser completada
                    word = "N"

                # condición para comprobar
                # que el carácter encontrado
                # es un espacio en blanco
                elif (letter == " "):
                    # incrementando el espacio
                    # cuenta por 1
                    num_spaces += 1

                    # asignando el valor Y a
                    # palabra variable porque después de
                    # espacio en blanco una palabra
                    # debe aparecer una palabra
                    word = "Y"

                # bucle para iterar cada
                # carácter de letra por
                # carácter
                for i in letter:
					# condición para comprobar
					# que el carácter encontrado
					# no sea un espacio en blanco y no
					# un carácter de nueva línea
                    if(i != " " and i != "\n"):
                        # carácter incremental
                        # cuenta por 1
                        num_charc += 1

    print("Cantidad de palabras en el archivo: ",
          num_words)

    print("Cantidad de líneas en el archivo: ",
          num_lines)

    print("Cantidad de caracteres en el archivo: ",
          num_charc)

    print("Cantidad de espacios en el archivo: ",
          num_spaces)
