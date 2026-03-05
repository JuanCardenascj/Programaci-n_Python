"""Son datos que tienen adentro otros datos y por eso son datos compuestos"""

#Listas - Se puede realizar diversas acciones.
lista = ["Jorge", " Soy David", True, 1.70]
print(lista) #Para imprimir toda la lista
print(len(lista)) #Para imprimir la longitud de la lista


#Para acceder a un dato en especifico
print(lista[1])

#Tuplas - No se pueden modificar los datos.
tupla = ("Jorge", "Soy David", True, 1.70)
print(tupla) #Imprime toda la tupla
print(tupla[1]) #Para acceder a un dato en especifico

#Set - Conjunto - No se puede acceder por el indice al elemento en el conjunto - No permite repetir valores
conjunto = {"Jorge", "Soy David", True, 1.70}
#print(conjunto[1]) Esto está mal

#Dict o Diccionario - Es Parecido al Json ) Key and Value )
diccionario = {
    'nombre' : "Luis",
    'canal' : "JuanCardenas",
    'edad' : 29
}
print(diccionario['nombre'])

