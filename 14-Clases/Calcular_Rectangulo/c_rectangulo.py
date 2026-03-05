class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return (2 * self.base ) + (2 * self.altura)
    
base = float(input("Digite la base "))
altura = float(input("Digite la altura "))

rectangulo = Rectangulo(base, altura)
print("El área del rectangulo: ", rectangulo.calcular_area())
print("El perímetro del rectángulo: ", rectangulo.calcular_perimetro)