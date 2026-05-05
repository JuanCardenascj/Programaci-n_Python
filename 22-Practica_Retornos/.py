def calcular_precio_total(*args, **kwargs): #Utilizamos ambas
    precio_total = sum(args)
    descuento = kwargs.get('descuento', 0)
    impuesto = kwargs.get('impuesto', 0)

    precio_total -= (precio_total * descuento)
    precio_total += (precio_total * impuesto)

    return precio_total

precio_final = calcular_precio_total(432, 122, 987, 230, descuento = 0.2, impuesto = 0.01)
print(precio_final)