"""Las tuplas:
    Son viables de crear cuando solo tenemos datos de solo lectura
    
    Por ejemplo: Cuando solo se van a leer datos"""

#Se puede iterar una tupla de la misma forma que se hacía con las listas
tupla =  (1,2,3,4,5,6,7)
print(tupla)
print(tupla[-1]) #El ultimo elmento
print(len(tupla)) #Número de elementos que tiene
print(tupla.index(5)) #Posición donde se encuentra el número
print(tupla[:3]) #Sublista con los primeros tres elementos
print(tupla[4]) #Elementos que hay en la posición

#Al igual que las listas, las tuplas tambien puede ser anidada
tupla2 = (1, 2, ("a", "b"), 3)
print(tupla2) #Muestra la tupla y la anidada
print(tupla2[2][0]) #En la tuplas 2 en la posición 0 ("a")

#Tambien es posible convertir una lista en tupla haciendo uso de la función tuple()
lista = [1,2,3,4,5,6,7,8]
tupla3 = tuple(lista)
print(type(tupla3)) #<Class "Tuple">
print(tupla3)

#Tambien es posible convertir de una tupla en una lista con función list()
lista2 = list(tupla3)
print(type(list))