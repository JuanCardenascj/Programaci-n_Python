"""Crea una función que:

1.  Reciba una lista de números
2.  Devuelva la lista con todos los números multiplicados por 2
"""

def duplicar_lista(numeros):
    multiplicados = []
    for numero in numeros:
        multiplicados.append(numero * 2)
    return multiplicados

print(duplicar_lista([22, 21, 33]))  # [2, 4, 6] 

#Prueba de una resta
def restar_lista(restar):
    resto = []
    for resta in restar:
        resto.append(resta - 2)
    return resto

print(restar_lista([432, 123, 123]))

#Prueba de una división 
def division_lista(divisions):
    division1 = []
    for division in divisions:
        division1.append(division / 2)
    return division1
print(division_lista([321, 32, 543, 123]))