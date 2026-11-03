"""Son similares a las tuplas, estructuras de datos que permite almacenar una secuencia de objetos de manera secuencial!

1. Las listas son mutables...!"""

frutas = ["manzana", "banano", "pera", "uva"]

#Creando una lista con LIST!
lista = ["Hola","soy","david",29]
familia = ["Zoraida", "Jorge Alberto", "Silvia", "Leidy", "Juan"]

#Cantidad de Elementos
cantidad_elementos = len(lista)
print(cantidad_elementos)
print(len(familia))

#Agregando un elemento a la lista, al final de ella
lista.append("Ethan")
print(lista)
familia.append("JhonG")
print(familia)

#Agregando un elemento a la lista en un indice especifico o posición específica
lista.insert(2, "Silvia")
print(lista)
familia.insert(1, "Angie")
print(familia)

#Contar elementos de la lista - Cuenta cuantas veces aparece un elemento en la lista de manera específica---!
print(lista.count(29))
print(familia.count("Silvia"))
print(familia.count("Juan"))
print(familia.count("Jorge Alberto"))

#Agregando varios elementos a la lista
lista.extend(["Jorge","Zoraida"]) #Se pasa en modo lista
print(lista)
familia.extend(["Ana", "Julio"])
print(familia)

#Eliminando un elemento de la lista por su indice
lista.pop(0) #Para eliminar el ultimo elemento (-1)
print(lista)
familia.pop(-1)
familia.pop(-2)
print(familia)

#Removiendo un elemento de la lista por su valor
lista.remove('soy') #Si lo encuentra lo elimina, de lo  contrario tira error
print(lista)
familia.remove('Ana')
print(familia)

#Reversando
lista.reverse()
print(lista)

#Ordenando los elementos de forma ascendente
lista2 = ([231,541,21,23,58,True])
lista2.sort() #No funciona con cadenas de texto

#Eliminando todos los elementos de la lista
lista.clear()

#Busca elementos --> IN
if "uva" in frutas:
    print("existe")

#Recorrer listas
for fruta in frutas:
    print(fruta)
