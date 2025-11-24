#Importo la libreria Flask para poder crear webs
from flask import Flask, request				#Tomo parametros de la URL

#Creo una nueva aplicacion
app = Flask(__name__)

#Escucho en la ruta raiz
@app.route("/")
def inicio():
	nombre = request.args.get("nombre")
	print(nombre)
    #Y renderizo una plantilla llamada index.html
	return "Mira en la consola si ha pasado algo"
    
#Si este archivo no es una libreria y es el archivo principal
if __name__ == "__main__":
    #Pon en marcha la aplicacion
    app.run(debug=True)

# http://127.0.0.1:5000/?nombre=Pau%20Contreras
# %20 = espacio (en las url)
