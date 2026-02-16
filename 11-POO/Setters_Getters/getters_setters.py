"""Creamos un objeto de la clase persona que llama Dalto y obtuvimos su nombre con el getter
Despues cambiamos el nombre, se obtuvo la propiedad y se mostro en pantalla"""

class Persona:
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad

    #Crea un Getter - Accede al nombre o un valor privado o muy privado
    def get_nombre(self):
        return self._nombre

    #Crea un Setter
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre  

dalto = Persona("Lucas", 21)

nombre = dalto.get_nombre()
print(nombre)

dalto.set_nombre("Papito")

nombre = dalto.get_nombre()
print(nombre)
