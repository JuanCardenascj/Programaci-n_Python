"""Es una colección de elemento donde:
   1. Cada elemento guarda un dato
   2. y una referencia al siguiente elemento
   
A diferencia de una lista normal, los elementos no están uno al lado del otro en memoria

  Comparación rápida con listas normales
  [10][20][30][40]
  
  Comparación rápida con lista enlazada
  [10 | *] → [20 | *] → [30 | *] → [40 | None]

Cada nodo tiene:
   1. el valor
   2. un enlace al siguiente nodo
   
   Concepto clave: NODO
   un nodo tiene dos partes:
   1. Dato
   2. Referencia"""
   
#Ejemplo Conceptual
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

#Lista enlazada simple
nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

"""Operaciones que se deben entender"""
#Recorrer una lista
actual = nodo1

while actual:
    print(actual.dato)
    actual = actual.siguiente

#Insertar nodo
nuevo = Nodo(5)
nuevo.siguiente = nodo1
nodo1 = nuevo
