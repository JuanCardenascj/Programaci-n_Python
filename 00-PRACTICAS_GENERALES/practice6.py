"""
🚀 Mini reto para subir aún más el nivel

Modifica el programa para que además muestre:

👉 Cuántos números fueron pares
👉 Cuántos números fueron impares

Ejemplo:

Pares: 4
Impares: 3
"""

suma = 0
contador = 0

numero = int(input("Ingrese un numero (0 para terminar): "))

mayor = numero
menor = numero
pares = 0
impares = 0

while numero != 0:
    suma = suma + numero
    contador = contador + 1
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1


    numero = int(input("Ingrese un numero (0 para terminar): "))

if contador > 0:
    promedio = suma / contador
    print(f"Cantidad de numeros ingresados: {contador}")
    print(f"Suma total: {suma}")
    print(f"Promedio: {promedio}")
    print(f"El número mayor es: {mayor}")
    print(f"El número menor es: {menor}")
    print(f"Los números pares son: {pares}")
    print(f"Los npumeros impares son: {impares}")
else:
    print("No se ingresaron numeros.")