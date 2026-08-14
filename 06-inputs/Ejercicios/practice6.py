"""Instrucción:

Pide dos números al usuario
Conviértelos a enteros
Calcula la suma
Muestra el resultado

Explicación:
Cada input() es independiente
int() convierte cada uno a número
"""

numero1 = int(input("Digite un numero: "))
numero2 = int(input("Digite un numero: "))

suma = numero1 + numero2
print(f"La suma es: {suma}")