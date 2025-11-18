class CLiente():
    def __init__(self):
        self.nombre = ""
        self.apellidos = ""
        self.email = ""
        
#Se definen setters y getters

    def setNombre(self,nuevonombre):
        self.nombre = nuevonombre
    
    def getNombre(self):
        return self.nombre
        
    
    def mostrar_cliente(self):
        print(self.getNombre)
        print(self.apellidos)
        print(self.email)
        
#Empezamos a describir los diferentes parametros

cliente1 = cliente("abel","dago iglesias","abel@gmail.com")
cliente2 = cliente("paco","rodriguez gil","paco@gmail.com")
cliente3 = cliente("alberto","sanz tora","alberto@gmail.com")

print = (cliente1.nombre)
print = (cliente1.apellidos)
print = (cliente1.email)
