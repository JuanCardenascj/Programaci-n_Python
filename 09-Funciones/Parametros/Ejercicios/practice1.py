#Para operar de manera sencilla...!

def sumar(numero1, numero2):
    resultado = numero1 + numero2 
    print(f"La suma entre {numero1}  y {numero2} es igual a: {resultado}")

def resta(numero1, numero2):
    resultado = numero1 - numero2
    print(f"La resta entre {numero1}  y {numero2} es de: {resultado}")

def multiplicacion(numero1, numero2):
    resultado = numero1 * numero2
    print(f"La multiplicación entre {numero1} y {numero2} es de: {resultado}")

def dividir(numero1, numero2):
    resultado = numero1 / numero2
    print(f"La división entre {numero1} y {numero2} es de: {resultado}")

print("Bienvenido a las operaciónes aritméticas ....!!! ")
numero1 = int(input("Por favor ingrese el primer número: "))
numero2 = int(input("Por favor ingrese el segundo número: "))
operacion = input("Que operación desea ejecutar ....! ")

if operacion == 'sumar':
    sumar(numero1, numero2)
elif operacion == 'resta':
    resta(numero1, numero2)
elif operacion == 'multiplicacion':
    multiplicacion(numero1, numero2)
elif dividir == 'dividir':
    dividir(numero1, numero2)
else:
    print('No digito ninguna operación correcta...!')