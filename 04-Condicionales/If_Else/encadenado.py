edad = 80

#IF ---> Encadenado
if edad  >= 0 and edad <= 12:
    print('Usted es un niño')
elif edad >= 13 and edad <= 17:
    print('Usted es un adolecente')
elif edad >= 18 and edad <= 59:
    print('Usted es un adulto')
elif edad >= 60 and edad <= 100:
    print('Usted ya es un adulto mayor')
else:
    print('Usted a digitado un número invalido...!')

edad2 = int(input("Por favor, ingrese su edad: "))

if edad2 >= 0  and edad2 <= 12:
    print('Usted es un niño')
elif edad2 >= 13 and edad2 <= 17:
    print('Usted es un adolecente')
elif edad2 >= 18 and edad2 <= 59:
    print('Usted es un adulto')
elif edad2 >= 60 and edad2 <= 100:
    print('Usted ya es un adulto mayor')
else:
    print('Usted a digitado un número invalido...!')