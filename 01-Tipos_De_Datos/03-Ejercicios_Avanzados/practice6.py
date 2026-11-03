"""
Dada:

numeros = [1,2,2,3,4,4,5,5,6]

Usa un set para eliminar repetidos.

Luego vuelve a convertir el resultado a lista.
"""

#Creando la lista numeros
numeros = [1,2,2,3,4,4,5,5,6]

#Usando el set para eliminar repetidos
numero2 = {1,2,2,3,4,4,5,5,6}
print(numero2)

#Convirtiendo el resultado
numero2 = list(numero2)
print(numero2)

#OTRA FORMA DE HACERLO MAS PROFESIONAL
numeros_unicos = set(numeros)
print(numeros_unicos)

#PARA VOLVER A LISTA
numeros_unicos = list(numeros_unicos)
print(numeros_unicos)