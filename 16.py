def es_mayor_de_edad(edad):
    return edad >= 18

edades = [12, 20, 17, 35, 16, 22]
edades_mayores = []

for edad in edades:
    if es_mayor_de_edad(edad):
        edades_mayores.append(edad)
print("Edades mayores de edad:", edades_mayores)

cantidad = len(edades_mayores)
print("Cantidad de personas mayores de edad:", cantidad)

suma = sum(edades_mayores)
print("Suma de las edades mayores de edad:", suma)
promedio = suma / cantidad if cantidad > 0 else 0
print("Promedio de las edades mayores de edad:", promedio)