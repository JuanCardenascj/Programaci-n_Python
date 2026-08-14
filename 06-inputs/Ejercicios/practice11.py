"""Instrucción:

Pide: nombre, edad, correo y teléfono
Muestra un resumen de los datos

Explicación:
Múltiples variables para guardar múltiples respuestas
"""
nombre = input("Digite su nombre: ")
edad = int(input("Digite su edad: "))
correo = input("Digite su correo: ")
telefono = int(input("Digite su numero de contacto: "))

print(f"Su nombre es: {nombre} y su edad {edad}, el numero donde podemos contactarlo es: {telefono} y su correo: {correo}")