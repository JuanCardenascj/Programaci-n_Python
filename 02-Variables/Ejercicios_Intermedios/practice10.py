"""Instrucción:

Crea a = 5 y b = 10
Intercambia los valores (a debe quedar con 10 y b con 5)
Muestra el resultado

Explicación:
a, b = b, a → Intercambia los valores
"""

a = 5
b = 10
print(f"Antes: a={a}, b={b}")  # Antes: a=5, b=10

a, b = b, a
print(f"Después: a={a}, b={b}")  # Después: a=10, b=5