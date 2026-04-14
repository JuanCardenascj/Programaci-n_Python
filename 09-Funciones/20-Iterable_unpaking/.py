"""Desempaquetado iterable!
Son cualquier estructura de datos capaz de entregar sus elementos uno en uno"""

def imprimir_nombre(primer_nombre, segundo_nombre, primer_apellido, segundo_apellido):
    print(f"Hola {primer_nombre} {segundo_nombre} {primer_apellido} {segundo_apellido} Bienvenido al curso...!")

estudiante = ("Sofia", "Daniel", "Contreras", "Cetares") #Define tupla con diferentes valores
imprimir_nombre(*estudiante) #Para que sea desempaquetado