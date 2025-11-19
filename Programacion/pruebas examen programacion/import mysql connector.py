import mysql.connector

def insertar_categoria(cursor, conexion, titulo, descripcion):
    cursor.execute("INSERT INTO categoria (titulo, descripcion) VALUES (%s, %s)", (titulo, descripcion))
    conexion.commit()

conexion = mysql.connector.connect(
    host="localhost",
    user="portafolio",
    password="portafolio123$",
    database="portafolio"
)
cursor = conexion.cursor()

print("Inicio de CRUD piezas y categorias")

while True:
    print("\n--- MENU ---")
    print("1. Crear pieza")
    print("2. Listar piezas")
    print("3. Actualizar pieza")
    print("4. Eliminar pieza")
    print("5. Ver vista unida (pieza + categoría)")
    print("6. Salir")

    opcion = int(input("Elige una de las opciones: "))

    if opcion == 1:
        titulo = input("Nombre de la pieza: ")
        descripcion = input("Descripción: ")
        imagen = input("Imagen: ")
        url = input("URL: ")
        id_categoria = input("ID de categoría: ")
        cursor.execute("""
            INSERT INTO piezas (titulo, descripcion, imagen, url, id_categoria)
            VALUES (%s, %s, %s, %s, %s)
        """, (titulo, descripcion, imagen, url, id_categoria))
        conexion.commit()

    elif opcion == 2:
        cursor.execute("SELECT * FROM piezas")
        for fila in cursor.fetchall():
            print(fila)

    elif opcion == 3:
        id_pieza = input("ID de la pieza a actualizar: ")
        titulo = input("Nuevo título: ")
        descripcion = input("Nueva descripción: ")
        imagen = input("Nueva imagen: ")
        url = input("Nueva URL: ")
        id_categoria = input("Nueva categoría: ")
        cursor.execute("""
            UPDATE piezas SET titulo=%s, descripcion=%s, imagen=%s, url=%s, id_categoria=%s
            WHERE identificador=%s
        """, (titulo, descripcion, imagen, url, id_categoria, id_pieza))
        conexion.commit()

    elif opcion == 4:
        id_pieza = input("ID de la pieza a eliminar: ")
        cursor.execute("DELETE FROM piezas WHERE identificador=%s", (id_pieza,))
        conexion.commit()
        print("Pieza eliminada.")

    elif opcion == 5:
        cursor.execute("SELECT * FROM vista_pieza")
        for fila in cursor.fetchall():
            print(fila)

    elif opcion == 6:
        print("Saliendo del programa.")
        break

cursor.close()
conexion.close()

