"""Parametros de Funciones: Información del usuario, que es la que nos da el usuario!

   Son esos inputs que le damos a nuestra función para que ejecute una cierta cantidad de tareas especiales....!!
"""

#Se realizaran las operaciones aritmeticas - Se necesitan ciertos inputs.!

def sumar(numero1, numero2):
    resultado = numero1 + numero2 #Para guardar el resultado en esta variable
    print(f"La suma entre {numero1}  y {numero2} es igual a: {resultado}")

def resta(numero1, numero2):
    resultado = numero1 - numero2
    print(f"La resta entre {numero1}  y {numero2} es de: {resultado}")

def multiplicacion(numero1, numero2):
    resultado = numero1 * numero2
    print(f"La multiplicación entre {numero1} y {numero2} es de: {resultado}")

def dividir(numero1, numero2):
    resultado = numero1 / numero2
    print(f"La división entre {numero1} y {numero2} es de: {resultado}")

sumar(250, 3)
resta(250, 3)
multiplicacion(250, 3)
dividir(250, 3)