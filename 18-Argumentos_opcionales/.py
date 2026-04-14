"""Crea una función que calcule el precio final de un producto, si existe un descuento"""
def precio_product(nombre_producto, cantidad, precio_u, descuento=0):
    precio_final = (cantidad * precio_u) * (1 - descuento)
    print(f"El precio final para {nombre_producto} es {precio_final}")

precio_product("Short", 10, 100, 0.95)