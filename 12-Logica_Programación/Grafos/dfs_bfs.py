"""  DFS Es una PILA (STACK)- tiene una mentalidad así:

     #Voy a seguir un camino hasta el final antes de probar otro

     # Es como alguien explorando un laberinto que siempre gira por el primer pasillo hasta encontrar una pared.!
 

       A → B → D → (no hay más)
                    ← retrocede
                    → E → (no hay más)
        ← retrocede
        → C → F

        A B D E C F

    # DFS se usa una idea muy importante, retroceder cuando no hay más caminos.

    BFS Es una Cola (QUEUE) - Primero explora todo lo que esté cerca, es como ondas expandiéndose en agua.

    Nivel 1 → A
    Nivel 2 → B C
    Nivel 3 → D E F

    A B C D E F

Lo primero en entrar es lo primero en salir!

"""

#Usar DFS cuando: 1. Quieres explotar todo 2. Dectectar ciclos 3. Backtracking 4. Laberintos 5. Arboles 6. Validaciones profundas - Aventurero

#Usar BFS cuando: 1. Ruta más corta 2. Navegación 3. Sistemas de recomendación 4. Problemas por niveles 5. Distancias mínimas - Organizado