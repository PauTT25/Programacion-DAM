#Importamos libreria
import sqlite3

#Nos conectamos a la base de datos
conexion = sqlite3.connect("clientes")

#Creamos un cursor
cursor = conexion.cursor()

cursor.execute('''
    SELECT * FROM clientes;
''')

filas
