#Crea un programa que:  Guarde el numero 27 en una variable llamada numero. Imprima el doble de ese numero. Imprima el residuo de dividirlo entre 5. Compruebe si el número es mayor que 20 e imprima el resultado

numero = 27
print(numero * 2)
print(numero % 5)
if numero > 20:
    print("El número es mayor que 20")
else:
    print("El número no es mayor que 20")