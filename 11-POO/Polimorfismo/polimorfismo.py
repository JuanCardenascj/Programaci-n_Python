"""El Polimorfismo: Es un variable que puede tomar diferentes tipos de datos"""

#Creamos dos clases
class Gato():
    def sonido(self):
        return "Miau"
    
class Perro():
    def sonido(self):
        return "Guau"
    
#Aplicando polimorfismo
gato = Gato()
perro= Perro()

print(perro.sonido()) #Aca se produce polimorfimos porque usa el mismo metodo

"""Polimorfismo por Sobrescritura (Override)
Ocurre cuando la clase hija redefine un método del padre."""

class Animal:
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        return "Guau"

#El hijo o la hija reemplaza el comportamiento!

