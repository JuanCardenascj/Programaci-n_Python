"""
Instrucción:
Crea numero = 15
Usa % para verificar si es múltiplo de 5
Muestra el resultado

Explicación:
numero % 5 == 0 → Si el resto es 0, es múltiplo de 5
"""

numero = int(input("Ingrese un número: "))  # Solicita al usuario que ingrese un número

if numero % 5 == 0:
    print("Es múltiplo de 5")
else:
    print("No es múltiplo de 5")