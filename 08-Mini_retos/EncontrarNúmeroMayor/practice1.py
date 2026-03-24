#Qué imprimirá?
numeros = [5,2,9,4]

mayor = numeros[0]

for n in numeros:
    if n > mayor:
        mayor = n

print(mayor)
