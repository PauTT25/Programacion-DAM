numeros = [1,2,"3",4,"patata"]

print(numeros)
numeros_etiquetas = ["cero","uno","dos","tres","cuatro","cinco"]

def calculaDoble():
    for numero in numeros:
      try:                          #primero intenta convertir
        numero = int(numero)        #convierto en entero
        print(numero*2)
      except:                       #si no puedes
        centinela = False
            #intenta buscar el valor en la lista de numeros
        for i in range(0,len(numeros_etiquetas)):
            if numero == numeros_etiquetas[i]:
                print(i*2)
                centinela = True
        if centinela == False:
                print("Mira tio lo he intentado pero no he podido")

calculaDoble()
