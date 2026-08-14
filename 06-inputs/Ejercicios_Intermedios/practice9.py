"""Instrucción:

Pide un número al usuario
Verifica que sea un número válido (usa try/except)
Si es válido, muestra su doble
Si no es válido, muestra un error

Explicación:
try/except atrapa errores de conversión
"""

try:
    numero = float(input("Número: "))
    print(f"El doble es: {numero * 2}")
except ValueError:
    print("Error: No ingresaste un número válido")