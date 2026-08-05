"""Instrucción:

Crea un diccionario que tenga como clave el nombre de un estudiante y como valor una lista de notas
Agrega 3 estudiantes
Muestra el promedio de cada uno 
"""

estudiantes = {
    "Ana" : [2.3, 3.2, 5.5, 100],
    "Luis" : [4.5, 5.4, 6.7, 3.4],
    "Carlos" : [1.4, 3.2, 5.4, 4.3]
}

#Agrega los tres estudiantes
estudiantes.update({
    "Safrina" : [2.3, 3.2, 3.2, 4.3]})
estudiantes.update({
    "Daniela" : [3.2, 5.6, 5.4, 3.4]})
estudiantes.update({
    "Zoraida" : [7.6, 8.7, 9.8, 7.6]})

for nombre, notas in estudiantes.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")