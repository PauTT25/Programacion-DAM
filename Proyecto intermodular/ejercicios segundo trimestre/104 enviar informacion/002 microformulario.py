#Importo la libreria Flask para poder crear webs
from flask import Flask, render_template, request				#Tomo parametros de la URL

#Creo una nueva aplicacion
app = Flask(__name__)

@app.route("/")
def inicio():
	return render_template("index.html")

#Escucho en la ruta raiz
@app.route("/envio")
def envio():
	nombre = request.args.get("nombre")
	apellidos = request.args.get("apellidos")
	print(nombre,apellidos)
    #Y renderizo una plantilla llamada index.html
	return "- Nombre: "+nombre+" - Apellidos: "+apellidos
    
#Si este archivo no es una libreria y es el archivo principal
if __name__ == "__main__":
    #Pon en marcha la aplicacion
    app.run(debug=True)

# http://127.0.0.1:5000/?nombre=Pau%20Contreras
# %20 = espacio (en las url)
