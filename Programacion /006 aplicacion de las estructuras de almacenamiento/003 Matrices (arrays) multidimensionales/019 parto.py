import pickle
agenda = []

while True:
    # Insertar
    nombre = input("Dime tu nombre:")
    apellidos = input("Dime tu apellido:")
    email = input("Dime tu email:")
    telefono = input("Dime tu telefono:")
    
    #Añado a la agenda
    agenda.append([nombre,apellidos,email,telefono])
    # Imprimir
    print(agenda)
    # Guardar
    archivo = open("agenda.bin", "wb")
    pickle.dump(agenda,archivo)
    archivo.close()
