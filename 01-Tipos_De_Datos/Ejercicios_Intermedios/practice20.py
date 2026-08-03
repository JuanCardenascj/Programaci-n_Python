"""Instrucción:

Crea un diccionario ventas = {"Lunes": 100, "Martes": 150, "Miércoles": 120}
Usa un bucle for para mostrar cada día y su venta
"""

ventas = {"Lunes" : 100, "Martes" : 150, "Miércoles" : 120}
for dia, venta in ventas.items():
    print(f"{dia} : {venta}")
