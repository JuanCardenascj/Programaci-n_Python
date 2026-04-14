nombre = "David" #Variable global

def imprimir_nombre():
    print(f"Hola como estás {nombre}") #Llama la variable goblal
imprimir_nombre()

#Primero imprime la variable local creada con nombre y luego la variable global
def imprimir_nombre2():
    nombre = "Carlos"
    print(f"Hola como estás {nombre}")
imprimir_nombre2()
print(f"El valor de mi variable global es {nombre}")

#Cambia el valor de la variable global
def imprimir_nombre3():
    global nombre
    nombre = "Jesus"
    print(f"Hola como estas {nombre}")
imprimir_nombre3()
print(f"El valor de mi variable global es {nombre}")


"""Para uso de la variable localmente"""
def imprimir_nombre4():
    local = "Juan"
    print(f"Hola {local} como estas?")
imprimir_nombre4()