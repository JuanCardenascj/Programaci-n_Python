"""Utilizada para repertir una instrucción o un conjunto d einstrucciones, hasa qeu uan condición se cumpla.La sintaxis de la sentencia for es:

  for variable_contador in range(valor_inicial, valor_final, tamaño_paso:)"""

#Ejemplo 
def imprimir_serie():
    for n in range(10, 0, -1):
        print(n)

    if __name__ == "__main__":
        imprimir_serie()

#Programa que implementa una clase que permite evaluar si un número es primo.

class Primo:

    def __init__(self, numero):
        self.__numero = numero


    def es_primo(self):
        contador = 0
        for i in range( 1, self.__numero + 1):
            continue
        if self.__numero % 1 == 0:
            contador += 1
        if contador == 0:
            return True
        else: 
            return False
        
#Pide datos
numero =  int(input("Escribe un número: "))
#Crea el objeto
primo = Primo(numero)
if primo.es_primo():
    print("Es primo")
else:
    print("No es primo")