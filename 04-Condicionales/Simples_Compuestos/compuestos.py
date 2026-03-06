"""Programa que implementa los métodos para calcular el diámetro, longitud y área de la circunferencia, evaluando que el radio sea mayor que cero.!"""

from math import pi

class Circunferencia:

#Crea el constructor
    def __init__(self, radio = 0):
        self.radio = radio

#Crea los Métodos
    def calcular_diametro(self):
        diametro = self.radio * 2
        return diametro
    
    def calcular_longitud_circunferencia(self):
        longitud = 2 * pi * self.radio
        return longitud
    
    def calcular_area_circunferencia(self):
        area = pi * self.radio * 2

#Pide los datos al usuario
radio = float(input("Ingresa el valor del radio: "))
if radio > 0:
    unaCircunferencia = Circunferencia(radio)
    print("Diametro: " + str(unaCircunferencia.calcular_diametro()))
    print("Longitud: " + str(unaCircunferencia.calcular_longitud_circunferencia()))
    print("Area: " + str(unaCircunferencia.calcular_area_circunferencia()))
else:
    print("Error el radio debe ser mayor que cero")