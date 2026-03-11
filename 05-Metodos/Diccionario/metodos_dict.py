"""Metodos para Dicionario"""

#Creando diccionario
diccionario = {
    "Nombre" : 'Juan David',
    "Apellido" : 'Cardenas Jimenez',
    "Subs" : 100
}

#Iterando con keys
clave = diccionario.keys()
print(clave)

#Accediendo al diccionario - El get no da error si la clave no existe
getttr = diccionario.get("Subs")
print(getttr)

#Acceder a un valor
print(diccionario["Nombre"])