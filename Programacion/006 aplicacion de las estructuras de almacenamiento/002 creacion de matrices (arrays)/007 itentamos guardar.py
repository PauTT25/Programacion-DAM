menu = []

while True:
    #Empezamos a escribir las opciones para el programa
    print("Opciones:")
    print("1.- Introduce nueva comida en el menu")
    print("2.- Listar comidas en el menu:")
    print("3.- Guardar en archivo")
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
            
    #Por ultimo en esta opcion le decimos que guarde la lista de la comida en el archivo
    elif opcion == 3:
        archivo = open("datos.txt","w")
        archivo.write(menu)
        archivo.close()
