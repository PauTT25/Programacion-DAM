#Librerias a importar
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

#Conexion de suusario para mysql
conexion = mysql.connector.connect(
    host="localhost",
    user="Usimulacro",
    password="Simulacro123$",
    database="simulacro"
)

#Mensaje de entrada
print("-----------------------------")
print("#####Rodrigo Menendez Molina######")
print("###CRUD pieza y categorias v0.1###")

#Bucle y menu
while True:
    print("-----------------------------")
    print("-------Menu-------")
    print("1. Añadir pieza")
    print("2. Listar piezas")
    print("3. Actualizar pieza")
    print("4. Eliminar pieza")
    print("5. Salir")
    opcion = int(input("Que pocion quieres: "))
    print("-----------------------------")


##############################################################################################
    #Priemra opcion, añadir pieza
    if opcion == 1:

        print("1. Insertar pieza")
        print("2. Insertar categoria")
        op1 = int(input("Opcion: "))

        cursor = conexion.cursor()

        if op1 == 1:
            titulo = input("Titulo: ")
            descripcion = input("Descripcion: ")
            imagen = input("Imagen: ")
            url = input("Url de la imagen: ")
            id_categoria = input("Identificador categoria: ")

            cursor.execute('''
                INSERT INTO pieza
                VALUES(
                    NULL,
                    "'''+titulo+'''",
                    "'''+descripcion+'''",
                    "'''+imagen+'''",
                    "'''+url+'''",
                    '''+id_categoria+'''
                    );
                ''')

            conexion.commit()

            print("Pieza añadida correctamente")

        elif op1 == 2:
            titulo = input("Titulo: ")
            descripcion = input("Descipcion: ")
            
            insertar_categoria(titulo,descripcion)

            conexion.commit()

            print("Pieza añadida correctamente")

        cursor.close()

##############################################################################################

    #Seguna opcion listar piezas
    elif opcion == 2:

        #Cramos el cursor y ejecutamos al consulta, mostramos la vision de piezas y categorias
        cursor = conexion.cursor()
        cursor.execute('''
            SELECT *FROM vista_piezas;
            ''')

        #Obtenemos las finals
        filas = cursor.fetchall()

        #Mostramos las filas
        if filas:
            for fila in filas:
                print(fila)
        else:
            print("No se encontraron piezas.")

        print("--------------------------------")

        #Mostramos piezas
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

##############################################################################################
    #Opcion3, actualizar una pieza
    elif opcion == 3:

        identificador = input("Identificador de la pieza a actualizar: ")

        titulo = input("Nuevo titulo: ")
        descripcion = input("Nueva descripcion: ")
        imagen = input("Nueva imagen: ")
        url = input("Nuevo url de la imagen: ")
        id_categoria = input("Nuevo identificador categoria: ")

        cursor = conexion.cursor()
        cursor.execute('''
        cursor.execute('''
            UPDATE pieza
            SET titulo = "'''+titulo+'''",
                descripcion = "'''+descripcion+'''",
                imagen = "'''+imagen+'''",
                url = "'''+url+'''",
                id_categoria = "'''+id_categoria+'''"
                WHERE identificador = "'''+identificador+'''";
            ''')
        
        conexion.commit()
        cursor.execute('''

        print("Pieza actualizada")

        cursor.close()

############################################################################################
    #Opcion 4, eliminar una pieza
    elif opcion == 4:

        #Pedimos el identificador de la pieza que se va a a eliminar
        identificador = input("Identific
        cursor.execute('''ador de la pieza a eliminar: ")

        cursor = conexion.cursor()
        cursor.execute('''
        DELETE FROM pieza WHERE identificador = '''+identificador+'''                       
        ''')

        conexion.commit()

        print("Pieza borrada")

        cursor.close()

##############################################################################################
    #Opcion 5, salir
    elif opcion == 5:
        break

    else:
        print("Inavlido")
 
        cursor.execute('''
