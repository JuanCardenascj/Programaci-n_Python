"""Metodos Listas"""

#Creando una lista con LIST!
lista = list(["Hola","soy","david",29])

#Cantidad de Elementos
cantidad_elementos = len(lista)
print(cantidad_elementos)

#Agregando un elmento a la lista
lista.append("Ethan")
print(lista)

#Agregando un elemento a la lista en un indice especifico
lista.insert(2, "Silvia")
print(lista)

#Agregando varios elementos a la lista
lista.extend(["Jorge","Zoraida"]) #Se pasa en modo lista
print(lista)

#Eliminando un elem ento de la lista por su indice
lista.pop(0) #Para eliminar el ultimo elemento (-1)
print(lista)

#Removiendo un elemento de la lista por su valor
lista.remove('soy') #Si lo encuentra lo elimina, de lo  contrario tira error
print(lista)

#Ordenando los elementos de forma ascendente
lista2 = ([231,541,21,23,58,True])
lista2.sort() #No funciona con cadenas de texto

#Eliminando todos los elemtnos de la lista
lista.clear()