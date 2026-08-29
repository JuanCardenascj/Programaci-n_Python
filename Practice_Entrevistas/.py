"""EJERCICIO 1: FizzBuzz (Aprende paso a paso)
¿Qué tenemos que hacer?
El problema dice:
Números del 1 al 50
Si es múltiplo de 3 → "Fizz"
Si es múltiplo de 5 → "Buzz"
Si es múltiplo de 3 y 5 → "FizzBuzz"
"""

# Un bucle for repite el código para cada número
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:  # Si es múltiplo de 3 Y de 5
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#De manera que se utilice función!
def fizzbuzz():
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
fizzbuzz()

"""Ejercicio 2: Contar Pares - Sin función vs Con función"""
numeros = [1, 2, 3, 4, 5, 6]
contador = 0

for numero in numeros:
    if numero % 2 == 0:
        contador += 1

print(contador)  # 3

#Con función
def contar_pares(numeros):
    contador = 0
    for numero in numeros:
        if numero % 2 == 0:
            contador += 1
    return contador

# Usar la función
resultado = contar_pares([1, 2, 3, 4, 5, 6])
print(resultado)  # 3

"""Ejercicio 3: Sumar lista - Sin función vs con función"""
numeros = [1, 2, 3, 4, 5]
total = 0

for numero in numeros:
    total += numero

print(total)  # 15

#Con función
def sumar_lista(numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

# Usar la función
print(sumar_lista([1, 2, 3, 4, 5]))  # 15

"""Ejercicio 4: Invertir cadena, Sin función vs con función"""
texto = "hola"
invertido = ""

for letra in texto:
    invertido = letra + invertido

print(invertido)  # "aloh"

def invertir(texto):
    invertido = ""
    for letra in texto:
        invertido = letra + invertido
    return invertido

print(invertir("hola"))  # "aloh"