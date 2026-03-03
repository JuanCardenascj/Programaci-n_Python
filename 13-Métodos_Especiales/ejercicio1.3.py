#Ahora vamos a romperte un poco el cerebro -> Predice esto:
class Contador:
    def __init__(self, valor):
        self.valor = valor

    def __call__(self, incremento): #Permite que el objeto se comporte como función
        self.valor += incremento
        return self.valor

c = Contador(10)

print(c(5))
print(c(3))