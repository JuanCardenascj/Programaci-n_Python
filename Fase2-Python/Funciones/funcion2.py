"""
🔹 Objetivo del ejercicio

Crear una función que:

Pida al usuario que ingrese un número.

Valide que sea un número entero (no letras, no decimales) usando try/except.

Devuelva el número si es válido.

Si el usuario digita algo inválido, muestre un mensaje de error y vuelva a pedir el número.

Esto combina bucles, manejo de errores y funciones, todo modularizado.
"""

def pedir_entero(mensaje): #La función def.!
    while True:  # Repite hasta que sea correcto.!
        entrada = input(mensaje)
        try: #Manejo de errores.!
            numero = int(entrada)  # Intentamos convertir a entero
            return numero          # Si es correcto, devolvemos
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

numero_usuario = pedir_entero("Digite un número entero: ")
print("Número ingresado:", numero_usuario)


"""
🎯 Ejercicio para ti

Escribe tu propia función que haga lo mismo, pero que además:

Valide que el número esté en un rango (por ejemplo, 0 a 5)

Devuelva el número si es correcto

Muestre mensaje de error si es fuera de rango o no es número

Luego, llama a tu función y muestra el número ingresado.

Hazlo tú primero, y después lo revisamos paso a paso.
"""

# Función para pedir un número con validación
def pedir_numero_rango(mensaje, min_val=0, max_val=5):
    while True:
        entrada = input(mensaje)
        if entrada.lower().strip() == "salir":
            return None  # Permite salir del programa
        try:
            numero = float(entrada)  # Convertimos a número
            if min_val <= numero <= max_val:
                return numero
            else:
                print(f"Nota inválida. Debe estar entre {min_val} y {max_val}.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# Función para analizar el número
def analizar_numero(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Cero"

# --- Programa principal ---
while True:
    nota = pedir_numero_rango("Digite una nota (0 a 5) o 'salir': ")
    if nota is None:  # Usuario decidió salir
        print("Programa terminado.")
        break

    resultado = analizar_numero(nota)
    print(f"La nota {nota} es {resultado}.")

    # Puedes añadir lógica extra, por ejemplo aprobado/reprobado
    if nota >= 3:
        print("Estado: Aprobado ✅")
    else:
        print("Estado: Reprobado ❌")