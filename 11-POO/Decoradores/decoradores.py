"""Es un concepto que se usa para cosas avanzadas.
1. En python un decorador es un función especial que decora a otra.!
2. Toma una función de entrada, le agrega un función extra y la devuelve modificada!
3.Utilizados para el manejo de excepciones"""

def decorador(funcion):
    def funcion_modificada(): #Crea una función decorada
        print("Antes de llamar a la función modificada") #Ejecuta un codigo antes
        funcion() #Ejecuta la función que se le paso como parametro
        print("Despues de la llamar a la función") #Ejecuta un codigo despues
    return funcion_modificada #Y luego devuelve el resultado final

# def saludo():
#     print("Hola Dalto, como andas?")

# saludo_modificado = decorador(saludo)
# saludo_modificado()

#Es lo mismo que está comentado, pero es la forma decoradora con @
@decorador
def saludo():
    print("Hola Dalto como andas")

saludo()