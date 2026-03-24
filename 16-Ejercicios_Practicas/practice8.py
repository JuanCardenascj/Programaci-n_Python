"""
Ejercicio 8: Adivina el número (simple)
Escribe un programa que:

Tenga un número fijo (ejemplo: 7)

Pida al usuario adivinar

Diga si acertó o no

Se repita hasta que acierte
"""

secreto = 7

while True:
    adivina = int(input("Adivina el número (1-10): "))
    
    if adivina == secreto:
        print("¡Felicidades! Acertaste")
        break
    else:
        print("No acertaste, intenta de nuevo")