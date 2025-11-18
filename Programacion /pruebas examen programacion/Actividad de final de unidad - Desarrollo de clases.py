'''
Para hacer este ejercicio tenemos que empezar creando la clase que nos piden con sus respectivos atributos, para seguir avanzando en el ejercicio tenemos que incluir metodos get y set los cuales nos permiten modificar los atributos para comprobar que los metodos funcionan correctamente.
'''

class Cliente():
    def __init__(self, nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        
#Se definen setters y getters

    def setNombre(self, nuevonombre):
        self.nombre = nuevonombre
    
    def getNombre(self):
        return self.nombre
        
    def setApellidos(self, nuevosapellidos):
        self.apellidos = nuevosapellidos

    def getApellidos(self):
        return self.apellidos
        
    def setEmail(self, nuevoemail):
        self.email = nuevoemail

    def getEmail(self):
        return self.email
        
    
    def mostrar_cliente(self):
        print(self.getNombre())
        print(self.apellidos())
        print(self.email())
        
#Empezamos a describir los diferentes parametros

cliente1 = Cliente("abel","dago iglesias","abel@gmail.com")
cliente2 = Cliente("paco","rodriguez gil","paco@gmail.com")
cliente3 = Cliente("alberto","sanz tora","alberto@gmail.com")

#Le decimos que nos imprima las instancias creadas con sus respectivas propiedades
print (cliente1.nombre)
print (cliente1.apellidos)
print (cliente1.email)

print (cliente2.nombre)
print (cliente2.apellidos)
print (cliente2.email)

print (cliente3.nombre)
print (cliente3.apellidos)
print (cliente3.email)


#Modificamos los datos usando los setters para comprobar que funciona
cliente1.setNombre("abel nuevo")
cliente2.setApellidos("rodriguez nuevo")
cliente3.setEmail("nuevo_correo@gmail.com")

#Mostramos los datos modificados con los getters
print("Datos modificados")
print(cliente1.getNombre())
print(cliente2.getApellidos())
print(cliente3.getEmail())

'''
CONCLUSION
La utilizacion de clases, constructores y metodos es muy eficiente a la hora de trabajar con objetos, ya que con su uso podemos definir claramente la estructura que nos piden. Los setters y los getters nos ayudan a manejar los datos de una manera ordenada y estructurada ya que los getters recuperan los datos y los setters nos ayudan a la hora de modificar correctamente cada atributo.
'''
