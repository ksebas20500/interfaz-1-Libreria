import tkinter as tk
from tkinter import Toplevel, messagebox

# Base
Raiz = tk.Tk()
Raiz.title("MENÚ BIBLIOTECA")
Raiz.geometry("800x600")
Raiz.configure(bg="lightblue")

# Adding a frame for the menu
menu_frame = tk.Frame(Raiz, bg="darkgrey", width=200)
menu_frame.pack(side="left", fill="y")

# Adding a frame for the logo
logo_frame = tk.Frame(Raiz, bg="lightblue")
logo_frame.pack(side="right", expand=True, fill="both")

# Load the logo image
logo_image = tk.PhotoImage(file="Poo-2Corte/images.png")
logo_label = tk.Label(logo_frame, image=logo_image, bg="lightblue")
logo_label.pack(expand=True)

# Define the class structure
class Libro:
    def __init__(self, titulo, id, autor, categoria):
        self.titulo = titulo
        self.id = id
        self.autor = autor
        self.categoria = categoria

    def mostrar_info(self):
        return f"Titulo: {self.titulo}, Id: {self.id}, Autor: {self.autor}, Categoria: {self.categoria}"

class Autor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_info(self):
        return f"Autor: {self.nombre} {self.apellido}"

class Usuario:
    def __init__(self, nombre, apellido, id_usuario):
        self.nombre = nombre
        self.apellido = apellido
        self.id_usuario = id_usuario

    def mostrar_info(self):
        return f"Usuario: {self.nombre} {self.apellido}, Id: {self.id_usuario}"

class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def mostrar_info(self):
        return (
            f"Prestamo:\n{self.libro.mostrar_info()}\n{self.usuario.mostrar_info()}\n"
            f"Fecha prestamo: {self.fecha_prestamo}\nFecha devolucion: {self.fecha_devolucion}"
        )

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_info(self):
        return f"Categoria: {self.nombre}"

class Biblioteca:
    def __init__(self):
        self.libro = []
        self.usuario = []
        self.prestamo = []

    def registrar_libro(self, libro):
        self.libro.append(libro)

    def registrar_usuario(self, usuario):
        self.usuario.append(usuario)

    def realizar_prestamo(self, prestamo):
        self.prestamo.append(prestamo)

    def devolver_libro(self, id_libro, id_usuario):
        prestamo_a_devolver = None
        for prestamo in self.prestamo:
            if prestamo.libro.id == id_libro and prestamo.usuario.id_usuario == id_usuario:
                prestamo_a_devolver = prestamo
                break
        if prestamo_a_devolver:
            self.prestamo.remove(prestamo_a_devolver)
            return True
        return False

    def mostrar_libros(self):
        return [libro.mostrar_info() for libro in self.libro]

    def buscar_libro(self, id_libro):
        for libro in self.libro:
            if libro.id == id_libro:
                return libro
        return None

    def buscar_usuario(self, id_usuario):
        for usuario in self.usuario:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None

# Create a Biblioteca instance
Biblioteca = Biblioteca()

# Register user
def registrar_usuario():
    ventana_registro = Toplevel(Raiz)
    ventana_registro.title("Registro de usuario")
    ventana_registro.geometry("300x250")

    tk.Label(ventana_registro, text="Hola, registra tus datos").place(relx=0.3, rely=0.05)
    tk.Label(ventana_registro, text="Nombre").place(relx=0.1, rely=0.25)
    tk.Label(ventana_registro, text="Apellido").place(relx=0.1, rely=0.35)
    tk.Label(ventana_registro, text="Id usuario").place(relx=0.1, rely=0.45)

    usuario_registro = tk.StringVar()
    tk.Entry(ventana_registro, textvariable=usuario_registro).place(relx=0.35, rely=0.25)

    apellido_registro = tk.StringVar()
    tk.Entry(ventana_registro, textvariable=apellido_registro).place(relx=0.35, rely=0.35)

    id_usuario_registro = tk.StringVar()
    tk.Entry(ventana_registro, textvariable=id_usuario_registro).place(relx=0.35, rely=0.45)

    def guardar_usuario():
        nombre = usuario_registro.get()
        apellido = apellido_registro.get()
        id_usuario = id_usuario_registro.get()
        nuevo_usuario = Usuario(nombre, apellido, id_usuario)
        Biblioteca.registrar_usuario(nuevo_usuario)
        messagebox.showinfo("Registro exitoso", "El usuario ha sido registrado exitosamente")
        ventana_registro.destroy()

    tk.Button(ventana_registro, text="Registrar usuario", command=guardar_usuario).place(relx=0.6, rely=0.75)
    tk.Button(ventana_registro, text="Cerrar", command=ventana_registro.destroy).place(relx=0.3, rely=0.75)

