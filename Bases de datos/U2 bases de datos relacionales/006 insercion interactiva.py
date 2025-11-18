#Importamos libreria
import sqlite3

#Nos conectamos a la base de datos
conexion = sqlite3.connect("clientes")

#Creamos un cursor
cursor = conexion.cursor()

nombre = input("Introduce el nombre del cliente:")
apellidos = input("Introduce los apellidos del cliente:")
email = input("Introduce el email del cliente:")

cursor.execute("""
    INSERT INTO clientes VALUES(
        NULL,'"""+nombre+"""','"""+apellidos+"""','"""+email+"""'
    );
""")
conexion.commit()

cursor.execute('''
    SELECT * FROM clientes;
''')
filas = cursor.fetchall()

for fila in filas:
    print (fila)
