"""Instrucción:

Pide el precio de un producto
Pide la cantidad
Calcula el total
Muestra el total con formato

Explicación:
float() → Para números con decimales
int() → Para números enteros
"""

precio_producto = float(input("Digite el precio del producto: "))
cantidad_producto = int(input("Digite la cantidad del producto a comprar: "))
total = precio_producto * cantidad_producto
print(f"El precio del producto es: {precio_producto}, la cantidad que usted desea comprar es de: {cantidad_producto}, y el total a pagar es: {total:.2f}")