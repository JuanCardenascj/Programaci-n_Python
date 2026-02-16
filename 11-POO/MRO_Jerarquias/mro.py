"""Orden de Jerarquias!
1. Imprime D : Porque es la base B Y C
2. Imprime B : Porque la primer clase que heredo es A
3. Imprime C : Porque la segunda clase que heredo A
4. Imprime A : Porque no encuentra mas que heredar e Imprime A"""

class A:
    def hablar(self):
        print("hola desde A")

class B(A):
    def hablar(self):
        print("hola desde B")

class C(A):
    def hablar(self):
        print("hola desde C")

class D(B,C):
    def hablar(self):
        print("hola desde D")

#Crea el objeto
d = D()
d.hablar() #Llama para imprimirlo


"""Orden Nuevamente de Jerarquias
1. Imprime D: Porque imprime el método hablar
2. Imprime B: Porque es el primero en heredar
3. Imprime A: Porque sube directo a (A)
4. Imprime C: Porque baja a buscar donde se encuentre el método nuevamente
5. Imprime E: Porque no lo encuentra en las demás jerarquias"""

class A:
    def hablar(self):
        print("hola desde A")

class E:
    def hablar(self):
        print("hola desde E")

class B(A):
    def hablar(self):
        print("hola desde B")

class C(E):
    def hablar(self):
        print("hola desde C")

class D(B,C):
    def hablar(self):
        print("hola desde D")

#Crea el objeto
d = D()
d.hablar() #Llama para imprimirlo