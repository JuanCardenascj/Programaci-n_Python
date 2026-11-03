"""Calculadora de compras

Una persona compra:
- 3 camisetas a $45.000 cada una.
- 2 pantalones a $80.000 cada uno.
- 1 par de zapatos a $120.000.
Calcula:
- El costo de cada categoría.
- El subtotal.
- Un descuento del 15%.
- El precio final después del descuento.
Utiliza variables para almacenar los valores."""

# Precios unitarios
precio_camiseta = 45000
precio_pantalon = 80000
precio_zapatos = 120000

# Cantidades
cantidad_camisetas = 3
cantidad_pantalones = 2
cantidad_zapatos = 1

# Costo de cada categoría
costo_camisetas = precio_camiseta * cantidad_camisetas
costo_pantalones = precio_pantalon * cantidad_pantalones
costo_zapatos = precio_zapatos * cantidad_zapatos

# Subtotal
subtotal = costo_camisetas + costo_pantalones + costo_zapatos

# Descuento
descuento = subtotal * 0.15

# Precio final
precio_final = subtotal - descuento

# Resultados
print("Costo de camisetas: $", costo_camisetas)
print("Costo de pantalones: $", costo_pantalones)
print("Costo de zapatos: $", costo_zapatos)
print("Subtotal: $", subtotal)
print("Descuento (15%): $", descuento)
print("Precio final después del descuento: $", precio_final)