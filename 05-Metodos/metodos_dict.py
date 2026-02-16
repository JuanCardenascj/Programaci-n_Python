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

#Accediendo al diccionario
getttr = diccionario.get("Subs")
print(getttr)