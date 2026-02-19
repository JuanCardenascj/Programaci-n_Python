"""Son estructurasw donde los datos se guardan en pares:
   --> Clave - Valor
   
   
   Caracteristicas Importantes_
   1. Búsquedas extremadamente rápidas
   2. No dependen del orden
   3. Muy usadas en sistemas reales
   4. Contar frecuencias
   5. Simula base de datos 
   6. Evitar O(ncuadratica)

Un diccionario internamiente es:_ Una tabla Hash.... y eso signifca acceso en o(1) 

¿ por que usa Hashing ? -> Porque convierte una clave en numero
   """

#Diccionario
worked = {
    "nombre": "Jorge",
    "edad": 20,
    "trabajo": "Ingeniero",
    "perfil": "Atención"
}

#Imprime el diccionario
print(worked)

"""Operaciones Básicas"""

#Accedeer a un valor
print(worked["nombre"])

#Agregar dato
worked["ciudad"] = "Arauca"

#Eliminar dato
del worked["perfil"]


#Ejemplo simple pero poderoso - Supón que quieres saber cuántas veces aparece cada número.

lista = [1, 2, 1, 3, 4, 3, 5, 4] #Sin diccionario -> O(n2)

#Con diciconario:
frecuencias = {}

for numero in lista:
    if numero in frecuencias:
        frecuencias[numero] += 1
    else:
        frecuencias[numero] = 1

print(frecuencias) #Complejidad O(n)

#O(1) - Solo cuando buscas por clave ID
#O(n) - Solo cuando buscas por el nombre
"""Pero si se quiere buscar por nombre también sea O(1), necestia otra estructura:
   
usuarios_por_nombre = {
    "Juan": 1,
    "Ana": 2,
    "Pedro": 3
}

usuarios_por_nombre["Juan"] Eso es O(1) y se llama indexación
   """