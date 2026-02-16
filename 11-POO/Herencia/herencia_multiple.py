class Persona: 
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre  = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola, estoy hablando un poco")

class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad

    #Crea el método constructor
    def mostrar_habilidad(self):
        print(f"Mi habilidad es: {self.habilidad}")

#Para heredar de manera multiple
class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre,edad,nacionalidad,habilidad,empresa, salario):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        print(f"Hola, soy {self.nombre}")
        self.mostrar_habilidad()
        print(f"Trabajo en {self.empresa}")

#Crea el objeto e imprime
roberto = EmpleadoArtista("Roberto", 59, "Argentino", "Cantar", "Google", 12000)

#Llama el método
roberto.presentarse()