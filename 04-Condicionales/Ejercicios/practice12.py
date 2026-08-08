"""Instrucción:

Crea una variable nombre = "Ana"
Usa if nombre: para verificar si tiene valor
Si tiene valor, muestra el nombre
Si no, muestra "No hay nombre"

Explicación:
if variable: → Verifica si tiene un valor (no vacío, no None, no 0)
"""

nombre = "Ana"

if nombre:
    print(f"Nombre: {nombre}")
else:
    print("No hay nombre")