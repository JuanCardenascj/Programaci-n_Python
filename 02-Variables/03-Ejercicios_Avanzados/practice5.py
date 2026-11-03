"""Instrucción:

Crea una variable global mensaje = "Hola"
Dentro de una función, crea una variable local con el mismo nombre
Muestra el valor dentro y fuera de la función

Explicación:
Variables globales: existen en todo el programa
Variables locales: solo existen dentro de la función
"""
mensaje = "Hola global"

def cambiar_mensaje():
    mensaje = "Hola local"
    print(mensaje)  # Hola local

cambiar_mensaje()
print(mensaje)  # Hola global