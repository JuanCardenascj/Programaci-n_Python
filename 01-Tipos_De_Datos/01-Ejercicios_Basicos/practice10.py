"""
Dada la lista:

colores = ["rojo", "azul", "verde"]

Cambia "azul" por "amarillo".
"""

#Cambiando el azul por el amarillo

colores = ["rojo", "azul", "verde"]
print(colores)

colores.remove("azul")
colores.insert(1, "amarillo")
print(colores)