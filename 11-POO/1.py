"""POO: Lol!

1. Clase: Es el molde o plantilla que define cómo sera un tipo de objeto
2. Objeto: Es un elemento concreto creado a partir de esa clase

¿Que es el Self? --> Es para guardar el nombre dentro de este objeto
"""

#Clase: Campeon --> Nombre, Vida, Daño, Ataque
#Objeto: Garen, 300, 900, velocidad

class Campeon: #Clase molde o plantilla
    def __init__(self, nombre, vida, dano):
        self.nombre = nombre
        self.vida = vida
        self.dano = dano

    def atacar(self, objetivo):
        if self.vida <= 0: #Vida del atacante
            print(f"{self.nombre} no puede atacar porque ha sido derrotado.")
            return

        if objetivo.vida <= 0: #Vida del objetivo
            print(f"{objetivo.nombre} ya ha sido derrotado.")
            return #Si está muerto, no se ejecuta, sale del método, detiene ejecución

        objetivo.recibir_dano(self.dano)

        if objetivo.vida <= 0:
            print(f"{objetivo.nombre} ha sido derrotado.!")

    def recibir_dano(self, dano):
        self.vida -= dano

        if self.vida < 0:
            self.vida = 0

        print(f"{self.nombre} recibe {dano} de daño.")

nombre = input("Escribe el nombre del campeón: ")
vida = int(input("Escribe la vida del campeón: "))
dano = int(input("Escribe el daño del campeón: "))

garen = Campeon(nombre, vida, dano)
print(garen.nombre, garen.vida, garen.dano)


nombre_ahri = input("Escribe el nombre de otro campeón: ")
vida_ahri = int(input("Escribe la vida del otro campeón: "))
dano_ahri = int(input("Escribe el daño del otro campeón: "))

ahri = Campeon(nombre_ahri, vida_ahri, dano_ahri)
print(ahri.nombre, ahri.vida, ahri.dano)


while True:
    atacante = input("¿Quién va a atacar? Escribe Garen o Ahri: ")
    objetivo = input("¿Quién recibirá el ataque? Escribe Garen o Ahri: ")

    if atacante == "Garen" and objetivo == "Ahri":
        garen.atacar(ahri)
    elif atacante == "Ahri" and objetivo == "Garen":
        ahri.atacar(garen)
    else:
        print("Selección no válida.")

    print("Vida de Garen:", garen.vida)
    print("Vida de Ahri:", ahri.vida)

    if garen.vida <= 0 or ahri.vida <= 0:
        print("¡Fin del combate!")
        break

    continuar = input("¿Quieres realizar otro ataque? (si/no): ")

    if continuar.lower() == "no":
        break