"""
Recorre:

[5,10,15,20,25]

e imprime cada número.
"""

#Recorriendo la lista
lista1 = [5, 10, 15, 20, 25]

for lista in lista1:
    print(lista)

#Contando cuántos número hay
print(len(lista1))

#Verificando si el numero existe
if 15 in lista1:
    print("Si existe")