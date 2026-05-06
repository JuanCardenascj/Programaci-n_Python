"""Utilizada para filtrar los elementos de un iterable"""

number = [1,2,3,4,5,6,7,8,9,10]
lista_pares = list(filter(lambda x : x % 2 == 0,number))
print(lista_pares)

names = ['Alice', 'Bod', 'Ana', 'David', 'Amelia', 'Charlie']
lista_nombres = list(filter(lambda x : x[0] == 'A', names ))
print(lista_nombres)