"""
Crea una función:

es_mayor_de_edad(edad)

Si la edad es 18 o más:

Mayor de edad

Si no:

Menor de edad
"""

#Creando la función
def es_mayor_de_edad(edad):
    if edad >= 18:
        print("Mayor de edad")
    else:
        print("Menor de edad")
es_mayor_de_edad(20)