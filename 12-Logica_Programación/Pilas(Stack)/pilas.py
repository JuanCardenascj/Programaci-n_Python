"""Funciona como una pila de platos:
   1. Ultimo en entrar
   2. Primero en salir
A esto se le define o se le llama -> LIFO (Last In First Out)
   
   Ejemplo real:
   
   1. Historial del navegador
   2. Funciones recursivas
   3. Deshacer acciones
   
   Operaciones Pricipales:
   1. Push -> Agregar
   2. Pop -> Eliminar el último"""

#Pilas - En python usa listas para simular pilas
pila = []

pila.append("A")
pila.append("B")
pila.append("C")
pila.append("D")

#Imprimir la Pila
print(pila)

#Para eliminar el ultimo dato!
print(pila.pop())