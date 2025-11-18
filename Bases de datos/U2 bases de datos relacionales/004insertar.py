#Importamos libreria
import sqlite3

#Nos conectamos a la base de datos
conexion = sqlite3.connect("clientes")

#Creamos un cursor
cursor = conexion.cursor()

#Ejecutamos una sentencia
cursor.execute('''
    CREATE TABLE IF NOT EXISTS "clientes" (
	"Identificador"	INTEGER,
	"nombre"	TEXT,
	"descripcion"	TEXT,
	"email"	TEXT,
	PRIMARY KEY("Identificador" AUTOINCREMENT)
);
''')

#Lanzamos la peticion
conexion.commit()

