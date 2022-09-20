#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Jess Garriga

"""
    El siguiente código ejecuta un programa de agendadonde guardar nombres y números de teléfono. El programa nos dará el siguiente menú:

- Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra debe permitir ingresar el teléfono correspondiente.
- Buscar: Nos pide una cadena de caracteres y nos muestra todos los contactos cuyos nombres comiencen por dicha cadena.
- Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
- Listar: Nos muestra todos los contactos de la agenda. Implementa un diccionario.
"""

from time import sleep

agenda = {}

while True:
    print("\n")
    print("Por favor, ingrese una opción:")
    sleep(2)
    print("1. Añadir/modificar")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Listar")
    print("5. Salir")
    
    opcion = int(input("¿Qué opción desea ejecutar?: \n"))
    if opcion == 1:
        nombre = input("Nombre del contacto: \n")    
        if nombre in agenda:
            print("%s ya existe. Su número de teléfono es %s" % (nombre,agenda[nombre]))
            opcion = input("Escriba 's' si quiere modificarlo. U otra letra para continuar. \n")
            if opcion == "s":
                numero = input("Ingrese el nuevo número de teléfono: \n")
                agenda[nombre]=numero
        else:
            numero = int(input("Ingrese el número de teléfono: \n"))
            print("Guardando... Aguarde")
            sleep(3)
            print("Éxito al registrar")
            sleep(2)
            print("Volviendo al inicio")
            agenda[nombre]=numero
    elif opcion == 2:
        cadena = input("Ingrese el nombre del contacto que quiere buscar: \n")    
        for nombre, numero in agenda.items():
            if nombre.startswith(cadena):
                print("El número de teléfono de %s es %s" % (nombre,agenda[nombre]))
                sleep(2)
                print("Volviendo al inicio")
    elif opcion == 3:
        nombre = input("Ingrese el nombre del contacto que quiere borrar: \n")    
        if nombre in agenda:
            opcion = input("Escriba 's' si quiere borrarlo. U otra tecla para continuar. \n")
            if opcion == "s":
                del agenda[nombre]
                print("Contacto eliminado con éxito")
                print("Volviendo al inicio")
        else:
            print("El contacto ingresado no existe")
            print("Volviendo al inicio")
    elif opcion == 4:
        for nombre, numero in agenda.items():
            print(nombre,"->",numero)
            print("Volviendo al inicio")
    elif opcion == 5:
        break
    else:
        print("Opción incorrecta")
        print("Volviendo al inicio")
