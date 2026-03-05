import math

class Calculadora:

    def __init__(self, x,y):
        self.x = x
        self.y = y

    def sumar(self):
        return self.x + self.y
    
    def restar(self):
        return self.x - self.y
    
    def multiplicar(self):
        return self.x * self.y
    
    def dividir(self):
        return self.x / self.y
    
    def calcular_division_entera(self):
        return self.x // self.y
    
    def calcular_potencia(self):
        return self.x ** self.y
    
    def calcular_residuo(self):
        return self.x % self.y

    def calcular_logaritmo(self):
        return math.log(self.x)

    def calcular_logaritmo_base10(self):
        return math.log10(self.x)

    def calcular_raiz(self):
        return math.sqrt(self.x)

    def calcular_seno(self):
        return math.sin(self.x)

    def calcular_coseno(self):
        return math.cos(self.x)

    def calcular_tangente(self):
        return math.tan(self.x)
    
x = float(input("Digite un número "))
y = float(input("Digite un numero "))

casio = Calculadora(x, y)

#Impresiones
print(x, "+", y, "=", casio.sumar())
print(x, "-", y, "=", casio.restar())
print(x, "x", y, "=", casio.multiplicar())
print(x, "/", y, "=", casio.dividir())
print(x, "//", y, "=", casio.calcular_division_entera())
print(x, "%", y, "=", casio.calcular_residuo())
print(x, "**", y, "=", casio.calcular_potencia())
print(x, "log", "=", casio.calcular_logaritmo())