"""
Crear una función:

def buscar_nombre(lista, nombre):

que indique si un nombre existe.

Ejemplo

Lista:

estudiantes = ["Juan", "Ana", "Carlos"]

Llamada:

buscar_nombre(estudiantes, "Ana")

Resultado:

Sí existe
"""

#Creando la función
def buscar_nombre(lista, nombre):

    if nombre in lista:
        print("Sí existe")

    else:
        print("No existe")


# Crear la lista
estudiantes = ["Juan", "Ana", "Carlos"]

# Llamar la función
buscar_nombre(estudiantes, "Ana")