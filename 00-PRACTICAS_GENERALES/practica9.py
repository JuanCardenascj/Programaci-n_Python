"""Encuentra el tercer número menor"""

list1 = [-980, -990, 990, 980, 321, 443, 654, 0 , 2, 3, 4, 5, 6, 7, 8, 9]

menor = float('inf')
segundo_menor = float('inf')
tercer_menor = float('inf')

for numero in list1:
    
    if numero < menor:
        tercer_menor = segundo_menor
        segundo_menor = menor
        menor = numero

    elif numero < segundo_menor and numero != menor:
        tercer_menor = segundo_menor
        segundo_menor = numero

    elif numero < tercer_menor and numero != segundo_menor and numero != menor:
        tercer_menor = numero

print("Tercer menor:", tercer_menor)
