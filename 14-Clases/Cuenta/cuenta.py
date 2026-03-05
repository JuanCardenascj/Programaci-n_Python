class Cuenta:

    def __init__(self, numero_cuenta, cliente, valor = 0):
        self.__numero_cuenta = numero_cuenta
        self.__cliente = cliente
        self.__saldo = valor

    #Getters (Métodos GET)
    def obtener_numero_cuenta(self):
        return self.__numero_cuenta
    def obtener_saldo(self):
        return self.__saldo
    
    #Métodos de la lógica del negocio
    def consignar(self, valor):
        self.__saldo += valor
    def retirar(self, valor):
        self.__saldo -= valor

class Cliente:

    def __init__(self, id, apellido, nombre):
        self._id = id
        self._apellido = apellido
        self._nombre = nombre

    #Getters (Métodos GET)
    @property
    def id(self):
        return self._id
    #Setters (Métodos SET)
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

#Crea el Objeto!
cliente1 = Cliente(1, "Hernadez", "Miguel")
cuenta1 = Cuenta(123456, cliente1, 0)
print("Numero cuenta: ", cuenta1.obtener_numero_cuenta())
print("Cliente: ", cliente1.nombre)
print("Saldo: ", cuenta1.obtener_saldo())
cuenta1.consignar
print("Saldo despues de consignar: ", cuenta1.obtener_saldo())