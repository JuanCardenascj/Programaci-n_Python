#Sistema para una escuela.!
class Persona():
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def Datos(self):
        print(f"Bienvenido: {self.nombre}, su edad es: {self.edad}")


class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado = grado

    def Grado(self):
        print(f"El grado al que usted pertenece es: {self.grado}")

#Creamos el objeto para los datos, ya que no se está pidiendo datos, entonces nosotros mismo debemos ingresarlos!
datos_clase = Estudiante("Juan David", 30, "Sexto Semestre")

#Llamamos el método para que este se imprima.
datos_clase.Grado()