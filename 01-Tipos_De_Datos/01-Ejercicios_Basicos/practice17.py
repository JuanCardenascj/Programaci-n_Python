"""Instrucción:

Crea una variable precio con valor 99.99
Crea una variable descuento con valor 0.15 (15%)
Calcula el precio con descuento
Muestra el resultado con 2 decimales
"""
precio = 99.99
descuento = 0.15
precio_final = precio * (1- descuento)
print(f"Precio con descuento: ${precio_final:.2f}")