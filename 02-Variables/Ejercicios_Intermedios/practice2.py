"""Instrucción:

Crea una variable persona que contenga un diccionario con: nombre, edad, ciudad
Muestra el diccionario completo
Muestra solo el nombre

Explicación:
persona = {"nombre": "Ana", "edad": 25} → Guarda el diccionario
persona["nombre"] → Accede al valor de la clave "nombre
"""

persona = {
    "nombre" : "Sanjuil",
    "edad" : 32,
    "ciudad" : "Bogotá"
}

print(persona)
print(f"Su nombre es: {persona['nombre']}")