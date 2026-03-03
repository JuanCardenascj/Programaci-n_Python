#Ahora nivel más fino -> Predice esto:
class A:
    def __new__(cls):
        print("New")
        return super().__new__(cls)

    def __init__(self):
        print("Init")

a = A()

#Python primero lee a new