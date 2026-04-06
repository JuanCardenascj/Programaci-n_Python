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
    print('Usted a digitado un número invalido..!')