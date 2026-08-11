"""Instrucción:

Pide un número de tarjeta
Usa condiciones para verificar:
Longitud de 16 dígitos
Todos son números
No tiene espacios
Muestra si es válida

Explicación:
len(tarjeta) == 16 → Longitud
tarjeta.isdigit() → Verifica que todos sean dígitos
"""

tarjeta = input("Número de tarjeta: ")

if len(tarjeta) == 16 and tarjeta.isdigit():
    print("Tarjeta válida")
else:
    print("Tarjeta no válida")