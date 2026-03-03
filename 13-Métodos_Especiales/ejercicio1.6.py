#Ahora pregunta seria -> Predice esto:
class A:
    def __init__(self):
        print("Init")

    def __call__(self):
        print("Call")

print(callable(A))
a = A()
a()

#Por qué ocurre en ese orden?
#No es por jerarquía, es por qué instrucción se ejecuta primero.
