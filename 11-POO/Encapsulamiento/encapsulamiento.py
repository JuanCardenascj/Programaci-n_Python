"""El encapsulamiento hace referencia a la capacidad que tiene un objeto de ocultar su estado, de manera que sus datos solo se puedan modificar pos los métodos asesores!

Por defecto todos los atributos y métodos de una clase son públicos, es decir que se puede acceder a los atributos y métodos de dicha clase."""

class Persona:
    def __init__(self, identificacion, nombre, edad):
        self.__identificacion = identificacion #Doble guion bajo. Privado!
        self.nombre = nombre
        self.edad = edad
    
    def saludo(self):
        return "Hola"
    
    #Para acceder o obtener con el GETTER
    def getIdentificacion(self):
        return self.__identificacion
    
persona1 = Persona(11654847987, "David", 30)
print(persona1._Persona__identificacion) #Para poder acceder a el atributo privado