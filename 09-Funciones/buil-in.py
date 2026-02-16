numeros = [4,6,1,42,15]

#Encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#Encontrando el numero mas bajo de una lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

#Redondeando a 6 decimales
numero = round(12.345678)
print(numero)

#Retorna False -> 0, vacio, false, ninguno
resultado_bool = bool([])
print(resultado_bool)

#Retorna True, si todos los valores son verdaderos
resultado_all = all([123,"True"]) #Comprueba lo que esta dentro de un iterable
print(resultado_all)