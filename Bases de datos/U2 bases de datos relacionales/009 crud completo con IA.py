import sqlite3
import os

# Conexión y creación de tabla si no existe
conexion = sqlite3.connect("clientes.db")
cursor = conexion.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        Identificador INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellidos TEXT NOT NULL,
        email TEXT NOT NULL
    )
""")
conexion.commit()

# === Colores ANSI ===
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def imprimir_titulo():
    print(f"{BOLD}{MAGENTA}═══════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{CYAN}   📒 AGENDA SQLite v1.0 — Pau Contreras Romero{RESET}")
    print(f"{BOLD}{MAGENTA}═══════════════════════════════════════════════{RESET}\n")

def imprimir_menu():
    print(f"""{YELLOW}
    1. ➕ Crear cliente
    2. 📜 Listar clientes
    3. ✏️  Actualizar cliente
    4. ❌ Eliminar cliente
    5. 🚪 Salir
{RESET}""")

while True:
    limpiar_pantalla()
    imprimir_titulo()
    imprimir_menu()

    try:
        opcion = int(input(f"{BOLD}{BLUE}Selecciona una opción: {RESET}"))
    except ValueError:
        print(f"{RED}❗ Opción inválida. Introduce un número del 1 al 5.{RESET}")
        input("Pulsa Enter para continuar...")
        continue

    if opcion == 1:
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        email = input("Email: ")
        cursor.execute("INSERT INTO clientes (nombre, apellidos, email) VALUES (?, ?, ?)", 
                       (nombre, apellidos, email))
        conexion.commit()
        print(f"{GREEN}✅ Cliente añadido correctamente.{RESET}")

    elif opcion == 2:
        cursor.execute("SELECT * FROM clientes")
        filas = cursor.fetchall()
        print(f"\n{BOLD}{CYAN}📋 Lista de clientes:{RESET}")
        print(f"{MAGENTA}{'-'*50}{RESET}")
        for fila in filas:
            print(f"{YELLOW}ID:{RESET} {fila[0]} | {GREEN}{fila[1]} {fila[2]}{RESET} | {CYAN}{fila[3]}{RESET}")
        print(f"{MAGENTA}{'-'*50}{RESET}")

    elif opcion == 3:
        identificador = input("ID del cliente a actualizar: ")
        cursor.execute("SELECT * FROM clientes WHERE Identificador = ?", (identificador,))
        cliente = cursor.fetchone()
        if not cliente:
            print(f"{RED}❗ No se encontró un cliente con ese ID.{RESET}")
        else:
            nombre = input(f"Nuevo nombre [{cliente[1]}]: ") or cliente[1]
            apellidos = input(f"Nuevos apellidos [{cliente[2]}]: ") or cliente[2]
            email = input(f"Nuevo email [{cliente[3]}]: ") or cliente[3]
            cursor.execute("""
                UPDATE clientes
                SET nombre = ?, apellidos = ?, email = ?
                WHERE Identificador = ?
            """, (nombre, apellidos, email, identificador))
            conexion.commit()
            print(f"{GREEN}✅ Cliente actualizado correctamente.{RESET}")

    elif opcion == 4:
        identificador = input("ID del cliente a eliminar: ")
        cursor.execute("SELECT * FROM clientes WHERE Identificador = ?", (identificador,))
        cliente = cursor.fetchone()
        if not cliente:
            print(f"{RED}❗ No se encontró un cliente con ese ID.{RESET}")
        else:
            confirmar = input(f"{RED}¿Seguro que deseas eliminar a {cliente[1]} {cliente[2]}? (s/n): {RESET}")
            if confirmar.lower() == "s":
                cursor.execute("DELETE FROM clientes WHERE Identificador = ?", (identificador,))
                conexion.commit()
                print(f"{GREEN}✅ Cliente eliminado correctamente.{RESET}")
            else:
                print(f"{YELLOW}↩️  Operación cancelada.{RESET}")

    elif opcion == 5:
        print(f"{MAGENTA}👋 ¡Hasta pronto!{RESET}")
        conexion.close()
        break

    else:
        print(f"{RED}❗ Opción no válida. Intenta de nuevo.{RESET}")

    input(f"\n{BOLD}Pulsa Enter para continuar...{RESET}")

