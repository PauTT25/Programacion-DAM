import pickle
catalogo = []

while True:
    print("Selecciona una opcion:")
    print("1.- Inserta unas zapatillas")
    print("2.- Leer las zapatillas")
    print("3.- Actualizar las zapatillas")
    print("4.- Eliminar unas zapatillas")
    print("5.- Salir")
    opcion = int (input("Elige una opcion:"))
    
    if opcion == 1:
        # Insertar
        zapatillas = input("Dime tu calzado:")
        color = input("Dime el color de tu calzado:")
        talla = input("Dime tu talla:")
        #Añado a la agenda
        catalogo.append([zapatillas,color,talla])
        
    elif opcion == 2:
        # Imprimir
        if 
        print(catologo)
        
    elif opcion == 3:
        # Guardar
        archivo = open("agenda.bin", "wb")
        pickle.dump(agenda,archivo)
        archivo.close()
