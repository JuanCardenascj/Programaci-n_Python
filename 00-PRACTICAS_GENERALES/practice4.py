"""
🧩 Ejercicio — Promedio de números

Haz un programa que:

Pida números al usuario indefinidamente

El usuario puede escribir 0 para terminar

Al final el programa debe mostrar:

Cantidad de números ingresados (sin contar el 0)

La suma total

El promedio
"""

suma = 0
contador = 0

numero = int(input("Ingrese un numero (0 para terminar): "))

while numero != 0:
    suma = suma + numero
    contador = contador + 1

    numero = int(input("Ingrese un numero (0 para terminar): "))

if contador > 0:
    promedio = suma / contador
    print(f"Cantidad de numeros ingresados: {contador}")
    print(f"Suma total: {suma}")
    print(f"Promedio: {promedio}")
else:
    print("No se ingresaron numeros.")
