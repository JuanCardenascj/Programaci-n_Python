class Lista:
    def __init__(self, lista):
        self.__lista = lista

    def anexar_dato(self, n):
        self.__lista.append(n)

    def anexar_dato_posicion(self, pos, n):
        self.__lista.insert(pos, n)

    def imprimir_lista(self):
        print(self.__lista)

    def borrar_elemento_posicion(self, n):
        lista.remove(n)

    def borrar_elemento(self):
        lista.pop()

    def imprimir_elemento_ultima_posicion(self):
        print(self.__lista[-1])

    def origen_ascendente(self):
        lista.sort()

    def orden_descendente(self):
        lista.sort(reverse = True)

#Definición de 2 listas
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

#Creación del Objeto
unaLista = Lista(lista)
print("Lista creada")
unaLista.imprimir_lista

opcion = 0
while(opcion != 9):
    n = 0
    posicion = 0
    print("\n\t\t Menú Principal")
    print("n\t1. Anexar elementos al final de la listar")
    print("\t2. Imprimir lista")
    print("\t3. Anexa elemento en una posicioón")
    print("\t4. Borrar último elemento de la lista")
    print("\t5. Borrar el elemento de la lista")
    print("\t6. Imprimir el elemento de la ultima posición")
    print("\t7. Ordenar de forma ascendete")
    print("\t8. Ordenar de formadesecente")
    print("\t9. Salir")

opcion = int(input("\n Digite la opción selecionda: "))
if opcion == 1:
    n = int(input("Digite un numero: "))
    unaLista.anexa_dato(n)
    unaLista.imprimir_lista()
elif opcion == 2:
    unaLista.imprimir_lista()
elif opcion == 3:
    posicion = int(input("Digite posicion donde necesita anexar el elemento: "))
    n = int(input("Digite un número: "))
    unaLista.anexar_dato_posicion(posicion,n)
    unaLista.imprimir_lista()
elif opcion == 4:
    unaLista.borrar_elemento()
    unaLista.imprimir_lista()
elif opcion == 5:
    posicon = int(input("Digite el elemento a borrar: "))
    unaLista.borrar_elemento_posicion(posicion)
    unaLista.imprimir_lista()
elif opcion == 6:
    unaLista.imprimir_elemento_ultima_posicion()
elif opcion == 7:
    unaLista.origen_ascendente()
    unaLista.imprimir_lista()
elif opcion == 8:
    unaLista.orden_descendente()
    unaLista.imprimir_lista()
else:
    print("Información Incorrecta")