"""Haz un programa que encuentre el segundo numero menor, de una lista!"""

list1 = [-980, -990, 990, 980, 321, 443, 654, 0 , 2, 3, 4, 5, 6, 7, 8, 9]

menor = float('inf')
segundo_menor = float('inf')

for numero in list1:
    if numero < menor:
        segundo_menor = menor
        menor = numero
    elif numero < segundo_menor and numero != menor:
        segundo_menor = numero

print("El segundo menor es:", segundo_menor)
