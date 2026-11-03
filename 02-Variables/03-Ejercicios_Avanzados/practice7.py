"""Instrucción:

Crea una lista frutas = ["manzana", "pera", "manzana", "uva", "pera", "manzana"]
Crea una variable contador que cuente cuántas veces aparece "manzana"
Muestra el resultado

Explicación:
contador empieza en 0
Recorre la lista, cada vez que encuentra "manzana" suma 1
"""

frutas = ["manzana", "pera", "manzana", "uva", "pera", "manzana"]
contador = 0

for fruta in frutas:
    if fruta == "manzana":
        contador += 1

print(f"Manzanas: {contador}")  # 3