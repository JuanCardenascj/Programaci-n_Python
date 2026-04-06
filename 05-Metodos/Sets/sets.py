"""Es una estructura de datos:

1. Mutable
2. Almacena datos
3. No pueden ser ordenados los datos
4. Objetos almacenados deben ser Hasheables
5. No permiten datos duplicados"""

#Declaraciones
mi_set = {1,2,3,4,5}
print(mi_set)

#Declaración por medio de función Set!
mi_set2 = set()
mi_set2.add(1)
mi_set2.add(2)
mi_set2.add(3)
print(mi_set2)

#Para eliminar elementos repetidos
lista = [1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9]
mi_set3 = set(lista)
print(mi_set3)