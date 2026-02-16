"""PYTHON LOS BUCLES SON FOR IN
Lo que hace es crear una variable que en cada vuelta va mostrando cada elemento dentro de la lista, en orden, hasta terminar todos los elementos dentro de la lista y el bucle termina de ejecutarse.!"""

""" TOD LO QUE SE ACABA DE HACER FUNCIONA EXACTAMENTE PARA LAS TUPLAS"""

animales = ["Gato", "Perro", "Loro", "Cocodrilo"]
numeros = [10, 62 , 12, 72]

#Recorriendo la lista animales
for animal in animales:
    print(f"Ahora la variable animal es igual a: {animal}")

#Recorriendo la lista numeros y multiplicando cada valor *10
for numero in numeros:
    resultado = numero * 10
    print(resultado)


#Iterando sobre dos listas con Zip() y deben ser del mismo tamaño. Se iteran al mismo tiempo!
for numero, animal  in zip(animales,numeros):
    print(f"Recorriendo lista 1: {numero}")
    print(f"Recorriendo lista 2: {animal}")

#Para operar o iterar en el rango
for num in range(100, 500):
    print(num) #Imprime los numeros desde el 100 hasta el 499

#Para operar o iterar en un solo rango
for num1 in range(100):
    print(num1) #Imprime los numeros del 0 al 99

#Forma correcta de recorrer una lista con su indice
for num2 in enumerate(numeros):
    print(num2)

#Usando el ELSE en for
for numero in numeros:
    print(f"Ejecuctando el ultimo bucle, valor actual: {numero}")
else: 
    print("El bucle termino")