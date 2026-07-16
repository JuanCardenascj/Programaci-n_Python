"""INPUTS"""

import json
import os

# Archivo donde se guardarán las habilidades
ARCHIVO = "habilidades.json"

# Cargar habilidades desde archivo o crear por defecto
if os.path.exists(ARCHIVO):
    with open(ARCHIVO, "r") as f:
        habilidades = json.load(f)
else:
    habilidades = {
        "Daño": 180,
        "Corta curas": 95,
        "Heridas Profundas": 50,
        "Daño Magico": 120,
        "Armadura": 150
    }

nombre_apellido = input("::::::::BIENVENIDO::::::::\nDigite su nombre y apellido: ")
print(f"Bienvenido: {nombre_apellido}")
print(f"\n{nombre_apellido}, ¿qué deseas hacer?")
print("1) Revisar habilidades")
print("2) Mejorar habilidades")
print("3) Salir")

opcion = input("Selecciona una opción: ")

if opcion == "1":
    print("\nTus habilidades actuales son:")
    
    for nombre, nivel in habilidades.items():
        print(f"{nombre}: {nivel}")

elif opcion == "2":
    print("\n......Entrando al sistema de mejoras...")
    
    print("""
1. Daño
2. Corta curas
3. Heridas Profundas
4. Daño Magico
5. Armadura
""")

    # Mapeo de números a nombres
    mapa = {
        "1": "Daño",
        "2": "Corta curas",
        "3": "Heridas Profundas",
        "4": "Daño Magico",
        "5": "Armadura"
    }

    habilidad = input("¿Qué habilidad deseas mejorar?: ")

    if habilidad in mapa:
        nombre = mapa[habilidad]
        habilidades[nombre] += 25
        print(f"\n{nombre} aumentó +25 puntos 🔥")
        print(f"Nuevo nivel: {habilidades[nombre]}")

        # Guardar los cambios en el archivo
        with open(ARCHIVO, "w") as f:
            json.dump(habilidades, f, indent=4)
        print("¡Cambios guardados correctamente!")
    else:
        print("Esa habilidad no existe")

elif opcion == "3":
    # Guardar antes de salir (por si acaso)
    with open(ARCHIVO, "w") as f:
        json.dump(habilidades, f, indent=4)
    print("¡Hasta luego, invocador!")

else:
    print("Esa opción no existe")