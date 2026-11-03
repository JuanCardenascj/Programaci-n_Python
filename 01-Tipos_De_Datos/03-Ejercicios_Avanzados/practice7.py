"""
Crea un diccionario:

agenda = {
    "Juan": "3101234567",
    "Ana": "3209876543",
    "Carlos": "3155555555"
}

Pide un nombre.

Si existe:

Número: XXXXX

Si no existe:

Contacto no encontrado
"""

#Creando la agenda telefonica
agenda = {
    "Juan": "3101234567",
    "Ana": "3209876543",
    "Carlos": "3155555555"
}

#Pidiendo nombre al usuario
nombre = input("Digite un nombre a consultar  ")

if nombre in agenda:
    print(f"Si existe {nombre}")
else:
    print("Contacto no en contrado!")