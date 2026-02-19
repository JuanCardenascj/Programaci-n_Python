"""
🧠 Ahora entramos oficialmente en Nivel 2 mental
🔵 Manejo de Excepciones

En sistemas reales no podemos permitir que el programa se detenga porque el usuario escribió mal algo.

Imagínate:

Sistema bancario → usuario escribe mal → el sistema se cae

Sistema de tu empresa → usuario pone mal un dato → el sistema se detiene

Eso es inaceptable.
"""

#Solución - TRY and EXCEPT
try:
    nota = int(input("Digite la nota: "))
    print("Número válido")
except ValueError:
    print("Error: Debe ingresar un número entero")

print("Programa continúa")

# 🔎 ¿Qué pasa aquí?
# Python intenta ejecutar el bloque try.
# Si todo sale bien → continúa.
# Si ocurre un ValueError → salta al except.
# El programa NO se detiene.

#Concepto profundo: Esto se llama control de flujo por excepciones, No es lo mimso que un (if).
#El (if) evalúa condicones. 
#El (try/except) maneja errores en tiempo de ejecución o tiempo real.!