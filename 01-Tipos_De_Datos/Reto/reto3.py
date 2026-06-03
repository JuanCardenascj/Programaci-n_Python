"""
Crea un programa que gestione estudiantes:

Guarda los nombres en una lista.
Guarda las materias en una tupla.
Guarda los códigos únicos en un set.
Guarda las notas en un diccionario.

Al final muestra toda la información organizada.

Este reto combina las 4 estructuras de datos principales y es muy parecido a los ejercicios que suelen aparecer en cursos iniciales de programación y estructuras de datos.
"""

estudiantes = ["Silvia", "Daniel", "Sarajuan", "Nadiel", "Astrubal"]
materias = ("Matemáticas", "Sociales", "Quimica", "Estadistica", "Curiosos")
codigos = {213, 231, 453, 562, 253}
notas1 = {"not1" : 5.0,
         "not2" : 5.0,
         "not3" : 4.3,
         "not4" : 5.0,
         "not5" : 3.2}

print(f"Los estudiantes: {estudiantes}, que cursaron las siguiente materias: {materias}, con los codigos de identificación: {codigos}, obtuvieron las siguientes notas: {notas1}")

print("!!!!Ahora!!!!!")

for estudiante in estudiantes:
    print(estudiantes)