import pickle

menu = []

while True:
    #Empezamos a escribir las opciones para el programa
    print("Opciones:")
    print("1.- Introduce nueva comida en el menu")
    print("2.- Listar comidas en el menu:")
    print("3.- Guardar en archivo")
    print("4.- Cargar lista")
    opcion = int(input("Selecciona una opcion:"))
    
    #Aqui describimos la primera opcion, añadir la comida
    if opcion == 1:
        comida = input("Introduce el nombre de la comida:")
        menu.append(comida)
    
    #En la segunda opcion le decimos que nos diga la comida que tenemos en lista
    elif opcion == 2:
        print("Tu comida hasta el momento es:")
        for elemento in menu:
            print(elemento)
            
    #En esta opcion le decimos que guarde la lista de la comida en el archivo
    elif opcion == 3:
        archivo = open("datos.bin","wb")        #WB signifa que lo escriba en binario (write binary)
        pickle.dump(menu,archivo)
        archivo.close()
        print("La lista se ha guardado correctamente👌.")
    
    #Por ultimo con esta opcion le pedimos que nos cargue la lista guardada dentro de pickle
    elif opcion == 4:
        archivo = open ("datos.bin", "rb")
        menu = pickle.load(archivo)             #Volcamos el archivo a la lista 
        archivo.close()
        print("La lista ha sido cargada correctamente👌.")
