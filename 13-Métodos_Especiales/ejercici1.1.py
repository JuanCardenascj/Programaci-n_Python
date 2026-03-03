#Ahora subamos de nivel -> Predice esto:
class Libro:
    def __init__(self, paginas):
        self.paginas = paginas

    def __len__(self):
        return self.paginas

l = Libro(150)

print(len(l))