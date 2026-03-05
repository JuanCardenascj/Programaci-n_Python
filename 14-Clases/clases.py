class Moto:
    def __init__(self, nombre, marca, color, modelo, cilindraje):
        self.nombre = nombre
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.cilindraje = cilindraje

#Para pedir los datos al usuario
nombre = input("Digite el nombre del propietario del vehículo...! ")
marca = input("Digite la marca de su vehículo..! ")
color = input("Digite el color de su vehículo..! ")
modelo = input("Digite el modelo de su vehículo..! ")
cilindraje = input("Digite el cilindraje de su vehículo..! ")

#Objeto: Instancia de una clase
moto = Moto(nombre, marca, color, modelo, cilindraje)
print(f"Hola {moto.nombre} la moto es de una marca {moto.marca}, color {moto.color}, modelo {moto.modelo}, y cilindraje {moto.cilindraje}.... Felicidades Tienes una Buena Moto...!!!")