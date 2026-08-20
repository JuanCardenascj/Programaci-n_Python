"""Instrucción:

Crea dos listas: nombres = ["Ana", "Luis", "Carlos"] y edades = [25, 30, 28]
Usa zip() para recorrerlas juntas
Muestra nombre y edad

Explicación:
zip(nombres, edades) → Combina las listas en pares
"""

nombres = ["Ana", "Luis", "Carlos"]
edades = [25, 30, 28]

for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")