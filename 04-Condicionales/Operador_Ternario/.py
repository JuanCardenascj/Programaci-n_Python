"""Operador Ternario... Resumir la lógica en una sola linea de codigo
Utilizado para asignarle valores a una variable, deacuerdo a una condición"""

edad = int(input("Por favor Ingrese su edad.... "))
mensaje = ""

if edad >= 18:
    mensaje = "Usted es mayor de edad"
else:
    mensaje = "Usted es menor de edad"

print(mensaje)

#Utilizando el ternario
mensaje = "Usted es mayor de edad" if edad >= 18 else "Usted es menor de edad" #En una sola linea de codigo
print(mensaje)