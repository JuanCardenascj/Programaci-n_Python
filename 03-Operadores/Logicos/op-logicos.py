"""Operadores Lógicos"""

#AND - Ambas tiene que ser True de lo contrario siempre devolvera False
Resultado1 = True & True #Devuelve verdadero
Resultado2 = False & True #Devuelve falso
Resultado3 = True & False #Devuelve falso
Resultado4 = False & False #Devuelve falso

#OR - Solo una debe ser True para de verdadero, para ser False ambas deben ser falsas
Resultado5 = True & True #Devuelve verdadero 
Resultado6 = False & True #Devuelve verdadero
Resultado7 = True & False #Devuelve verdadero
Resultado8 = False & False #Devuelve falso

#NOT - Invierte el valor que está
Resultado9 = not True #Devuelve falso
Resultado10 = not False #Devuelve verdadero

print(Resultado1)