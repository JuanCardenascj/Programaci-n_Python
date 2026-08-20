"""Instrucción:

Usa range() para generar números del 1 al 10
Usa un bucle for para mostrar cada número
Muestra el cuadrado de cada número

Explicación:
range(1, 11) → Genera [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero ** 2 → Calcula el cuadrado
"""

for numero in range(1, 11):
    print(f"{numero} al cuadrado es {numero ** 2}")