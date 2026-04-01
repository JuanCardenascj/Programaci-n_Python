"""Es una estructura de datos inmutable y permite almacenar una secuencia de objetos
y permite acceder a ellos atravez del indice..!"""

mi_tupla = (123, False, "edwar", 0.6434)
print(mi_tupla[0])

#Caracteristicas - Puede retornar mas de un elemento en una función
def retornar_estudiante():
    return 'David', 94, 0.4 #Retorna valores internamente
tupla_estudiante = retornar_estudiante() #Crea la tupla, y llama la función
print(tupla_estudiante) #Imprime la tupla

#Caracteristica - Crea multiples variables en una sola linea
nombre_estudiante, edad_estudiante, promedio_estudiante = retornar_estudiante()
print(nombre_estudiante)
print(edad_estudiante)
print(promedio_estudiante)

#Cambiar valores de las variables
variable_1 = 2
variable_2 = 3

variable_tempo = variable_1
variable_1 = variable_2
variable_2 = variable_tempo

print(variable_1, variable_2)