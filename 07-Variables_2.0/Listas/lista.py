"""Son variables que almacenan arrays. internamente cada posición puede ser un tipo de dato distinto.!"""

#Ejemplos:
lista1 = [] #Es una lista vacia
numeros = [1,2,3,4,5,6,7,8,9]
vocales = []
materias = ["Matemáticas", "Sociales", "Calculo", "Arítmetica"]
fecha = [27, "noviembre", 2022]
lst = [1,2,3,13.4, "Python", [1,2,3]]

#Métodos asociados a la Lista!
numeros = [1,2,3,4,5,6,7,8,9]
numeros.append(5) #Añade este item al final de la lista

numeros = [1,2,3,4,5,6,7,8,9]
numeros.clear() #Elimina todos los items de una lista y deja una lista vacía

numeros = [1,2,3,4,5,6,7,8,9]
n = numeros.count(2) #Cuenta el número de veces que aparece el item en la lista

numeros = [1,2,3,4,5,6,7,8,9]
numeros.insert(0) #Agregar un ítem a la lista en un indice específico

numeros = [1,2,3,4,5,6,7,8,9]
numeros.pop() #Borrar el ultimo elemento de la lista

numeros = [1,2,3,4,5,6,7,8,9]
numeros.remove(2) #Borra el ítem especificado

numeros = [1,2,3,4,5,6,7,8,9]
print(numeros.reverse()) #Inicia la lista en el último ítem