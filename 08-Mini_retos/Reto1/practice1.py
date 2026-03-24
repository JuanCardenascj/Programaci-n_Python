"""Reto Programador Junior---!!!

  Haz un programa que:
   1. Pida 5 números al usuario
   2. Guarde esos números en una lista
   3. Al final imprima el número mayor"""

numeros = []

for i in range(5):
    numero = int(input("Digite un número: "))
    numeros.append(numero)

mayor = numeros[0]
menor = numeros[0]

for n in numeros:
    if n > mayor:
        mayor = n
    elif n < menor:
        menor = n

print("El número mayor es:", mayor)
print("El número menor es:", menor)