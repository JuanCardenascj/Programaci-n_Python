"""Programe un programa que permite evaluar cual es el mayor de 2 números enteros, como tambien determina si los dos números son iguales"""

class NumeroMayor:

    def __init__(self, x = 0, y = 0):
        self.x = x 
        self.y = y

    def determinar_mayor(self):
        if x > y:
            print(x, "Es mayor que ", y)
        elif x < y:
            print(y, "Es mayor a ", x)
        else:
            print(x, "Es igual a ", y)

x = int(input("Ingresa el valor de x: "))
y = int(input("Ingresa el valor de y: "))

#Objeto
numero = NumeroMayor(x,y)
numero.determinar_mayor()

"""Clase que implementa los métodos para calcular el área del triángulo a partir de los lados aplicando la fórmula de Heron.!"""
import math

class Area_Triangulo:
    def __init__(self, a = 0, b = 0,  c = 0):
        self.a = a
        self.b = b
        self.c = c
        
    def calcular_perimetro(self):
        return (self.a + self.b + self.c)
    
    def calcular_semiperimetro(self):
        return (self.a + self.b + self.c)
    
    def calcular_area_triangulo(self):
        s = self.calcular_semiperimetro()
        #Calcular el area
        area = math.sqrt((s*(s-self.a)*(s-self.b)*(s-self.c)))
        return area
    
#Define o crea el o los objetos
lado1 = int(input("Ingrese el valor del primer lado: "))
lado2 = int(input("Ingrese el valor del segundo lado: "))
lado3 = int(input("Ingrese el valor del tercer lado: "))

if lado1 > 0 and lado2 > 0 and lado3 > 0:
    triangulo = Area_Triangulo(lado1, lado2, lado3)
    print(f" El perimetro del triangulo {triangulo.calcular_perimetro()}")
    print(f"El semi perimetro del triangulo {triangulo.calcular_semiperimetro()}")
    print(f"El area del triangulo {round(triangulo.calcular_area_triangulo(),3)}")
else:
    print("Los tres lados deben ser números positivos.!")