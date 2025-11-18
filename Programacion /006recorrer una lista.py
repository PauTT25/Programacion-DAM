archivo = open ("basededatos.txt","r")

linea = archivo.readlines()
for linea in lineas:
  print(linea)
archivo.close()
