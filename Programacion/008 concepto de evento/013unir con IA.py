import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# --- Conexión a la base de datos ---
try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="empresadam",
        password="Empresadam123$",
        database="empresadam"
    )
    cursor = conexion.cursor()
except mysql.connector.Error as err:
    messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos:\n{err}")
    exit()

# --- Ventana principal ---
ventana = tk.Tk()
ventana.title("Gestión de Clientes - Empresa DAM")
ventana.geometry("850x550")
ventana.configure(bg="#1E2A38")  # Azul gris oscuro elegante

# --- Estilo Moderno Oscuro ---
style = ttk.Style()
style.theme_use("clam")

# Tabla (Treeview)
style.configure("Treeview",
                background="#2C3E50",
                foreground="#ECF0F1",
                rowheight=30,
                fieldbackground="#2C3E50",
                font=("Segoe UI", 10))
style.configure("Treeview.Heading",
                background="#0D6EFD",  # Azul brillante para contraste
                foreground="white",
                font=("Segoe UI Semibold", 10))
style.map("Treeview",
          background=[("selected", "#1ABC9C")])  # Verde azulado de selección

# --- Título ---
titulo = tk.Label(ventana,
                  text="📋 Lista de Clientes",
                  font=("Segoe UI Semibold", 20),
                  bg="#1E2A38",
                  fg="#ECF0F1")
titulo.pack(pady=15)

# --- Marco principal ---
frame_tabla = ttk.Frame(ventana)
frame_tabla.pack(padx=20, pady=10, fill="both", expand=True)

# --- Scrollbar ---
scroll_y = ttk.Scrollbar(frame_tabla, orient="vertical")
scroll_y.pack(side="right", fill="y")

# --- Tabla de datos ---
arbol = ttk.Treeview(frame_tabla,
                     columns=("dninie", "nombre", "apellidos", "email"),
                     show="headings",
                     yscrollcommand=scroll_y.set)

arbol.heading("dninie", text="DNI del cliente")
arbol.heading("nombre", text="Nombre del cliente")
arbol.heading("apellidos", text="Apellidos del cliente")
arbol.heading("email", text="Email del cliente")

arbol.column("dninie", width=120, anchor="center")
arbol.column("nombre", width=180, anchor="w")
arbol.column("apellidos", width=200, anchor="w")
arbol.column("email", width=220, anchor="w")

scroll_y.config(command=arbol.yview)
arbol.pack(fill="both", expand=True)

# --- Cargar datos desde MySQL ---
try:
    cursor.execute("SELECT * FROM clientes;")
    filas = cursor.fetchall()

    for fila in filas:
        arbol.insert("", "end", values=(fila[1], fila[2], fila[3], fila[4]))
except mysql.connector.Error as err:
    messagebox.showerror("Error SQL", f"No se pudieron obtener los datos:\n{err}")

# --- Marco de botones ---
frame_botones = tk.Frame(ventana, bg="#1E2A38")
frame_botones.pack(pady=20)

# Estilo de botones
style.configure("TButton",
                font=("Segoe UI", 10, "bold"),
                padding=8)

btn_refrescar = ttk.Button(frame_botones, text="🔄 Refrescar", style="TButton",
                           command=lambda: messagebox.showinfo("Refrescar", "Función pendiente"))
btn_salir = ttk.Button(frame_botones, text="❌ Salir", style="TButton",
                       command=ventana.destroy)

btn_refrescar.pack(side="left", padx=15)
btn_salir.pack(side="left", padx=15)

# --- Pie de página ---
pie = tk.Label(ventana,
               text="© 2025 Empresa DAM | Gestión de Clientes",
               font=("Segoe UI", 9),
               bg="#1E2A38",
               fg="#95A5A6")
pie.pack(side="bottom", pady=10)

# --- Ejecutar ventana ---
ventana.mainloop()

