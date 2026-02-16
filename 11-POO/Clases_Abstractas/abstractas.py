"""Clases Abstractas_:
Son clases que no se pueden instanciar, pero son como recetas que permiten crear clases apartir de esas plantillas
Un modelo para todo lo demas, un modelo para crear otras clases!"""

from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractclassmethod
    def trabajar(self):
        pass

    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)

    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")

dalto = Estudiante("Lucas", 21, "Masculino", "Programador")

dalto.hacer_actividad()