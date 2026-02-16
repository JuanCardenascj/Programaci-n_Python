"""Los árboles son una de las estructuras más usadas en ingeniería de software y ciencias de la computación

 ¿Qué es un árbol?
Es una estructura jerárquica formada por nodos conectados entre sí. Se parece a un arbol real!

           A
       / \
      B   C
     / \
    D   E

    📦 Conceptos básicos que debes dominar
✔ Nodo

Cada elemento del árbol.

✔ Nodo raíz (Root)

Es el primer nodo del árbol.

👉 En el ejemplo sería A.

✔ Nodo padre

Nodo que tiene hijos.

✔ Nodo hijo

Nodo que depende de otro.

✔ Nodo hoja

Nodo que no tiene hijos.

👉 D, E y C serían hojas.

⭐ Tipo más importante: Árbol Binario

Es el más usado y el que debes dominar primero.

👉 Cada nodo puede tener máximo 2 hijos:

Hijo izquierdo

Hijo derecho

        10
       /  \
      5    20
     / \     \
    3   7     30

"""

#Creación de la clase NODO
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

#Crear el árbol manualmente
raiz = Nodo(10)

raiz.izquierda = Nodo(5)
raiz.derecha = Nodo(20)

raiz.izquierda.izquierda = Nodo(3)
raiz.izquierda.derecha = Nodo(7)

raiz.derecha.derecha = Nodo(30)

"""Recorridos de árboles (Muy importantes)"""

#Inorden (Izquierda -> raíz -> derecha)
def inorden(nodo):
    if nodo:
        inorden(nodo.izquierda)
        print(nodo.valor)
        inorden(nodo.derecha)

#Preorden (Raíz -> Izquierda -> Derecha)
def preorden(nodo):
    if nodo:
        print(nodo.valor)
        preorden(nodo.izquierda)
        preorden(nodo.derecha)

#Postirden (Izquiuerda -> Derecha -> Raíz)
def postorden(nodo):
    if nodo:
        postorden(nodo.izquierda)
        postorden(nodo.derecha)
        print(nodo.valor)

#Probando los recorridos
print("Inorden:")
inorden(raiz)

print("Preorden:")
preorden(raiz)

print("Postorden:")
postorden(raiz)
