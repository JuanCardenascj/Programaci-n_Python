#args -> es para utilizar N cantidad de elementos
def suma(*args):
    return sum(args) #Función integrada de python, para que sume lo que tenga

resultado = suma(32, 543, 2, 6, 6543, 12, 65)
print(f"El resultado es: {resultado}")