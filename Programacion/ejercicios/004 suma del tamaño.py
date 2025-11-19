import os

carpeta = input("Indica una carpeta:")

elementos = os.listdir(carpeta)

suma = 0

for elemento in elementos:
    ruta = os.path.join(carpeta, elemento)
    suma += os.path.getsize(ruta)
  
    print("La carpeta ocupa:")
    print(os.path.getsize(ruta)/1024*1024,"MB")
    print(os.path.getmtime(ruta),"segundos")
