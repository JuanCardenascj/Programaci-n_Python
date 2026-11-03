"""
Crea un diccionario llamado producto con:

nombre
precio
disponible

Luego muestra el tipo de dato de cada valor.
"""

#Creando un diccionario llamado producto 
producto = {"Nombre" : "Diccionario",
            "Producto" : "Diccionario Lenguas",
            "Disponible" : True}

print(producto)

#Mostrando el tipo de dato de cada valor
print(type(producto["Nombre"]))
print(type(producto["Producto"]))
print(type(producto["Disponible"]))