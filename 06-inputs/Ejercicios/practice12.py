"""Instrucción:

Pide la temperatura en Celsius
Convierte a Fahrenheit
Muestra el resultado

Explicación:
Fahrenheit = (Celsius * 9/5) + 32
"""

celsius = float(input("Temperatura en Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C son {fahrenheit:.1f}°F")