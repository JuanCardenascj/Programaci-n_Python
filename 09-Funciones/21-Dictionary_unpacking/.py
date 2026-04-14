"""No importa el orden en como esten definidos cada uno de los elementos"""
def imprimir_nombre(primer_nombre, segundo_nombre, primer_apellido, segundo_apellido):
    print(f"Hola {primer_nombre} {segundo_nombre} {primer_apellido} {segundo_apellido} Bienvenido al curso...!")

estudiante = {
    "primer_nombre" : "Samuel",
    "segundo_nombre" : "David",
    "primer_apellido" : "Salcedo",
    "segundo_apellido" : "Jimenez"
}

imprimir_nombre(**estudiante)