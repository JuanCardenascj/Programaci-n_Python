#Desarrollar un Script que pida la edad y la altura del usuario
#Si la persona es mayor de edad puede participar
#Pero la persona debe medir mas de 170cm
#Si la persona no mide 170cm podra participar si es mayor a 25 años
#Y si la altura es mayor a 165

print('Bienvenido...............!')
edad = int(input("Digite su edad ... ")) #Realiza casteo para convertir
altura = int(input("Digite su altura .. ")) #Realizar casteo para convertir

if edad >= 18: #Al no cumplir con la edad, no entra en la anidación, si la cumple si ingresa..!
    if altura >= 170 or edad >= 25 and altura >= 165:
        print('Puedes Participar en el equipo de Baloncesto')
    else:
        print('No cumples con los requisitos para el equipo de baloncestos!')
else:
    print('Debe ser mayor de edad para participar en el equipo de Baloncesto..!')