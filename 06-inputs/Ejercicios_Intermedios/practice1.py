"""Instrucción:

Pide la edad al usuario
Usa if para verificar si es mayor de edad
Muestra un mensaje apropiado

Explicación:
input() devuelve texto, lo conviertes a entero para comparar
"""

edad = int(input("Digite su edad: "))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")