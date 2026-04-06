"""Import --> Importa librerias creadas por otras personas"""

import turtle #Apoya mucho en interfaz grafíca

ventana = turtle.Screen() #Crea una ventana y la guarda en la variable
ventana.bgcolor("white") #Cambia el color a blanco

#Crea una tortuga o el objeto tortuga
tortuga = turtle.Turtle()
tortuga.speed(10) #Velocidad del movimiento

#Dibujar una estrella con la tortuga..!
for _ in range(5):
    tortuga.forward(250)
    tortuga.right(144)
ventana.exitonclick()