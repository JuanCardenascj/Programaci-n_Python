""" Instrucción:

Pide un año
Usa condiciones para verificar si es bisiesto:
Divisible por 4
Pero no por 100 (excepto si es divisible por 400)
Muestra el resultado

Explicación:
(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
"""

año = int(input("Año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("Es bisiesto")
else:
    print("No es bisiesto")