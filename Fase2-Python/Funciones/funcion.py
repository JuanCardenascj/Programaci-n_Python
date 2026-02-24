""" ¿Que es una función? 
 Es un bloque de código reutilizable.!
 
   Ejemplo:
   
   def saludar():
    print("Hola gente")
    saludar()"""

#Ejercicio!
#Quiero que construyas esto:
#Una función que:
   #Reciba un número
   #Devuelva si es positivo, negativo o cero
   #No imprima directamente
   #Devuelva el resultado

def analizar_numero(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Cero"
    
resultado = analizar_numero(5)

if resultado == "Positivo":
    print("Número válido para continuar")