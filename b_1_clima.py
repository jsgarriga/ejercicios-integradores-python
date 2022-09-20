#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Jess Garriga

"""
    El siguiente código ejecuta un programa que muestra la temperatura actual en grados celcius con la librería "python-weather" para una ciudad ingresada por user.
"""

import modulo_clima.py

ciudad = None
try:
    ciudad = input(str("Ingrese el nombre de la ciudad:\n"))
except Exception as e:
    print("Hubo un error:", e)
finally:
    print("La ciudad solicitada es:", ciudad)

print("La temperatura para", ciudad, "es de", clima.obtener_estado_tiempo(ciudad), "°C")
