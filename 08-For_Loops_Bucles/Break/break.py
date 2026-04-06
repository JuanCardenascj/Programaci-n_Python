import random

meta = 20

caracol1 = 0
caracol2 = 0

while caracol1 < 20 and caracol2 < 20:
    avance_caracol_1 =  random.randint(1,4)
    avance_caracol_2 =  random.randint(1,4)

    caracol1 += avance_caracol_1
    caracol2 += avance_caracol_2

    print(f"Caracol 1 avanza {avance_caracol_1}, para un total de: {caracol1}")
    print(f"Caracol 2 avanza {avance_caracol_2}, para un total de: {caracol2}")
    print(".........................................")

if caracol1 > caracol2:
    print("El caracol 1 ha ganado")
elif caracol2 > caracol1:
    print("El caracol 2 ha ganado")
else:
    print("Ambos caracoles han avanzado la misma distancia. Tenemos un EMPATE!")