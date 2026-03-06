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