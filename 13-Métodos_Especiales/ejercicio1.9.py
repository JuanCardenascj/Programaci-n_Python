#Ahora viene algo que te vuela la cabeza un poco --> Predice esto:
class A:
    def __new__(cls):
        print("New")
        return 5

    def __init__(self):
        print("Init")

a = A()
print(a)
print(type(a))

#Conclusión Poderosa... -> __new__ Puede:
#Cambiar el tipo del objeto
#Evitar que __init__ se ejecute
#Controlar completamente la creación de instancias