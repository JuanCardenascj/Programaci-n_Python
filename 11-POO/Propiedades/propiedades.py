class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    
    #Crear el getter con Propperty
    @property
    def nombre(self):
        return self._nombre
    
    #Crear el setter con Propperty
    @nombre.setter
    def nombre(self, new_nombre):
        self._nombre = new_nombre

dalto = Persona("Lucas", 21)

nombre = dalto.nombre
print(nombre)

dalto.nombre = "Pepe"

nombre = dalto.nombre
print(nombre)