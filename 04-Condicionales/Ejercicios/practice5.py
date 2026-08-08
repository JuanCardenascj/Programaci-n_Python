"""Instrucción:

Crea a = 10 y b = 20
Usa if, elif y else para compararlos
Muestra cuál es mayor

Explicación:
elif → "else if" (si no se cumple lo anterior, pregunta otra cosa)
Se evalúa de arriba hacia abajo
"""

a = 10
b = 20
if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{a} Es menor que {b}")
else:
    print(f"Los números {a} y {b} son iguales")