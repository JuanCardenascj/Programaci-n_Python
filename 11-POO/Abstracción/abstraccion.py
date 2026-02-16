"""Abstracción:
Basicamente significa manejar la complejidad ocultando todos los detalles innecesarios, al programador al usuario y solo darle las funcionalidad irrelevantes.!
"""

class Auto():
    def __init__(self):
        self._estado = "Apagado"

    def encender(self):
        self._estado = "Encendido"
        print("El auto está encendido")

    def conducir(self):
        if self._estado == "Apagado":
            self.encender()
        print("Conduciendo el auto")

mi_auto = Auto()
mi_auto.conducir()
