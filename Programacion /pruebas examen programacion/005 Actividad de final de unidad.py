'''
Este ejercicio nos ha pedido que creemos un CRUD utilizando la libreria pickle la cual nos permite guardar y recuperar objetos, empezamos definiendo la clase llamada cliente con las diferentes propiedades que nos ofrecen, con la ayuda de las listas creamos una vacia para añadir las propiedades que nos piden, finalmente el programa carga los clientes que hemos añadido en el archivo existente.
'''

import pickle 

class Cliente():
    def __init__(self, nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
    
# Insertamos una lista de clientes vacía
clientes = []

try:
    with open("clientes.pkl", "rb") as archivo:
        clientes = pickle.load(archivo)
        print("Ahora sí que hay clientes.")
except:
    clientes = []  # Si no hay archivo, la lista empieza vacía
    print("Aún no hay clientes.")
    
# Empezamos a hacer el bucle del menú
while True:
    print("--- MENU DE CLIENTES ---")
    print("1.- Crear cliente")
    print("2.- Listar clientes existentes")
    print("3.- Actualizar cliente")
    print("4.- Eliminar cliente")
    print("5.- Salir")

    opcion = int(input("Elige una opción: "))

# Crear nuevo cliente
    if opcion == 1:
        nombre = input("Nombre del cliente: ")
        apellidos = input("Apellidos del cliente: ")
        email = input("Email del cliente: ")

        nuevo_cliente = Cliente(nombre, apellidos, email)
        clientes.append(nuevo_cliente)

        with open("clientes.pkl", "wb") as archivo:
            pickle.dump(clientes, archivo)

        print("El cliente se ha guardado correctamente.")

# Listar clientes
    elif opcion == 2:
        if len(clientes) == 0:
            print("No hay clientes guardados.")
        else:
            print("--- LISTA DE CLIENTES ---")
            for i, cliente in enumerate(clientes):
                print(i, "-", cliente.nombre, cliente.apellidos, "-", cliente.email)

# Actualizar cliente
    elif opcion == 3:
        if len(clientes) == 0:
            print("No hay clientes para actualizar.")
        else:
            print("--- ACTUALIZAR CLIENTE ---")
            for i, cliente in enumerate(clientes):
                print(i, "-", cliente.nombre, cliente.apellidos, "-", cliente.email)

            identificador = int(input("Introduce el ID del cliente a modificar: "))

            if 0 <= identificador < len(clientes):
                nombre = input("Introduce el nuevo nombre: ")
                apellidos = input("Introduce los nuevos apellidos: ")
                email = input("Introduce el nuevo email: ")

                clientes[identificador].nombre = nombre
                clientes[identificador].apellidos = apellidos
                clientes[identificador].email = email

                with open("clientes.pkl", "wb") as archivo:
                    pickle.dump(clientes, archivo)

                print("Cliente actualizado correctamente.")
            else:
                print("Número no válido.")

# Eliminar cliente
    elif opcion == 4:
        if len(clientes) == 0:
            print("No hay clientes para eliminar.")
        else:
            print("--- ELIMINAR CLIENTE ---")
            for i, cliente in enumerate(clientes):
                print(i, "-", cliente.nombre, cliente.apellidos, "-", cliente.email)

            identificador = int(input("Introduce el ID del cliente a eliminar: "))

            if 0 <= identificador < len(clientes):
                clientes.pop(identificador)

                with open("clientes.pkl", "wb") as archivo:
                    pickle.dump(clientes, archivo)

                print("Cliente eliminado correctamente.")
            else:
                print("Número no válido.")

# Salir del programa
    elif opcion == 5:
        print("Saliendo")
        break

'''
CONCLUSION
El ejercicio nos ayuda a comprender como funcionan las clases y objetos,  como el manejo básico de listas, archivos y estructuras de control. Nos basamos en el ejemplo de crear un CRUD el cual es muy utilizado en el desarrollo de aplicaciones y bases de datos, mostrandonos cómo se pueden crear, leer, actualizar y eliminar registros de una forma sencillla.
'''



        
    
        
        

    
    
