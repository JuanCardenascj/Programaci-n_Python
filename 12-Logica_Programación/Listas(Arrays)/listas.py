"""Una lista es una coleccion de elmentos almacenados en orden.
   Permite guardar muchos datos en una sola variable! 
   Muchos tipos de datos en una sola colección.
   
   Características:
   
   1. Tienen un orden
   2. Permiten acceder por posición
   3. Pueden modificarse
   4. Pueden tener diferentes tipos de datos"""

#LISTA - ARRAY
numeros = [132, 524, 585, 98, 100, 652]

"""Acciones o Operaciones básicas que se deben dominar"""

#Para recorrer una Lista - Array
for numero in numeros:
    print(numero)

#Para acceder por índice en la Lista - Array
print(numeros[0])

#Para agregar un elemento en la Lista - Array
numeros.append(897)

#Para insetar datos en medio
numero.insert(1, 99)

#Para eliminar un elemento en la Lista - Array
numeros.remove(100)
