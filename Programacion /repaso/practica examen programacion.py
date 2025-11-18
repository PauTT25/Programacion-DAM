import pickle

class CLiente():
    def __init__(self,nombre,apellidos,email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        
print("#####  Gestion de clientes v0.1  #####")
print("#####    Pau Contreras Romero    #####")

clientes = []

try:   ####Cuidado con que el archivo no exista####
    archivo = open("clientes.bin","rb")
    clientes = pickle.load(archivo)
    archivo.close()
except:
    print("No existe archivo de datos")

while True:

    archivo = open("clientes.bin","wb")
    pickle.dump(clientes,archivo)
    archivo.close()
    
    print("Escoge una opcion:")
    print("1.-Insertar un cliente")
    print("2.-Listar clientes")
    print("3.-Actualizar un cliente")
    print("4.-Eliminar un cliente")
    opcion = int(input("Escoge una opcion:"))
    
    if opcion == 1:
       
        nombre = input("Introduce el nombre:")
        apellidos = input("Introduce los apellidos:")
        email = input("Introduce el email:")
        
        clientes.append(CLiente(nombre,apellidos,email))
        
    elif opcion == 2:
        identificador = 0
        for cliente in clientes:
            print("Este es el cliente con ID:",identificador)
            print(cliente.nombre,cliente.apellidos,cliente.email)
            identificador += 1
   
    elif opcion == 3:
        identificador = int(input("Introduce el ID para modificar:"))
        nombre = input("Introduce el nombre nuevo:")
        apellidos = input("Introduce los apellidos nuevos:")
        email = input("Introduce el email nuevo:")
        clientes[identificador].nombre = nombre
        clientes[identificador].apellidos = apellidos
        clientes[identificador].email = email
        
    elif opcion == 4:
        identificador = int(input("Introduce el id para eliminar:"))
        confirmacion = input("¿Estas seguro? (S/N): ").lower()
        
        if confirmacion == "s":
            clientes.pop(identificador)    #####El pop elimina un elemento de la lista, no es recomendable utilizarlo.
        elif confirmacion == "n":
            print("Cancelado")
        else:
            print("Opcion no valida")
    archivo = open("clientes.bin","wb")
    pickle.dump(clientes,archivo)
    archivo.close
            
        
