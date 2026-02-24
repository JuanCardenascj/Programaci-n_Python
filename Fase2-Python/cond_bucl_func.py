"""🔹 Fase 2: Condicionales, bucles y funciones
1️⃣ Conceptos clave

Condicionales: if / elif / else

Bucles: while y for

Manejo de errores: try/except

Funciones: def nombre_funcion(): con return"""

#Ejemplo

def analizar_numero(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else: 
        return "Cero"
    
x = analizar_numero(10)
print(x)


"""2️⃣ Preguntas de razonamiento
¿Qué pasa si llamas a analizar_numero(-5) pero no guardas el resultado ni lo imprimes?

Respuesta: No pasa nada, no imprime ni muestra nada, pero si fue retornado un valor en el return y en este caso fue negativo!

¿Por qué es mejor que una función devuelva un valor en vez de imprimirlo dentro?

Respuesta: 1. Permite guardarse en una variable para usarlo despues
           2. Pasarse a otra función
           3. Hacerse cálculos cuando quieras
           4. Imprimirse cuando quieras
Analogía:
         1. Return -> Entrega un paquete a quine lo pide (se puede abrir, guardar o enviar)
         2. Print -> Gritar el contenido del paquete, pero nadie puede usarlo después.

¿Qué diferencia hay entre un bucle while y un bucle for?

1. While:
       1.1. Se ejecuta mientras la condición sea verdadera.
       1.2. No sabe de antemano cuántas veces se ejecutará.
       1.3. Riesgo de bucle infinito si no se actualiza la condición.

2. For: 
      2.1. Se ejecuta número determinado de veces, generalmente iterando sobre una secuencia (lista, rango, cadena, etc...!)
      2.2. Ideal cuando sabes cuántos elementos vas a recorrer.
"""

