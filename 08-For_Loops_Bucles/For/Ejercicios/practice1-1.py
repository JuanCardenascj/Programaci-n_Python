"""Import --> Importa librerias creadas por otras personas"""

import turtle #Apoya mucho en interfaz grafíca

ventana = turtle.Screen() #Crea una ventana y la guarda en la variable
ventana.bgcolor("white") #Cambia el color a blanco

#Crea una tortuga o el objeto tortuga
tortuga = turtle.Turtle()
tortuga.speed(4) #Velocidad del movimiento

#Dibujar un cuadrado con la tortuga..!
for _ in range(1):
    tortuga.forward(300)
    tortuga.right(90)
    tortuga.forward(300)
    tortuga.right(90)
    tortuga.forward(300)
    tortuga.right(90)
    tortuga.forward(300)
    tortuga.right(30)
    tortuga.forward(300)
    tortuga.right(120)
    tortuga.forward(300)
    tortuga.left(60)
    tortuga.forward(300)
    tortuga.left(90)
    tortuga.forward(260)
    tortuga.left(90)
    tortuga.forward(460)
ventana.exitonclick()