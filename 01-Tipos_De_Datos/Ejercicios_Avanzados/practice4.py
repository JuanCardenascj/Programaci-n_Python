"""
Crea un diccionario:

inventario = {
    "arroz": 10,
    "leche": 8,
    "azucar": 15
}

Haz que el usuario escriba un producto.

Si existe:

Hay X unidades

Si no existe:

Producto no encontrado
"""

#Creando el diccionario
inventario = {
    "arroz": 10,
    "leche": 8,
    "azucar": 15
}

#Pidiendo el producto al usuario
producto = input("Ingrese un producto: ")

if producto in inventario:
    print("Hay", inventario[producto], "unidades")
else:
    print("Producto no encontrado...!")