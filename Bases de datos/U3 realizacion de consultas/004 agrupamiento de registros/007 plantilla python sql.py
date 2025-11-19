import mysql.connector 

conexion = mysql.connector.connect(
  host="localhost",
  user="1clientes",
  password="Clientes987$",
  database="clientes"
)                                      
  
cursor = conexion.cursor() 
cursor.execute('''
  SELECT 
    FLOOR(AVG(edad))
  FROM clientes;
''')  

filas = cursor.fetchall()

print(filas)
