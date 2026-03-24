"""
Ejercicio 4: Contador de vocales
Escribe un programa que:

Pida una palabra

Cuente cuántas vocales tiene
"""

palabra = input("Escrba una palabra: ")

contador = 0

for letra in palabra:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        contador += 1

print(f"La palabra tiene {contador} vocales")