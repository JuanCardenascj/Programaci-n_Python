"""INPUTS"""

#Pedirle un dato al Usuario
nombre_apellido = input("::::::::BIENVENIDO:::::::: \nDigite su nombre y su apellido: ")
print(f"Bienvenido: {nombre_apellido}")

print(f"\n{nombre_apellido}, ¿qué deseas hacer?")
print("1) Revisar mi daño actual")
print("2) Mejorar habilidades")
print("3) Salir")

opcion = input("Selecciona una opción: ")

if opcion == "1":
    print(f"{nombre_apellido}, tu daño es alto 🔥")
elif opcion == "2":
    print("Entrando al sistema de mejoras...")
elif opcion == "3":
    print("¡Hasta luego, invocador!")
else:
    print("Esa opción no existe")

