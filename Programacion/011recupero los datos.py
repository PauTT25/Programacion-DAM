import pickle

class Cliente():
    def __init__(self,nuevonombre,nuevoemail):
        self.nombre = nuevonombre
        self.email = nuevoemail
        
archivo = open("clientes.bin","wb")
Clientes = pickle.load(archivo)
archivo.close()

print(clientes)
