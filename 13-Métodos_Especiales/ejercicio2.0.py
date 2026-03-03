#Ultimo reto para cerrar este bloque fuerte --> Predice esto:
class A:
    def __new__(cls):
        print("New")
        return super().__new__(cls)

    def __init__(self):
        print("Init")

    def __call__(self):
        print("Call")

a = A()
a()