"""Instrucción:

Crea una función sumar(a, b) que devuelva a + b
Crea una variable operacion que guarde la función
Usa la variable para llamar a la función

Explicación:
Las funciones también se pueden guardar en variables
operacion = sumar → La variable ahora contiene la función
"""
def sumar(a, b):
    return a + b

operacion = sumar
resultado = operacion(5, 3)
print(resultado)