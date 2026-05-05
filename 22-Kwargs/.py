#Permite pasar a las funciones un numero indeterminado de argumentos
def conectar_bd(**kwargs): #Se utiliza los dos asteriscos.!

    nombre = kwargs.get('nombre_db', 'default')
    user = kwargs['usuario']
    password = kwargs['password']
    port = kwargs['password']
    dir_bd = kwargs['dir_bd']
    print(f"Conectando con la base de datos: {nombre}")
    print(f"login with: {user} - {password}")

conectar_bd(nombre_bd='generico', 
            usuario='root', 
            password='1234', 
            port=5002,
            dir_bd = '10.54.47.20') #Se convierte en un diccionario!