#Crea una función que reciba dos números y una operación (suma, resta, multiplicación, división) y devuelva el resultado.
def calculadora(a, b, operacion):
    if operacion == "suma":
        return a + b
    elif operacion == "resta":
        return a - b
    elif operacion == "multiplicacion":
        return a * b
    elif operacion == "division":
        if b != 0:
            return a / b
        else: 
            return "Error: División por cero"
    else: 
        return "Operación no válida"

# Prueba
print(calculadora(5, 3, "suma"))       # 8
print(calculadora(10, 2, "division"))  # 5.0c
print(calculadora(21, 2, "resta"))
print(calculadora(21, 23, "multiplicacion"))