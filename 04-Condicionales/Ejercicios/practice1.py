#Qué imprimirá?
edad = 17

if edad >= 18:
    print("Adulto")
else:
    print("Menor")

#Ahora que sea pidiendole datos al usuario
print("Bievenido...............!")
edad1 = int(input("Por favor Digite su edad .... "))

if edad1 >= 18 and edad1 <= 30:
    print("Usted es un adulto joven")
else:
    print("Usted es un adulto")


#Ahora pidiendo datos al usuario, pero con anidadas
print("Bievenidido por segunda vez.......!")
edad2 = int(input("Por favor digite su edad ..... "))

if edad2 >= 18:
    if edad2 >= 25 and edad2 <= 30:
        print("Usted es un adulto joven")
    else:
        print("Usted es un adulto!")

#Otra anidada con datos al usuario
print("hola...! ")
nombre1 = (input("Por favor digite su nombre .... "))
if nombre1 == "Juan David":
    if nombre1 == "Juancho":
        print("Hola Juan Cárdenas ¿Como estas?")
    else:
        print("Eres tu Juan david? ")