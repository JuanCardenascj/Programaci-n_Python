"""Instrucción:

Pide una calificación (0-100)
Usa if, elif, else para asignar una letra:
90-100: A
80-89: B
70-79: C
60-69: D
<60: F
Muestra la letra

Explicación:
Las condiciones se evalúan en orden
"""

calificacion = int(input("Calificación (0-100): "))

if calificacion >= 90:
    print("A")
elif calificacion >= 80:
    print("B")
elif calificacion >= 70:
    print("C")
elif calificacion >= 60:
    print("D")
else:
    print("F")