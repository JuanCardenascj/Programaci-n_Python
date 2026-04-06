#Crea Iterables
lista_nombres = ["Edward", "David", "Jimena"]

for nombre in lista_nombres:
    print(nombre)

#Mostrar los indices de cada uno de los elementos
for indice in range(3):
    print(indice, lista_nombres[indice]) #Así le da un indice a cada nombre

#Utilizamos la función y es mejor método y elegante..!
for indice, valor in enumerate(lista_nombres):
    print(indice, valor)