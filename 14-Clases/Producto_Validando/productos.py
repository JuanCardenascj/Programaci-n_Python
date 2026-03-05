class Producto:

    def __init__(self, id, nombre, descripcion, precio):
        self._id = id
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio = precio
    
    @property
    def id(self):
        return self._id
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
    def descripcion(self):
        return self._descripcion
    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion
    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self, precio):
        self._precio = precio

#Creamos el objeto de la clase Producto
producto = Producto(1, "Portatil", "Laptop Axus XPS Gamer", 1500.000)

#Imprimir los valores iniciales de los atributos
print(f"ID: {producto.id}")
print(f"Nombre: {producto.nombre}")
print(f"Descripcion: {producto.descripcion}")
print(f"Precio: {producto.precio}")

#Cambiar los valores de los atributos
producto.id = 2
producto.nombre = "Monitor"
producto.descripcion = "Monitor Fell 27 Inch"
producto.precio = 200.0

#Imprimir los valores actualizados de los atributos
print(f"ID: {producto.id}")
print(f"Nombre: {producto.nombre}")
print(f"Descripcion: {producto.descripcion}")
print(f"Precio: {producto.precio}")