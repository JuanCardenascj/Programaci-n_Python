#Crea la clase
class Pikachu:
    tipo = 'Electrico'

#Inicializador
    def __init__(self, nombre, nivel, salud, voltaje_max, amperaje_max, color):
        self.nombre = nombre
        self.nivel = nivel
        self.salud = salud
        self.voltaje_max = voltaje_max
        self.amperaje_max = amperaje_max
        self.color = color

#Métodos - añade en el self a lo que deseas acceder
    def atacar(self):
        print(f"Pikachu ataca y genera {self.nivel/4} de daño!")

#Creamos el objeto
pikachu_1 = Pikachu('Dayan',870,400,6,2,'Amarillo')
#Sube de nivel 
pikachu_1.nivel = 1200

#Imprimimos
print(f"Pikachu llamado {pikachu_1.nombre} tiene un nivel {pikachu_1.nivel} y es de tipo {pikachu_1.tipo}")