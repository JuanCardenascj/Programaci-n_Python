""" Instrucción:

Crea un menú con opciones: 1-ver, 2-agregar, 3-salir
Usa if, elif, else para manejar cada opción
Muestra mensajes diferentes para cada opción

Explicación:
Múltiples condicionales para el menú
"""

opcion = input("1. Ver\n2. Agregar\n3. Salir\nElige: ")

if opcion == "1":
    print("Mostrando datos...")
elif opcion == "2":
    print("Agregando datos...")
elif opcion == "3":
    print("Saliendo...")
else:
    print("Opción no válida")