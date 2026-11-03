"""Calculadora de edad

Solicita al usuario su edad actual y calcula:
- Cuántos años tendrá dentro de 10 años.
- Cuántos años tenía hace 5 años.
- Cuántos meses ha vivido aproximadamente.
- Cuántos días ha vivido aproximadamente (utiliza 365 días por año)."""

edad_actual = int(input("Ingrese su edad actual: "))
edad_dentro_10_años = edad_actual + 10
edad_hace_5_años = edad_actual - 5
meses_vividos = edad_actual * 12
dias_vividos = edad_actual * 365

print(f"Edad dentro de 10 años: {edad_dentro_10_años}")
print(f"Edad hace 5 años: {edad_hace_5_años}")
print(f"Meses vividos: {meses_vividos}")
print(f"Días vividos: {dias_vividos}")