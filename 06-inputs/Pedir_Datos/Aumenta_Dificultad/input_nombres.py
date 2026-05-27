"""INPUTS"""

# Pedir datos al usuario
nombre_apellido = input("::::::::BIENVENIDO::::::::\nDigite su nombre y apellido: ")
print(f"Bienvenido: {nombre_apellido}")

# Habilidades iniciales
habilidades = {
    "Daño": 10,
    "Corta curas": 5,
    "Heridas Profundas": 3,
    "Daño Magico": 8,
    "Armadura": 15
}

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
    print("\nEntrando al sistema de mejoras...")
    
    print("""
1. Daño
2. Corta curas
3. Heridas Profundas
4. Daño Magico
5. Armadura
""")

    habilidad = input("¿Qué habilidad deseas mejorar?: ")

    if habilidad in habilidades:
        habilidades[habilidad] += 5
        print(f"\n{habilidad} aumentó +5 puntos 🔥")
        print(f"Nuevo nivel: {habilidades[habilidad]}")

    else:
        print("Esa habilidad no existe")

elif opcion == "3":
    print("¡Hasta luego, invocador!")

else:
    print("Esa opción no existe")