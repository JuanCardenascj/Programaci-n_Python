"""Instrucción:

Crea una variable producto = "Laptop"
Crea una variable precio = 800
Crea una variable mensaje que combine: "El producto " + producto + " cuesta $" + precio (convertido a string)
Muestra el mensaje

Explicación:
str(precio) → Convierte el número a texto para poder unirlo
"""

producto = "Laptop"
precio = 900
mensaje = f"El producto: {producto} cuesta: ${precio}"
print(mensaje)