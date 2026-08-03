""" Bitácora de Viaje
Cree un programa que:
   1.Pida al usuario que ingrese el destino de un viaje y la fecha
   2.Guarde esa información en un archivo viajes.txt
   3.Cada nuevo viaje se agrega al final (sin borrar los anteriores)
   4.Permita ver todos los viajes guardados

Requisitos:
Usa una función agregar_viaje() que reciba destino y fecha
Usa una función ver_viajes() que lea y muestre todos los viajes
Usa el modo "a" (append) para agregar sin borrar
"""

def agregar_viaje(destino, fecha):
    with open("viajes.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"Destino: {destino} - Fecha: {fecha}\n")
    print("✅ Viaje agregado")

def ver_viajes():
    try:
        with open("viajes.txt", "r", encoding="utf-8") as archivo:
            print("\n📋 VIAJES GUARDADOS:")
            print("-" * 30)
            for linea in archivo:
                print(linea.strip())
            print("-" * 30)
    except FileNotFoundError:
        print("📝 No hay viajes guardados")

# Programa principal
while True:
    print("\n1. Agregar viaje")
    print("2. Ver viajes")
    print("3. Salir")
    opcion = input("Elige: ")

    if opcion == "1":
        destino = input("Destino: ")
        fecha = input("Fecha: ")
        agregar_viaje(destino, fecha)
    elif opcion == "2":
        ver_viajes()
    elif opcion == "3":
        print("👋 Hasta luego")
        break
    else:
        print("❌ Opción no válida")