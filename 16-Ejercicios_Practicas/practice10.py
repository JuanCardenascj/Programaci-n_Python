"""
Ejercicio 10: Promedio de 3 notas
Escribe un programa que:

Pida 3 notas

Calcule el promedio

Diga si está aprobado (promedio >= 60)
"""

nota1 = float(input("Escriba una nota: "))
nota2 = float(input("Escriba una nota: "))
nota3 = float(input("Escriba una nota: "))

promedio = (nota1 + nota2 + nota3) / 3

print(f"El promedio es: {promedio}")

if promedio >= 60:
    print("Aprobado")
else:
    print("Reprobado")