#Mira esto (Nivel Interesante) -> Predice:
class A:
    def __new__(cls):
        print("New")
        return None

    def __init__(self):
        print("Init")

a = A()
print(a)