"""Instrucción:

Pide la edad
Usa condiciones para clasificar:
0-12: Niño
13-17: Adolescente
18-64: Adulto
65+: Adulto mayor
Muestra la clasificación

Explicación:
Condiciones múltiples
"""

edad = int(input("Edad: "))

if edad <= 12:
    print("Niño")
elif edad <= 17:
    print("Adolescente")
elif edad <= 64:
    print("Adulto")
else:
    print("Adulto mayor")