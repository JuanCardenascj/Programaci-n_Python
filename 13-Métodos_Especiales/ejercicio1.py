# 🔥 Primer ejercicio de métodos mágicos

# Predice esto:

# class Libro:
#     def __init__(self, paginas):
#         self.paginas = paginas

# l = Libro(300)

# print(l)

#Corrección Profesional!!!
class Libro:
    def __init__(self, paginas):
        self.paginas = paginas

    def __str__(self):
        return f"Libro con {self.paginas} páginas"

l = Libro(300)
print(l)

#Diferencia entre __str__ and __repr__ || Estó es nivel fuerte:
#Método -> __str__ Uso -> Representación amigable para usuarios
#Método -> __repr__ Uso -> Representación técnica para desarrolladores

#Ejemplo Profesinal
# class Libro:
#     def __init__(self, paginas):
#         self.paginas = paginas

#     def __str__(self): 
#         return f"Libro con {self.paginas} páginas"

#     def __repr__(self): --> Para consola interactiva
#         return f"Libro({self.paginas})"