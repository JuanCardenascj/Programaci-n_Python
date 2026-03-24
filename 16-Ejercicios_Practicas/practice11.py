"""
Ejercicio: Piedra, papel o tijera
Escribe un programa que:

Permita jugar contra la computadora

El usuario elige: piedra, papel o tijera

La computadora elige aleatoriamente

Muestra quién gana

Se repite hasta que el usuario quiera salir

Pista: Usa import random
"""

import random

opciones = ["piedra", "papel", "tijera"]

print("=== JUEGO DE PIEDRA, PAPEL O TIJERA ===\n")

while True:
    # Computadora elige al azar
    computadora = random.choice(opciones)
    
    # Usuario elige
    usuario = input("Elige piedra, papel o tijera (o 'salir' para terminar): ").lower()
    
    # Opción para salir
    if usuario == "salir":
        print("¡Gracias por jugar! Hasta luego.")
        break
    
    # Validar que la opción sea válida
    if usuario not in opciones:
        print("Opción no válida. Elige piedra, papel o tijera.\n")
        continue
    
    # Mostrar elecciones
    print(f"\nComputadora: {computadora}")
    print(f"Tú: {usuario}")
    
    # Determinar ganador
    if usuario == computadora:
        print("¡Empate!\n")
    
    elif usuario == "piedra" and computadora == "tijera":
        print("¡Ganaste! Piedra aplasta tijera\n")
    
    elif usuario == "papel" and computadora == "piedra":
        print("¡Ganaste! Papel envuelve piedra\n")
    
    elif usuario == "tijera" and computadora == "papel":
        print("¡Ganaste! Tijera corta papel\n")
    
    else:
        print("Perdiste :(\n")