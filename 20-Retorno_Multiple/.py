def sumar(nombre_producto, cantidad, precio_u, descuento=0):
    precio_final = (cantidad * precio_u) * (1-descuento)
    return nombre_producto, cantidad, precio_final #De está manera de retorna mas de un valor

compra_final = sumar('medias', 3, 10)
print(f"La compra final es: {compra_final}")