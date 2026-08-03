"""Instrucción:

Usa input() para pedir el nombre del usuario
Usa input() para pedir su edad (como texto)
Convierte la edad a entero
Muestra un mensaje de bienvenida
"""

nombre = input("Como te llamas: ")
edad = int(input("Cuántos años tienes: "))
print(f"Hola {nombre}, el año que viene tendras {edad + 1} años")