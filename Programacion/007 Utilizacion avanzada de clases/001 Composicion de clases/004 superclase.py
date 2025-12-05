class Persona():
  def __init__(self,nombre,apellidos,email,direccion):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
    self.direccion = direccion
  def dameDatos(self):
    return self.nombre+self.apellidos

class Profesor(Persona):
  def __init__(self,nombre,apellidos,email,direccion):
  	super().__init__(nombre, apellidos, email,direccion)			#Cuando utilizemos super en python tenemos que indicarle que queremos que nos traiga en la clase, si nos nos 
  
class Alumno(Persona):
  def __init__(self,nombre,apellidos,email,direccion):
    super().__init__(nombre, apellidos, email,direccion)

 
alumno1 = Alumno("Pau","Contreras","pau@gmail.com","calle de Pau")
print(alumno1.dameDatos())

profesor1 = Profesor("Juan","Garcia","juan@jocarsa.com","calle de Juan")
print(profesor1.dameDatos())
