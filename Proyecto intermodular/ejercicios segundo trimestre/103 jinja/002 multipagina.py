#Importo la libreria Flask para poder crear webs
from flask import Flask, render_template

#Creo una nueva aplicacion
app = Flask(__name__)

#Escucho en la ruta raiz
@app.route("/")
def inicio():
    #Y renderizo una plantilla llamada index.html
    return render_template("inicio.html")

#Escucho en la ruta raiz
@app.route("/sobremi")
def sobremi():
    #Y renderizo una plantilla llamada index.html
    return render_template("sobremi.html")
    
#Escucho en la ruta raiz
@app.route("/contacto")
def contacto():
    #Y renderizo una plantilla llamada index.html
    return render_template("contacto.html")
    
#Si este archivo no es una libreria y es el archivo principal
if __name__ == "__main__":
    #Pon en marcha la aplicacion
    app.run(debug=True)
