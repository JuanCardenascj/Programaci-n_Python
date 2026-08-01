"""
Crea una función que:

Reciba un nombre y una edad
Si no se da edad, que sea 18 por defecto
Devuelva un mensaje
"""

def presentar_persona(nombre, edad=18):
    return f"Hola {nombre} y tu edad es {edad}"
print(presentar_persona("Danna"))
print(presentar_persona("Ana", 20))