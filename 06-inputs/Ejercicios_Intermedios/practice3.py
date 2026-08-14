"""Instrucción:

Pide algo al usuario
Verifica si ingresó algo
Si ingresó algo, muestra el valor
Si no ingresó nada, muestra un mensaje de error

Explicación:
if nombre: → Verifica que no esté vacío
"""
nombre = input("Nombre: ")

if nombre:
    print(f"Hola {nombre}")
else:
    print("Error: No ingresaste un nombre")