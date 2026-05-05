#Qué imprimirá?
nota = 3.2

if nota >= 4:
    print("Excelente")
elif nota >= 3:
    print("Aprobado")
else:
    print("Reprobado")

#Ahora pidiendole datos al usuario
print("Bienvenido a la calidad evaluativa de su resultado final.!")
nota1 = float(input("Por favor digite su nota final o definitiva:   "))

if nota1 == 5:
    print("Excelente, continua así!")
elif nota1 >= 4 and nota1 <= 4.9:
    print("Muy bien eres un estudiante promedio, continua así para mejorar!")
elif nota1 >= 3 and nota1 <= 3.9:
    print("Felicidades, pasaste con una nota minima pero podemos mejorar...!")
elif nota1 >= 2 and nota1 <= 2.9:
    print("Bien, pero debe seguir intentando para obtener una mayor nota, sino te recuperas podrias llegar afectar tu rendimiento")
elif nota1 >= 1 and nota1 <= 1.9:
    print("Debes estudiar mas para mejorar...!")
elif nota1 == 0:
    print("Me esperaba una mejor nota de ti, debe seguir estudiando para lograr mejores notas.!!")
else:
    print("El número digitado no es una nota valida..!")