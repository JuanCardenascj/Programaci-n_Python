"""
Crea una función:

contar_elementos(lista)

que retorne cuántos elementos tiene una lista.

Ejemplo:

frutas = ["manzana", "pera", "uva"]

contar_elementos(frutas)

Resultado:

3
"""

#Creando la función...!
def contar_elementos(listas):
    cantidad = len(listas)
    return cantidad

frutas = ["manzana", "pera", "uva"]

resultado = contar_elementos(frutas)

print(resultado)