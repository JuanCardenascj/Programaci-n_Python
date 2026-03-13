"""Return sirve para devolver un valor desde una función"""

#Ejemplo.!
def sumar(a, b): #Declaración de la función
    return a + b #Retorna el valor de a + b pero no lo muestra en la consola
resultado = sumar(12, 12) #Introduce los valores o los parametros
print(resultado) #Imprime el resultado


#Ejemplo2.!
def cuadrado(x):
    return x * x
print(cuadrado(5))