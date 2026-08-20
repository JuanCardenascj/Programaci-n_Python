"""Instrucción:

Crea un diccionario persona = {"nombre": "Ana", "edad": 25, "ciudad": "Bogotá"}
Usa items() para recorrer clave y valor
Muestra cada clave y su valor

Explicación:
for clave, valor in persona.items(): → Itera sobre pares clave-valor
"""

persona = {"nombre": "Ana", "edad": 25, "ciudad": "Bogotá"}

for clave, valor in persona.items():
    print(f"{clave}: {valor}")