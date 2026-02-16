class Persona: 
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre  = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

#Para crear herencias "(..)"
class Empleado(Persona): #(PASS) Para crear algo pero no definir que va a hacer
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad) #Supper() acceder a métodos constructores de la clase padre (superclase) desde la clase hija o (subclase) -> Llama al constructor del padre
        self.trabajo = trabajo
        self.salario = salario

class Estudiante(Persona):
    def __init__(self,nombre,edad,nacionalidad,notas,universidad):
        super().__init__(nombre,edad,nacionalidad)
        self.notas = notas
        self.universidad = universidad

class Independiente(Persona):
    def __init__(self,nombre,edad,nacionalidad,empresa,rut):
        super().__init__(self,nombre,edad,nacionalidad)
        self.empresa = empresa
        self.rut = rut