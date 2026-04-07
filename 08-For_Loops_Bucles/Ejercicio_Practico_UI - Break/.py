import random
import turtle

#Caracteristicas o definiciones de la ventana
ventana = turtle.Screen() #Para crear la ventana y guardarla dentro de la variable
ventana.title("Carrera de caracoles") #Para el titulo
ventana.bgcolor('lightblue') #Para el color de fondo
ventana.setup(width=800,height=600) #Para el ancho y largo de la ventana

#Creando los dos caracoles
caracol1 = turtle.Turtle()
caracol1.shape("turtle")
caracol1.color("black")
caracol1.penup()
caracol1.goto(-300,100)

caracol2 = turtle.Turtle()
caracol2.shape("turtle")
caracol2.color("red")
caracol2.penup()
caracol2.goto(-300,0)

meta = 300

while True:
    avance_caracol_1 = random.randint(1,20)
    avance_caracol_2 = random.randint(1,20)

    caracol1.forward(avance_caracol_1)
    caracol2.forward(avance_caracol_2)

    print(f"El caracol 1 avanza {avance_caracol_1}, para un total de: {caracol1.xcor()}")
    print(f"El caracol 2 avanza {avance_caracol_2}, para un total de: {caracol2.xcor()}")
    print("----------------------------------------------------")

    if caracol1.xcor() >= meta or caracol2.xcor() >= meta:
        break

if caracol1.xcor() > caracol2.xcor():
    print("El caracol 1 ha ganado")
elif caracol2.xcor() > caracol1.xcor():
    print("El caracol 2 ha ganado")
else:
    print("Esto es un empate")

ventana.exitonclick() #Para que se cierre dandole click