"""Que es un GRAFO: es una estructura formada por:
    1. Nodos (tambien son llamados vértices)
    2. Conexiones entre nodos (aristas)
    
    Ejemplo:
    
    A ----- B
    |       |
    |       |
    C ----- D

    Es utilizado en:
    1. Redes sociales
    2. Google Maps
    3. Rutas de transporte
    4. Internet
    5. Juegos
    6. Sistemas de recomenndación

Un grafo es una estructura de datos que sirve para representar relaciones entre cosas.

Un grafo tiene solo dos elementos:

Nodos (o vértices)

Solo los elementos principales.

Ejemplos:
  1. Personas
  2. Ciudades
  3. Usuarios
  4. Vehículos
  5. Puntos de recolección


Aristas (o conexiones)

Son las relaciones entre los nodos.

Ejemplos:
   1. Amistad entre personas
   2. Carreteras entre ciudades
   3. Relación usuario -> Solicitud
   4. Ruta vehículo -> Barrio
"""

#Crear un grafo con diccionario
grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

#Forma1: Lista de Adyacencia - Se presenta con diccionarios.

grafo2 = {
    "Juan": ["Maria"],
    "Maria": ["Juan","Pedro"],
    "Pedro": ["Maria", "Ana"],
    "Ana": ["Pedro"]
} #Cada nodo apunta a sus conexiones


grafo3 = {
    "Casa": ["Tienda", "Colegio"],
    "Tienda": ["Casa", "Hospital"],
    "Colegio": ["Casa", "Hospital"],
    "Hospital": ["Tienda", "Colegio"]
}

"""Operaciones Importantes en los Grafos

Cuando se trabaja con los grafos normalmente haces:
   
   1. Recorrerlos
   2. Buscar rutas
   3. Encontrar caminos más cortos
   4. Detectar ciclos
   5. Encontrar conexiones

Tipos de Grafos!
1. Grafo no Dirigio - Las conexiones o aristas van en ambos sentidos

 Ejemplo: 

  casa -> tienda
  tienda -> casa

2. Grafo Dirigido - Las conexiones tienen dirección

  Ejemplo: 

  Casa -> Tienda

3. Grafo Ponderado - Las conexiones tienen peso.

  Ejemplo: 

  Casa -> Tienda (5 minutos)
  Casa -> Colegio (10 minutos)
"""

