"""
🚀 Si seguimos avanzando el entrenamiento

El siguiente reto natural sería:

🧩 Nivel +1

Hacer el mismo programa pero además mostrar:

👉 Número mayor ingresado
👉 Número menor ingresado
"""
suma = 0
contador = 0

numero = int(input("Ingrese un numero (0 para terminar): "))

mayor = numero
menor = numero

while numero != 0:
    suma = suma + numero
    contador = contador + 1
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero

    numero = int(input("Ingrese un numero (0 para terminar): "))

if contador > 0:
    promedio = suma / contador
    print(f"Cantidad de numeros ingresados: {contador}")
    print(f"Suma total: {suma}")
    print(f"Promedio: {promedio}")
    print(f"El número mayor es: {mayor}")
    print(f"El número menor es: {menor}")
else:
    print("No se ingresaron numeros.")