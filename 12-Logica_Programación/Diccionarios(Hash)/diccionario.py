"""Son estructurasw donde los datos se guardan en pares:
   --> Clave - Valor
   
   
   Caracteristicas Importantes_
   1. Búsquedas extremadamente rápidas
   2. No dependen del orden
   3. Muy usadas en sistemas reales"""

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