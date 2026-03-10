#Creando un conjunto con una función set - Recordar que los datos no son modificables

conjunto = set(["dato1", "dato2"])

#Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato2", "dato1"]) #para congelar el conjunto!

print(conjunto)

#TEORIA DE CONJUNTOS

conjuntop = {1,3,5,7}
conjuntoo = {1,3,7}

#Verificando si es un subconjunto
resultado = conjuntoo.issubset(conjuntop) #Es un subconjunto
resultado = conjuntoo <= conjuntop

print(resultado)