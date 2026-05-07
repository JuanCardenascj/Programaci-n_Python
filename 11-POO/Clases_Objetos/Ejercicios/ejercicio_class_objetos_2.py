"""Practicando con un segundo ejercicio!

Crear una clase que se llame Familia, con los atributos: 1.Nombre, 2.Edad
Con los metódos: familia y que imprima que es de la familia!"""

class Familia: 
    def __init__(self, nombre, edad, parentesco):
        self.nombre = nombre
        self.edad = edad
        self.parentesco = parentesco

    def familia(self):
        print(f"{self.nombre} es {self.parentesco} de la familia.")

nombre = input("Digite su Nombre: ")
edad = input("Digite su Edad: ")
parentesco = input("¿Qué es en la familia? (tío, primo, sobrino, abuelo, papá, mamá): ")

familia = Familia(nombre, edad, parentesco)

print(f"""
DATOS DEL MIEMBRO DE LA FAMILIA:

Nombre: {familia.nombre}
Edad: {familia.edad}
Parentesco: {familia.parentesco}
""")

familia.familia()

