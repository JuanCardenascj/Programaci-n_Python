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
"""

#Crear un grafo con diccionario
grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}
