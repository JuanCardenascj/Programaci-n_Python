"""
🔥 Nuevo ejercicio de nivel adecuado

Vamos a unir todo lo que ya sabes.

Ejercicio:

Haz un programa que:

Pida al usuario un número.

Permita escribir "salir" para terminar.

Valide que lo ingresado sea número.

Si es número:

Si es positivo → imprimir "Positivo"

Si es negativo → imprimir "Negativo"

Si es 0 → imprimir "Es cero"

Si no es número → mostrar error y continuar.

Debe usar:

while

try/except

.strip().lower()

break
"""


while True:
    entrada = input("Digite un numero o escriba 'salir' para terminar: ").strip().lower()

    if entrada in ["salir", "exit", "quit", "cerrar", "output"]: #La escribes como una lista!
        break

    try:
        numero = float(entrada)

        if numero == 0:
            print("El número es 0..!")
        elif numero > 0:
            print("El número es positivo..!")
        else:
            print("El número es negativo..!")

    except ValueError:
        print("Error: Debe ingresar un número válido.")