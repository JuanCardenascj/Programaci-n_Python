"""WHILE SE EJECUTA DE FORMA INFINITA -  Se va a ejecutar siempre que una condición sea real, osea son infinitos 

Ejemplo:
    num = 1
     while num < 5:
         print(num)
          num +=1 
          
Se va a ejecutar mientras que el numero sea menor a 5
Primera vuelta = 1
Segunda vuelta = 2
Tercera vuelta = 3
Cuarta vuelta = 4
Quinta vuelta se detiene!"""

contador = 0

#Mientras que la condición se cumpla el bucle se va a ejecutar (La condición se verifica vuelta tras vuelta)
while contador <  10: #Cuando llega al 10 se detiene el contador
    print(contador)
    contador += 1 #Se va mostrar de 0 a 9
print("El while llego a su fin!")

while contador <  10: #Cuando llega al 10 se detiene el contador
    contador += 1 #Se va mostrar de 1 a 10
    print(contador)
print("El while llego a su fin!")
