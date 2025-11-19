menu = []

while True:
    print("Opciones:")
    print("1.- Introduce nueva comida en el menu")
    print("2.- Listar comidas en el menu:")
    opcion = int(input("Selecciona una opcion:")
    if opcion == 1:
        comida = input("Introduce el nombre de la comida:")
        menu.append(comida)
    elif opcion == 2:
    print("Tu comida hasta el momento es:")
    for elemento in menu:
        print(elemento)
