"""Instrucción:

Pide al usuario su edad con input()
Convierte la edad a entero
Si es mayor o igual a 18, muestra "Eres mayor de edad"
Si no, muestra "Eres menor de edad"

Explicación:
int(input()) → Convierte el texto a número
if edad >= 18: → Verifica si es mayor o igual a 18
"""

edad = int(input("Digite su edad: "))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")