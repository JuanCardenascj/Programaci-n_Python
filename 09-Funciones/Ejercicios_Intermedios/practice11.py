"""Crea una función que:
1. Reciba una lista de números
2. Aplique una función a cada número
3. Devuelva la lista transformada"""

# Escribe tu código aquí
def transformar_lista(numeros, funcion):
    resultado = []
    for numero in numeros:
        resultado.append(funcion(numero))
    return resultado

numeros = [1, 2, 3]
print(transformar_lista(numeros, lambda x: x + 1))  # [2, 3, 4]
print(transformar_lista(numeros, lambda x: x * 3))  # [3, 6, 9]