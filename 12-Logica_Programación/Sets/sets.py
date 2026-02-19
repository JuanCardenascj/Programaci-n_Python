"""Son basicamente un diccionario sin valores
Ejemplo:
        numeros = {1, 2, 3}

Internamente también usa hashing. Esto sirve para:
        1. Eliminar duplicados
        2. Búsquedas rápidas
        3. Intersecciones
        4. Comparaciones eficientes
"""

#Ejemplo poderoso - Quieres saber si dos listas comparten elementos. Pero aqui abria un mal enfoque
lista1 = [2,3,5,2,5,3]
lista2 = [56,43,23,1,2]

for a in lista1:
    for b in lista2:
        if a == b:
            print("Coinciden") #Aqui es O(n2)

#Aca estaria con un mejor enfoque
set1 = set(lista1)
set2 = set(lista2)

if set1 & set2:
    print("Coinciden") #Mucho mas eficiente