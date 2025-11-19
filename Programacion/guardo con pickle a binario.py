import pickle


class Cliente():
    def __init__(self,nuevonombre,nuevoemail):
        self.nombre = nuevonombre
        self.email = nuevoemail
        
clientes = []

clientes.append(Cliente("Pau Contreras","info@jocarsa.com")
clientes.append(Cliente("Juan","juan@gamil.com")

archivo = open("clientes.bin","wb")
pickle.dump(clientes,archivo)
archivo.close()
