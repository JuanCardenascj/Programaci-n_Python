"""
Ejercicio 1: Variables y tipos de datos
Crea un programa que:

Declare variables para almacenar tu nombre, edad, altura (en metros) y si estás estudiando (True/False)

Muestre cada valor con un mensaje descriptivo

Muestre el tipo de dato de cada variable usando type()
"""
# Ejercicio 1 corregido
name = input("Enter your name... ")
age = int(input("Enter your age... "))
height = float(input("Enter your height in meters... "))
student = input("You are studying--- True or False: ").lower() == "true"

print(f"Su nombre es {name} y su edad {age}, su altura es de {height} metros, "
      f"y usted se encuentra estudiando {student}")

# Mostrar tipos de datos
print(f"Tipo de name: {type(name)}")
print(f"Tipo de age: {type(age)}")
print(f"Tipo de height: {type(height)}")
print(f"Tipo de student: {type(student)}")