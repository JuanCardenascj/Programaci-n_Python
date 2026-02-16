"""Lo que se hizo anteriormente TAMBIEN FUNCIONA PARA LOS CONJUNTOS!"""

animales = {"Gato", "Perro", "Loro", "Cocodrilo"}
numeros = {10, 62 , 12, 72}

#Recorriendo la conjunto animales
for animal in animales:
    print(f"Ahora la variable animal es igual a: {animal}")

#Recorriendo la conjunto numeros y multiplicando cada valor *10
for numero in numeros:
    resultado = numero * 10
    print(resultado)


#Iterando sobre dos conjuntos con Zip() y deben ser del mismo tamaño. Se iteran al mismo tiempo!
for numero, animal  in zip(animales,numeros):
    print(f"Recorriendo conjunto 1: {numero}")
    print(f"Recorriendo conjunto 2: {animal}")

#Para operar o iterar en el rango
for num in range(100, 500):
    print(num) #Imprime los numeros desde el 100 hasta el 499

#Para operar o iterar en un solo rango
for num1 in range(100):
    print(num1) #Imprime los numeros del 0 al 99

#Forma correcta de recorrer una conjunto con su indice
for num2 in enumerate(numeros):
    print(num2)

#Usando el ELSE en for
for numero in numeros:
    print(f"Ejecuctando el ultimo bucle, valor actual: {numero}")
else: 
    print("El bucle termino")