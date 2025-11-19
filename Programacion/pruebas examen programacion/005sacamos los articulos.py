import mysql.connector
from flask import Flask

conexion = mysql.connector.connect(
    host="localhost",
    user="portafolio",
    password="portafolio123$",
    database="portafolio"
    )
cursor = conexion.cursor()
app = Flask(__name__)

@app.route("/")
def holamundo():
    cursor.execute("SELECT * FROM piezas_y_categorias;")
    
    filas = cursor.fetchall()
    
    cadena = ""
    
    for fila in filas:
        cadena += str(fila)
        
    cadena + = ""
    return cadena
    
if __name__ == "__main__":
        
