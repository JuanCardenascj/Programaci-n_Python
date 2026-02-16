"""Clase: La receta para construir un objeto
   Objeto: Caracteristicas y cualidades de un objeto"""

class Celular(): #Pascal_Case_Definir_Clase_Python || Buenas Prácticas
    def __init__(self, marca, modelo, camara): #Método __init__ contiene los atributos de la clase
        self.marca = marca #Atributos de la clase || Acceder a los atributos
        self.modelo = modelo #Atributos de la clase || Acceder a los atributos
        self.camara = camara #Atributos de la clase || Acceder a los atributos

    def llamar(self):#Metodos para definir las acciones de nuestros objetos
        print("Estas haciendo una llamada")

Celular1 = Celular("Iphone","15pro","5") #Creación del objeto

print(Celular1.camara)


"""Clase: Es la que contiene los Atributos, Métodos, Objetos
   Atributos: Caracteristicas de la clase
   Métodos: Acciones de la clase
   Objetos: tienen atributos y métodos que son utilizados de la clase"""

class Bicicleta:
    def __init__(self, color, cambios, rines):
        self.color = color
        self.cambios = cambios
        self.rines = rines

    #Creamos los Métodos || Comportamientos de la clase!
    def frenar(self):
        return "La bicileta está frenando."
    
    def avanzar(self):
        return "La bicicleta está en movimiento!"
    
    def girar(self):
        return "La bicileta está girando...!!"
    
#Creamos los Objetos || Instancias
urbana = Bicicleta("Red", 12, 23.5)
hibrida = Bicicleta("Blue", 2, 27.3)

#Imprimimos
print(urbana.color) #Atributos no llevan parentesis
print(urbana.girar()) #Métodos si llevan parentesis