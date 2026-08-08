"""Instrucción:

Crea una variable numero = 4
Usa % (módulo) para verificar si es par
Si es par, muestra "Es par"
Si no, muestra "Es impar"

Explicación:
numero % 2 == 0 → Si el resto de dividir por 2 es 0, es par
4 % 2 = 0 → Verdadero
"""

numero =  4
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")