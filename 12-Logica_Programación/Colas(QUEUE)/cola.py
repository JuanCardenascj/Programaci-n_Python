"""La cola o las colas funcionan como una fila en un banco:
   
   1. Primero en entrar
   2. Primero en salir
A esto se le llama FIFO (First In First Out)

  Ejemplos reales:
  1. Turnos
  2. Procesos del sistemas
  3. Peticiones a servidores
  
  Operaciones Principales
  1.Enqueue -> Agrega
  2.Dequeue -> Eliminar primero"""

#Colas
from collections import deque

cola = deque()

cola.append("Cliente 1")
cola.append("Cliente 2")
cola.append("Cliente 3")
cola.append("Cliente 4")
cola.append("Cliente 5")

#Imprime el primer cliente 1
print(cola.popleft())