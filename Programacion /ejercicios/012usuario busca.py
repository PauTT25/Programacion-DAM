archivo = open ("mapa.txt","r") #READ
busca = input("Introduce el termino a buscar:")

lineas = archivo.readlines()

for linea in lineas:
    if busca in linea:
        print("Encontrado!:",linea)
