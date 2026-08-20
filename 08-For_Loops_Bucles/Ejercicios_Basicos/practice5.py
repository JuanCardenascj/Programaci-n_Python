"""Instrucción:

Crea una lista frutas = ["Manzana", "Pera", "Uva", "Naranja"]
Usa range(len()) para recorrer la lista con índice
Muestra el índice y la fruta

Explicación:
len(frutas) → Tamaño de la lista (4)
range(4) → [0, 1, 2, 3]
frutas[i] → Accede al elemento en la posición i
"""

frutas = ["Manzana", "Pera", "Uva", "Naranja"]

for fruta in range(len(frutas)):
    print(f"{fruta}: {frutas[fruta]}")