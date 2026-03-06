"""Un programa que implementa una la Clase Punto, Que permite identificar el cuadrante en el cual esta ubicado los puntos en el plano cartesiano.."""

class Punto:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def determinar_cuadrante(self):
        resultado = ""
        if self.x == 0 and self.y == 0:
            resultado = "Origen"
        if self.x == 0:
            resultado == "Eje Y"
        if self.y == 0:
            resultado == "Eje x"
        if self.x > 0 and self.y > 0:
            resultado = "Cuadrante I"
        if self.x < 0 and self.y > 0:
            resultado = "Cuadrante II"
        if self.x < 0 and self.y < 0:
            resultado = "Cudarante III"
        if self.x > 0 and self.y < 0:
            resultado = "Cuadrante VI"
            return resultado
        
#Pide los datos al usuario
x = int(input("Ingresa el valor de x: "))
y = int(input("Ingresa el valor de y: "))


#Crea el Objeto
punto = Punto(x,y)
print(punto.determinar_cuadrante())