# Register book
def registrar_libro():
    ventana_registro_libro = Toplevel(Raiz)
    ventana_registro_libro.title("Registrar libro")
    ventana_registro_libro.geometry("300x250")

    tk.Label(ventana_registro_libro, text="Titulo del libro").place(relx=0.1, rely=0.25)
    tk.Label(ventana_registro_libro, text="Id del libro").place(relx=0.1, rely=0.35)
    tk.Label(ventana_registro_libro, text="Autor del libro").place(relx=0.1, rely=0.45)
    tk.Label(ventana_registro_libro, text="Categoria del libro").place(relx=0.1, rely=0.55)

    titulo_var = tk.StringVar()
    tk.Entry(ventana_registro_libro, textvariable=titulo_var).place(relx=0.45, rely=0.25)

    id_libro_var = tk.StringVar()
    tk.Entry(ventana_registro_libro, textvariable=id_libro_var).place(relx=0.45, rely=0.35)

    autor_var = tk.StringVar()
    tk.Entry(ventana_registro_libro, textvariable=autor_var).place(relx=0.45, rely=0.45)

    categoria_var = tk.StringVar()
    tk.Entry(ventana_registro_libro, textvariable=categoria_var).place(relx=0.45, rely=0.55)

    def guardar_libro():
        titulo = titulo_var.get()
        id_li = id_libro_var.get()
        autor = autor_var.get()
        categoria = categoria_var.get()
        nuevo_libro = Libro(titulo, id_li, autor, categoria)
        Biblioteca.registrar_libro(nuevo_libro)
        messagebox.showinfo("Registro exitoso", "El libro ha sido registrado exitosamente")
        ventana_registro_libro.destroy()

    tk.Button(ventana_registro_libro, text="Registrar libro", command=guardar_libro).place(relx=0.6, rely=0.75)

# Show registered books
def mostrar_libros():
    ventana_mostrar_libros = Toplevel(Raiz)
    ventana_mostrar_libros.title("Libros registrados")
    ventana_mostrar_libros.geometry("400x300")

    lista_libros = Biblioteca.mostrar_libros()
    texto_libros = "\n".join(lista_libros)

    tk.Label(ventana_mostrar_libros, text=texto_libros, justify=tk.LEFT).pack(pady=10, padx=10)
    tk.Button(ventana_mostrar_libros, text="Cerrar", command=ventana_mostrar_libros.destroy).pack(pady=10)

