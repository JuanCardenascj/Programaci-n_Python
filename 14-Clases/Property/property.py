class Estudiante:

    def __init__(self, id, nombre, apellido):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

#Crea el Objeto
estudiante = Estudiante(1, "Juan david", "Cárdenas")

#Utilizar los métodos get
print(f"ID: {estudiante.id}, Nombre: {estudiante.nombre}, Apellido: {estudiante.apellido}")

#Utilizar los métodos set
estudiante.id = 2
estudiante.nombre = "Juliana J"
estudiante.apellido = "Sofia"

#Verificar los cambios
print(f"ID: {estudiante.id}, Nombre: {estudiante.nombre}, Apellido: {estudiante.apellido}")