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
        if self.vida <= 0:
            print(f"{self.nombre} no puede atacar porque ha sido derrotado.")
            return

        if objetivo.vida <= 0:
            print(f"{objetivo.nombre} ya ha sido derrotado.")
            return

        objetivo.vida -= self.dano

        if objetivo.vida < 0:
            objetivo.vida = 0

        print(f"{self.nombre} ataca a {objetivo.nombre} y le causa {self.dano} de daño.")
        print(f"A {objetivo.nombre} le quedan {objetivo.vida} puntos de vida.")

        if objetivo.vida <= 0:
            print(f"{objetivo.nombre} ha sido derrotado.!")

garen = Campeon("Garen", 700, 100)
ahri = Campeon("Ahri", 500, 100)
velkos = Campeon("Velkos", 6534, 234)
ekko = Campeon("Ekko", 4321, 543)
yasuo = Campeon("Yasuo", 600, 234)

garen.atacar(ahri)
ahri.atacar(garen)
velkos.atacar(garen)
ekko.atacar(garen)

print("Vida restante de Ahri:", ahri.vida)
print("Vida restante de Garen:", garen.vida)


print(garen.nombre, garen.vida, garen.dano)
print(ahri.nombre, ahri.vida, ahri.dano)
print(velkos.nombre, velkos.vida, velkos.dano)
print(ekko.nombre, ekko.vida, ekko.dano)