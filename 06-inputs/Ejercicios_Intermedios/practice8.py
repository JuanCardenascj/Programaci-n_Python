"""Instrucción:

Muestra un menú con 3 opciones
Pide al usuario que elija una opción
Muestra un mensaje según la opción elegida

Explicación:
input() puede tomar números como texto
"""
print("1. Ver datos")
print("2. Agregar datos")
print("3. Salir")

opcion = input("Elige una opción: ")

if opcion == "1":
    print("Mostrando datos...")
elif opcion == "2":
    print("Agregando datos...")
elif opcion == "3":
    print("Saliendo...")
else:
    print("Opción no válida")