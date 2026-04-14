"""Pasar argumentos en un orden diferente --> Definiendo subclave

No importa orden, desde que la clave quede bien definida.,!"""
def imprimir_nombre(primer_nombre, segundo_nombre, primer_apellido, segundo_apellido):
    print(f"Hola {primer_nombre} {segundo_nombre} {primer_apellido} {segundo_apellido} Bienvenido al curso...!")

imprimir_nombre(segundo_apellido="Rojas", primer_nombre="David", primer_apellido="Jimenez", segundo_nombre="Alberto")