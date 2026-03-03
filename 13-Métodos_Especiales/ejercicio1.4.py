#Ahora te hago una prefunta que separa niveles - Predice esto:
class Contador:
    def __init__(self, valor):
        self.valor = valor

    def __call__(self, incremento): #Porque se usa para booleanos
        return self.valor + incremento

c = Contador(10)

print(callable(c))
print(callable(5))
print(callable(lambda x: x))

#Un ojeto es callable si:
#Es una función
#Es una clase (las clases son callables porque crean instancias)
#Tiene definido el método __call__