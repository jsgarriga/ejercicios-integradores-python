#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Jess Garriga

"""
    Módulo para mostrar la temperatura actual en grados celcius con la librería "python-weather" para una ciudad ingresada por user.
"""

import python_weather
import asyncio
import os

async def getweather(ciudad):
    client = python_weather.Client() #  eliminé formato "IMPERIAL" ya que por defecto usa el sistema métrico (consulta: documentación)
    weather = await client.get(ciudad) #  corregí el método ".find" por ".get" (probablemente el código usaba una versión anterior de la librería)
    await client.close()
    return weather.current.temperature

def obtener_estado_tiempo(ciudad):
    loop = asyncio.get_event_loop()
    temperatura = loop.run_until_complete(getweather(ciudad))
    return temperatura
