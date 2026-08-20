"""Instrucción:

Crea una lista colores = ["Rojo", "Verde", "Azul", "Amarillo"]
Usa un bucle for para contar cuántos elementos tiene
Muestra el conteo

Explicación:
contador = 0 → Inicializa el contador
contador += 1 → Incrementa por cada elemento
"""

colores = ["Rojo", "Verde", "Azul", "Amarillo"]
contador = 0

for color in colores:
    contador += 1

print(f"La lista tiene {contador} elementos")