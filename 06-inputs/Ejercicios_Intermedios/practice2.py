"""Instrucción:

Pide un número al usuario
Verifica si es positivo, negativo o cero
Muestra el mensaje correspondiente

Explicación:
if, elif, else para diferentes casos
"""

numero = int(input("Digite un numero: "))
if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es 0")