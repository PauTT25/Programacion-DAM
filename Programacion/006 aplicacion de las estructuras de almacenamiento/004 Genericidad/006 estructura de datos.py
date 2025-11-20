numeros = [1,2,"3",4,"cinco"]

print(numeros)
numeros = ["cero","uno","dos","tres","cuatro","cinco"]
def calculaDoble():
  for numero in numeros:
    try:                     #primero intenta convertir   
      numero = int(numero)   # Convierto en entero
      print(numero*2)
    except:                  #si no puedes
      print("(no válido)")

calculaDoble()
