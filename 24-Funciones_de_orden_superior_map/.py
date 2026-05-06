"""Es cualquier función que acepta otra función como argumento!
  Pueden retornar un función o una lista..."""

#MAP!
lista_frutas = ['banano', 'pera', 'manzana']
sufix = '_fruta' #Sufijo

#Función lambda --> Anonima
lista_frutas_sufix =  list(map(lambda x : x+sufix, lista_frutas))
print(lista_frutas_sufix)