#Crea un programa que solicite una nota entre 0 y 5 y muestra.
nota = float(input("Ingrese una nota entre 0 y 5: "))

if nota >= 4.5:
    print("Excelente")
elif nota >= 3 and nota < 4.5:
    print("Aprobado")
elif nota < 3:
    print("Reprobado")
else:
    print("Nota inválida, por favor ingrese un valor entre 0 y 5.")