# Borrow books
def datos_libro():
    ventana_prestar_libro = Toplevel(Raiz)
    ventana_prestar_libro.title("Prestar libro")
    ventana_prestar_libro.geometry("300x250")

    tk.Label(ventana_prestar_libro, text="Id del libro").place(relx=0.1, rely=0.25)
    tk.Label(ventana_prestar_libro, text="Id usuario").place(relx=0.1, rely=0.35)
    tk.Label(ventana_prestar_libro, text="Fecha de préstamo").place(relx=0.1, rely=0.45)
    tk.Label(ventana_prestar_libro, text="Fecha de devolución").place(relx=0.1, rely=0.55)

    libro_var = tk.StringVar()
    tk.Entry(ventana_prestar_libro, textvariable=libro_var).place(relx=0.45, rely=0.25)

    usuario_var = tk.StringVar()
    tk.Entry(ventana_prestar_libro, textvariable=usuario_var).place(relx=0.45, rely=0.35)

    fecha_prestamo_var = tk.StringVar()
    tk.Entry(ventana_prestar_libro, textvariable=fecha_prestamo_var).place(relx=0.45, rely=0.45)

    fecha_devolucion_var = tk.StringVar()
    tk.Entry(ventana_prestar_libro, textvariable=fecha_devolucion_var).place(relx=0.45, rely=0.55)

    def guardar_prestamo():
        id_libro = libro_var.get()
        id_usuario = usuario_var.get()
        fecha_prestamo = fecha_prestamo_var.get()
        fecha_devolucion = fecha_devolucion_var.get()

        libro = Biblioteca.buscar_libro(id_libro)
        usuario = Biblioteca.buscar_usuario(id_usuario)

        if libro and usuario:
            nuevo_prestamo = Prestamo(libro, usuario, fecha_prestamo, fecha_devolucion)
            Biblioteca.realizar_prestamo(nuevo_prestamo)
            messagebox.showinfo("Préstamo exitoso", "El libro ha sido prestado exitosamente")
            ventana_prestar_libro.destroy()
        else:
            messagebox.showerror("Error", "Libro o usuario no encontrado")

    tk.Button(ventana_prestar_libro, text="Prestar libro", command=guardar_prestamo).place(relx=0.6, rely=0.75)

# Return books
def devolver_libro():
    ventana_devolver_libro = Toplevel(Raiz)
    ventana_devolver_libro.title("Devolver libro")
    ventana_devolver_libro.geometry("300x250")

    tk.Label(ventana_devolver_libro, text="Id del libro").place(relx=0.1, rely=0.25)
    tk.Label(ventana_devolver_libro, text="Id usuario").place(relx=0.1, rely=0.35)

    id_libro_var = tk.StringVar()
    tk.Entry(ventana_devolver_libro, textvariable=id_libro_var).place(relx=0.45, rely=0.25)

    id_usuario_var = tk.StringVar()
    tk.Entry(ventana_devolver_libro, textvariable=id_usuario_var).place(relx=0.45, rely=0.35)

    def realizar_devolucion():
        id_libro = id_libro_var.get()
        id_usuario = id_usuario_var.get()

        if Biblioteca.devolver_libro(id_libro, id_usuario):
            messagebox.showinfo("Devolución exitosa", "El libro ha sido devuelto exitosamente")
            ventana_devolver_libro.destroy()
        else:
            messagebox.showerror("Error", "Libro o usuario no encontrado, o no hay préstamo registrado")

    tk.Button(ventana_devolver_libro, text="Devolver libro", command=realizar_devolucion).place(relx=0.6, rely=0.75)

# Menu buttons
btn_registrar_usuario = tk.Button(menu_frame, text="Registrar Usuario", command=registrar_usuario, bg="white", width=20, height=2)
btn_registrar_usuario.pack(pady=10)

btn_registrar_libro = tk.Button(menu_frame, text="Registrar Libro", command=registrar_libro, bg="white", width=20, height=2)
btn_registrar_libro.pack(pady=10)

btn_mostrar_libros = tk.Button(menu_frame, text="Mostrar Libros", command=mostrar_libros, bg="white", width=20, height=2)
btn_mostrar_libros.pack(pady=10)

btn_prestar_libro = tk.Button(menu_frame, text="Prestar Libro", command=datos_libro, bg="white", width=20, height=2)
btn_prestar_libro.pack(pady=10)

# Add the "Devolver Libro" button to the menu
btn_devolver_libro = tk.Button(menu_frame, text="Devolver Libro", command=devolver_libro, bg="white", width=20, height=2)
btn_devolver_libro.pack(pady=10)

# Close button
btn_cerrar = tk.Button(Raiz, text="Cerrar", command=Raiz.quit, bg="red", fg="white", width=10, height=2)
btn_cerrar.pack(side="bottom", pady=10)

Raiz.mainloop()
