#Construye una calculadora
numero1 = input("Ingrese el primer número: ")
numero2 = input("Ingrese el segundo número: ")
operacion = input("Ingrese la operación (+, -, *, /): ")

if operacion == "+":
    resultado = float(numero1) + float(numero2)
    print("El resultado de la suma es:", resultado)
elif operacion == "-":
    resultado = float(numero1) - float(numero2)
    print("El resultado de la resta es:", resultado)
elif operacion == "*":
    resultado = float(numero1) * float(numero2)
    print("El resultado de la multiplicación es:", resultado)
elif operacion == "/":
    resultado = float(numero1) / float(numero2)
    print("El resultado de la división es:", resultado)
else:
    print("Operación no válida")