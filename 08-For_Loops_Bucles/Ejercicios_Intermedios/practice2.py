"""Instrucción:

Crea una lista frutas = ["Manzana", "Pera", "Uva"]
Usa enumerate() para obtener índice y valor
Muestra el índice y el valor

Explicación:
enumerate() → Devuelve índice y valor en cada iteración
"""

frutas = ["Manzana", "Pera", "Uva"]
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")