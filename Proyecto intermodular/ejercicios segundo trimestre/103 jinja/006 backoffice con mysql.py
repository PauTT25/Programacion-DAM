#Importo la libreria Flask para poder crear webs
from flask import Flask, render_template
import mysql.connector				#Importamos MySQL

########################## MYSQL ##########################################################
conexion = mysql.connector.connect(
host="localhost", user= "ExamenTrimestral", password= "ExamenTrimestral123$", database= "portafolioexamen"
)																				#Datos de la conexion a la base de datos
cursor = conexion.cursor()														#Creo un cursor MySQL
#--------------- ESTO ENVIA LAS TABLAS---------------------------------------------------------------------
cursor.execute("SHOW TABLES;")													#Muestra las tablas de la base de datos
tablas = []																		#Creo una lista vacia
filas = cursor.fetchall()														#Lo guardo en una lista
for fila in filas:																#Recorro el resultado
  tablas.append(fila[0])														#Lo añado a la lista de tablas
#--------------- ESTO ENVIA LAS CABECERAS DE LAS TABLAS--------------------------------------------------------
cursor.execute("SHOW COLUMNS in piezasportafolio;")								#Muestra las columnas de la base de datos
columnas = []																	#Creo una lista vacia
filas = cursor.fetchall()														#Lo guardo en una lista
for fila in filas:																#Recorro el resultado
	columnas.append(fila[0])													#Lo anado a la lista de tablas

#--------------- ESTO ENVIA TODA LA TABLA--------------------------------------------------------
cursor.execute("SELECT * FROM piezasportafolio;")								#Muestra las tablas de la base de datos
contenido_tabla = cursor.fetchall()												#Lo guardo en una lista
																																	
########################## MYSQL ##########################################################
 
 
#Creo una nueva aplicacion
app = Flask(__name__)

#Escucho en la ruta raiz
@app.route("/")
def inicio():
    #Y renderizo una plantilla llamada index.html
    return render_template("backoffice.html",mis_tablas = tablas,mis_columnas = columnas, mi_contenido_tabla = tablas)				#Envio las tablas a HTML
    
#Si este archivo no es una libreria y es el archivo principal
if __name__ == "__main__":
    #Pon en marcha la aplicacion
    app.run(debug=True)
