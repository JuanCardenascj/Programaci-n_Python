"""Crear una clase que se llame estudiante, con los atributos: Nombre, Edad, Grado. Con los metodos estudiar y que imprima el estudiante está estudiando"""

#Primera parte Funcional - Pero aun no está listo!
class Estudiante1:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

estudiante1 = Estudiante1("Juan",29,"SextoSemestre")
print(estudiante1.nombre)


#Segunda parte Funcional. que interactua con el usuario - Pero aun no está listo!
class Estudiante2:
    def __init__(self,nombre2,edad2,grado2):
        self.nombre2 = nombre2
        self.edad2 = edad2
        self.grado2 = grado2

    #Se crea el metodo o acciones estudiar
    def estudiar(self):
        print("Estudiando....!")

nombre2 = input("Digite su Nombre: ")
edad2 = input("Digite su Edad: ")
grado2 = input("Digite su Grado: ")

#El objeto (Estudiante2)
estudiante2 = Estudiante2(nombre2,edad2,grado2)

print(f"""
      DATOS DEL ESTUDIANTE: \n \n
      Nombre: {estudiante2.nombre2}\n
      Edad: {estudiante2.edad2}\n
      Grado: {estudiante2.grado2}\n
      """)

estudiar = input()
if (estudiar.lower() == "estudiar"):
    estudiante2.estudiar()

