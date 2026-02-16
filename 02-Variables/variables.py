"""1. Es un espacio en memoria donde guardamos información
   2. Son variables porque pueden variar su valor"""

nombre = "David" #Primero declara y luego la define
nombre = "Cárdenas"
nombre = "Jorge"

"""Concatenar con +"""
pasada = "Hola " + " ¿Como estás"

"""Ahora la concatenación con f-strings"""
bienvenida = "Hey"
salida = "Next"
resultado = f"Hola {bienvenida} ¿Como estas?"  

"""operadores de pertenecencia (in / not in)"""
print("Jorge" in bienvenida) #False
print("Hola" not in bienvenida) #True

print(resultado)
print(pasada)
print(nombre)