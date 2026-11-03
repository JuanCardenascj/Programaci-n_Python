"""
Crea una lista con diferentes tipos de datos:

datos = [10, "Juan", True, 3.5, False, "Python", 20]

Cuenta cuántos:

enteros
cadenas
booleanos
decimales

hay en la lista.
"""

#Creando una lista con diferentes tipos de datos
datos = [10, "Juan", True, 3.5, False, "Python", 20]

enteros = 0
cadenas = 0
booleanos = 0
decimales = 0

for dato in datos:

    if type(dato) == bool:
        booleanos += 1
        
    elif type(dato) == int:
        enteros+= 1

    elif  type(dato) == float:
        decimales += 1

    elif type(dato) == str:
        cadenas += 1

print("Enteros:", enteros)
print("Cadenas:", cadenas)
print("Booleanos:", booleanos)
print("Decimales:", decimales)        