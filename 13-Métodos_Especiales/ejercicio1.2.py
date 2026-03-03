#Ahora subimos de nivel..... Mira esto:
class Libro:
    def __init__(self, paginas):
        self.paginas = paginas

    def __add__(self, otro):
        return self.paginas + otro.paginas

l1 = Libro(100)
l2 = Libro(200)

print(l1 + l2)

#Imprime 300 ...!