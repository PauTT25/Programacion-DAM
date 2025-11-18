import mysql.connector

#Funcion de insertar    
def insertar_categoria(titulo,descripcion):
    cursor.execute('''
        INSERT INTO categoria
        VALUES(
            NULL,
            "'''+titulo+'''",
            "'''+descripcion+'''"
        );
        ''')
# --- Conexion de usuario con para mysql ---
conexion = mysql.connector.connect(
    host="localhost",
    user="portafolioceac",
    password="Simulacro123$",
    database="portafolio"
    )
cursor = conexion.cursor()

# --- Le decimos que nos imprima el titulo de la aplicacion ---
print("Inicio de CRUD piezas y categorias")
    
# --- Empezamos añadiendo un bucle --- 
while True:
    print("--- MENU ---")
    print("1.-Crear pieza")
    print("2.-Listar piezas")
    print("3.-Actualizar pieza")
    print("4.-Eliminar pieza")
    print("5.-Salir")
    
    opcion = int(input("Elige una de las opciones:"))
    
# --- Creamos la primera opcion ---
    if opcion == 1: 
        titulo = input("Nombre de la pieza:")
        descripcion = input("Descripcion de la pieza:")
        imagen = input("Imagen de la pieza:")
        url = input("URL de la pieza:")
        id_categoria = input("Introduce la categoria: ")
        
        cursor.execute('''
            INSERT INTO Pieza VALUES (
            NULL,
            "'''+titulo+'''",
            "'''+descripcion+'''",
            "'''+imagen+'''",
            "'''+url+'''",
            '''+id_categoria+'''
            );
        ''')
        conexion.commit()

# --- Creamos la segunda opcion --- 
    elif opcion == 2:
        cursor.execute('''
            SELECT * FROM pieza;
        ''')
        
        filas = cursor.fetchall()
        
        for fila in filas:
            print(fila)
        
# --- Creamos la tercera parte ---
    elif opcion == 3:
        id_pieza = input("Dime el ID de la pieza para actualizarla:")
        titulo = input("Dime el título nuevo:")
        descripcion = input("Introduce la descripcion:")
        imagen = input("Introduce la imagen: ")
        url = input("Introduce la url: ")
        id_categoria = input("Introduce la categoria: ")

        cursor.execute('''
            UPDATE Piezas SET 
                titulo = "'''+titulo+'''",
                descripcion = "'''+descripcion+'''",
                imagen = "'''+imagen+'''",
                url = "'''+url+'''",
                id_categoria = '''+id_categoria+'''
            WHERE Identificador = '''+id_pieza+''';
        ''')
        conexion.commit()
    
# --- Creamos la quarta parte --- 
    elif opcion == 4:
        identificador = input("Introduce el id a eliminar: ")
        cursor.execute('''
            DELETE FROM Piezas
            WHERE Identificador = '''+identificador+'''
        ''')
        conexion.commit()
        print("La pieza se ha eliminado.")
        
# --- Hacemos la vista unida ---
    cursor.execute('''
            SELECT *FROM pieza;
            ''')

        #Obtenemos las finals
        filas = cursor.fetchall()

        #Mostramos las filas
        if filas:
            for fila in filas:
                print(fila)
        else:
            print("No se encontraron piezas.")
            
        cursor.close()
# --- Creamos la ultima parte ---
    elif opcion == 5:
        print("Salimos de la aplicacion.")
        break
    
    
        
    
        
        
    

    
    
    





