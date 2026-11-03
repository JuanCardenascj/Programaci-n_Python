#Programa - Si el usuario escribe Numero 1 = 7  y Numero 2 = 5
a = int(input("Número 1: "))
b = int(input("Número 2: "))

opcion = int(input("Ingrese 1 para sumar, 2 para restar, 3 para multiplicar, 4 para dividir, 5 para módulo, 6 para exponente: "))

if opcion == 1:
    print("La suma es: ", a + b)
elif opcion == 2:
    print("La resta es: ", a - b)
elif opcion == 3:
    print("La multiplicación es: ", a * b)
elif opcion == 4:
    print("La división es: ", a / b)
elif opcion == 5:
    print("El módulo es: ", a % b)
elif opcion == 6:
    print("El exponente es: ", a ** b)