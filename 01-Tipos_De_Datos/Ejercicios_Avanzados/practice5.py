"""
Crea una lista con nombres:

["Juan", "Ana", "Carlos", "María"]

Luego:

Muestra todos los nombres.
Cuenta cuántos estudiantes hay.
Busca si existe un nombre ingresado por el usuario.
"""

#Creando la lista con los nombres
nombres = ["Juan", "Ana", "Carlos", "María"]

#Mostrando todos los nombres
for nombre in nombres:
    print(nombre)

#Contando cuantos estudiantes hay
print("Cantidad:", len(nombres))

#Buscando si existe un nombre ingresado por el usuario
nombre = input("Inscriba el nombre del estudiante que desea consultar ")

if nombre in nombres:
    print("Si existe")
else:
    print("No existe!")