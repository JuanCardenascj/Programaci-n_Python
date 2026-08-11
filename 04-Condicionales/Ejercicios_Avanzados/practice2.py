"""Instrucción:

Pide el precio de un producto
Aplica descuento según el monto:
1000: 20% descuento
500: 10% descuento
100: 5% descuento
<= 100: sin descuento
Muestra el precio final

Explicación:
Diferentes descuentos según el precio
"""

precio = float(input("Digite el precio del producto: "))

if precio > 1000:
    descuento = 0.20
elif precio > 500:
    descuento = 0.10
elif precio > 100:
    descuento = 0.05
else:
    descuento = 0

precio_final = precio * (1 - descuento)
print(f"Precio final: ${precio_final:.2f}")