#Ahora escribe el ultimo ejercicio pero en codigo
"""Diferncia importante con la funcionaria INT: Porque al tener int antes del input, convierte a entero.!
    
    1. int("3")
    2. int("   3   ")
    3. int("-5")

"""
nota = int(input("Digite una nota entre (0, 5): "))

if nota < 0 or nota > 5:
    print("Nota inválida")
elif nota >= 3:
    print("Aprobado")
else:
    print("Reprobado")

#ValueError es lo que arroja cuando el programa explota.!