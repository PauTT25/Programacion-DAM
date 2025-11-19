import mysql.connector
# --- Conexión ---
conexion = mysql.connector.connect(
    host="localhost",
    user="portafolioceac",
    password="Simulacro123$",
    database="portafolio"
)
cursor = conexion.cursor()

print("Inicio de CRUD piezas y categorias")


while True:
    print("--- MENU ---")
    print("1.-Crear pieza")
    print("2.-Listar piezas")
    print("3.-Actualizar pieza")
    print("4.-Eliminar pieza")
    print("5.-Salir")
    
    opcion = int(input("Elige una de las opciones:"))
    
    # --- Crear pieza ---
    if opcion == 1: 
        titulo = input("Nombre de la pieza: ")
        descripcion = input("Descripcion de la pieza: ")
        imagen = input("Imagen de la pieza: ")
        url = input("URL de la pieza: ")
        id_categoria = input("Introduce la categoria: ")
        
        
        cursor.execute('''
            INSERT INTO pieza VALUES (
                NULL,
                "'''+titulo+'''",
                "'''+descripcion+'''",
                "'''+imagen+'''",
                "'''+url+'''",
                '''+id_categoria+'''
            );
        ''')
        conexion.commit()

    # --- Listar piezas ---
    elif opcion == 2:
        cursor.execute('SELECT * FROM pieza;')
        filas = cursor.fetchall()

        if filas:
            for fila in filas:
                print(fila)
        else:
            print("No se encontraron piezas.")

    # --- Actualizar pieza ---
    elif opcion == 3:
        id_pieza = input("Dime el ID de la pieza para actualizarla: ")
        titulo = input("Dime el título nuevo: ")
        descripcion = input("Introduce la descripcion: ")
        imagen = input("Introduce la imagen: ")
        url = input("Introduce la url: ")
        id_categoria = input("Introduce la categoria: ")

        cursor.execute('''
            UPDATE pieza SET 
                titulo = "'''+titulo+'''",
                descripcion = "'''+descripcion+'''",
                imagen = "'''+imagen+'''",
                url = "'''+url+'''",
                id_categoria = '''+id_categoria+'''
            WHERE Identificador = '''+id_pieza+''';
        ''')
        conexion.commit()

    # --- Eliminar pieza ---
    elif opcion == 4:
        identificador = input("Introduce el id a eliminar: ")
        cursor.execute('DELETE FROM pieza WHERE Identificador = ' + identificador)
        conexion.commit()
        print("La pieza se ha eliminado.")

    # --- Salir ---
    elif opcion == 5:
        print("Salimos de la aplicación.")
        break

# Cierre de conexión
cursor.close()
conexion.close()

    
    
        
    
        
        
    

    
    
    





