"""Instrucción:

Crea una variable personas que sea una lista de diccionarios
Cada diccionario debe tener: nombre, edad
Agrega 2 personas
Muestra el nombre de la segunda persona

Explicación:
personas[1] → Accede al segundo elemento de la lista
personas[1]["nombre"] → Accede a la clave "nombre" del segundo diccionario
"""

persona = [
    {"Nombre" : "David", "edad" : 30},
    {"Nombre" : "Daniel", "edad" : 23}
]
print(persona)
print(persona[1]["Nombre"])