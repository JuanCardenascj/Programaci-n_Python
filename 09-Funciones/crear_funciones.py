#Creando una función simple
def saludar():
    print("Hola Juan David, Profe!")
saludar() #Ejecutando la función simple

#Creando una función con parametros
def saludar2(nombre):
    print(f"Hola {nombre}, mi profe ¿Como vas?")
saludar2("Juan David")

def sexo(nombre1,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        abjetivo = "reina"
    elif (sexo == "hombre"):
        abjetivo = "titan"
    else:
        abjetivo = "crack"
    print(f"Hola {nombre1}, mi {abjetivo} como vas?")
sexo("Camila", "mujer")
sexo("Daniel", "hombre")
sexo("Frank", "no binario")