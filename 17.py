numeros = []

for i in range(5):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

print("Lista completa:", numeros)

pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Números pares:", pares)
print("Números impares:", impares)