import tkinter as tk
from tkinter import messagebox
import tkinter.messagebox as msg
from pyperclip import copy
import numpy as np
import random as rand
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_agg import FigureCanvasAgg
from PIL import ImageTk, Image


import customtkinter as ctk
ctk.set_default_color_theme('dark-blue')

# --------------------- CLASES DE LOS FRAMES DE LA APP

# --------------------- Frame de Home


class FrameHome(ctk.CTkFrame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.pack(fill="both", expand=True)
        # Variables del Frame Home
        self.texto = ""
        self.canvas = None
        self.lienzo = None
        # Llamada a componentes
        self.textInput()
        self.buttonCreateSplin()
        self.buttonCreatePair()
        # Configuración de la distribución de columnas
        self.grid_columnconfigure(0, weight=1)

    # -------------------- Funciones de Componentes
    def textInput(self):
        self.texto = ctk.CTkLabel(
            master=self, text="Numero de pares ordenados (8-12)", font=('Consolas', 18))
        self.texto.pack(pady=10, padx=10)

        self.text_box = ctk.CTkEntry(
            master=self, placeholder_text="Ingrese el número de pares", font=('Consolas', 18), width=350, justify="center")

        self.text_box.configure(validate="key", validatecommand=(
            self.register(lambda char: char.isdigit() or char == '-'), '%S'))
        self.text_box.configure(validatecommand=(
            self.register(self.validar_text_box), '%P'))
        self.text_box.pack(pady=10, padx=10)

    def buttonCreateSplin(self):
        self.boton = ctk.CTkButton(self, text="Ejecutar", command=self.plot_grafica,
                                   state="disabled", font=("Consolas", 24))
        self.boton.pack(pady=10, padx=10)

    def buttonCreatePair(self):
        self.boton_plot = ctk.CTkButton(self, text="Copiar Pares", command=self.copiar_pares,
                                        state="disabled", font=("Consolas", 24))
        self.boton_plot.pack(pady=10, padx=10)

    def plot_grafica(self):
        valor = int(self.text_box.get())
        lista = []
        contador = 0
        for i in range(-10, 10):
            lista.append(i)
            contador = contador + 1

        x = rand.sample(lista, valor)
        y = rand.sample(lista, valor)
        x.sort()

        self.texto = ""
        for i in range(len(x)):
            self.texto += str(x[i]) + " " + str(y[i]) + "\n"
        f = CubicSpline(x, y, bc_type='natural')
        x_new = np.linspace(x[0], x[len(x) - 1], 500)
        y_new = f(x_new)

        # Creamos una figura de Matplotlib
        fig = plt.figure(figsize=(7, 6))
        ax = fig.add_subplot(111)

        # Graficamos los datos en la figura
        ax.plot(x_new, y_new, 'b', label='Interpolación')
        ax.plot(x, y, 'ro', label='Puntos')
        for xy in zip(x, y):
            ax.annotate('(%.2f, %.2f)' % xy, xy=xy)
        ax.set_xlabel('x', fontsize=12)
        ax.set_ylabel('y', fontsize=12)
        ax.set_title('Interpolación con Splines Cúbicos', fontsize=14)
        ax.grid(True, linestyle='--', linewidth=0.9, alpha=0.5)
        ax.legend()
        
        # Ajustar los márgenes del gráfico
        plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)
        
        # Verificamos si hay un canvas
        if self.lienzo:
            self.lienzo.destroy()

        # Creamos un nuevo lienzo
        self.lienzo = ctk.CTkCanvas(self)
        self.lienzo.pack()
        # Convertir el gráfico en una imagen
        canvas_agg = fig.canvas
        canvas_agg.draw()
        buffer = canvas_agg.buffer_rgba()
        image = Image.frombytes('RGBA', canvas_agg.get_width_height(), buffer.tobytes())
        
         # Ajustar el tamaño del lienzo al tamaño del gráfico
        self.lienzo.configure(width=image.width, height=image.height)
        
        # Mostrar la imagen del gráfico en el lienzo
        self.plot_image = ImageTk.PhotoImage(image)
        self.lienzo.create_image(0, 0, anchor="nw", image=self.plot_image)
           
        # Habilitamos el botón de plotear gráfica
        self.boton_plot.configure(state="normal")

    # -------------------- Funciones de interactividad
    def validar_text_box(self, valor):
        if valor.isdigit():
            valor = int(valor)
            if valor >= 8 and valor <= 12:
                self.boton.configure(state="normal")
            else:
                self.boton.configure(state="disabled")
        else:
            self.boton.configure(state="disabled")
        return True

    def copiar_pares(self):
        copy(self.texto)
        self.showMessagePair()

    def showMessagePair(self):
        mensaje = tk.Toplevel(self)
        mensaje.geometry(str(self.center_MessagePair(210, 50)))
        mensaje.overrideredirect(True)
        mensaje_label = tk.Label(
            mensaje, text="Texto copiado en el portapapeles")
        mensaje_label.pack(padx=10, pady=10)
        mensaje.after(1500, mensaje.destroy)

    def center_MessagePair(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        return '{}x{}+{}+{}'.format(width, height, x, y)

# ---------------------------  Frame de los Creditos


class FrameCredits(ctk.CTkFrame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.pack()
        self.show_members()

    def show_members(self):
        # Limpiar el frame antes de agregar nueva información
        for widget in self.winfo_children():
            widget.destroy()

        # Lista de participantes con su nombre e información
        participants = [
            {
                "nombre": "Ballon Villar, Diego Eduardo",
                "informacion": "U201520327"
            },
            {
                "nombre": "Goñas Lopez, Franck Manuel",
                "informacion": "U201421134"
            },
            {
                "nombre": "Pilco Chiuyare, André Dario",
                "informacion": "U202110764"
            },
            {
                "nombre": "Poma Astete, Luis Felipe",
                "informacion": "U202110902"
            },
            {
                "nombre": "Sovero Cubillas, John Davids",
                "informacion": "U202115065"
            }
        ]

        # Estilos
        frame_bg_color = "#d3d9e9"  # Color de fondo del frame
        card_bg_color = "#554D74"  # Color de fondo de las tarjetas
        nombre_font = ("Consolas", 14, "bold")  # Fuente del nombre
        informacion_font = ("Consolas", 12)  # Fuente de la información
        padding_y = 10  # Relleno vertical
        border_width = 2  # Ancho del borde de las tarjetas

        # Configurar el frame
        self.config(bg=frame_bg_color)

        # Mostrar la información de cada participante en tarjetas transparentes
        for participant in participants:
            card_frame = ctk.Frame(self, bg=frame_bg_color, bd=border_width)
            card_frame.pack(pady=(padding_y, 10), expand=True)

            nombre_label = ctk.Label(card_frame, text=participant["nombre"], font=nombre_font,
                                     foreground="white", bg=card_bg_color, width=40, height=2, cursor="dot", relief="sunken")
            nombre_label.pack(pady=(padding_y // 2, 0))

            informacion_label = ctk.Label(card_frame, text=participant["informacion"], font=informacion_font,
                                          foreground="light gray", bg=card_bg_color, width=40, height=2, cursor="dot", relief="sunken")
            informacion_label.pack(
                pady=(0, padding_y // 2), fill="x")


# ----------------------- CLASE DE LA APP
class App(tk.Tk):
    def __init__(self, width=800, height=600):
        super().__init__()

        # Crear la ventana principal
        self.title("Splines Cúbicos")
        self.barra_menu()
        # Crear los marcos para cada pantalla
        self.programFrame = FrameHome(self)
        # self.creditsFrame = FrameCredits(self)

        # Posicionamiento de la ventana
        self.center_window(width, height)
        # Mostrar la pantalla de inicio
        # self.show_home()

        # Registrar función de controlador de evento para cerrar la ventana
        self.protocol("WM_DELETE_WINDOW", self.quit)

    # ------------ Funciones para la Ventana

    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def barra_menu(self):

        barra_menu = tk.Menu(self)

        # Configuración de la barra de menú
        self.config(menu=barra_menu, width=300, height=300)

        # Configuración de cada elemento del menú
        barra_menu.add_cascade(label='Inicio', command=self.show_home)
        barra_menu.add_cascade(label='Créditos', command=self.show_credits)
        barra_menu.add_cascade(label='Salir', command=self.quit)

    def show_home(self):
        # Ocultar los otros marcos y mostrar la pantalla de inicio
        self.programFrame.pack(fill=tk.BOTH, expand=1)
        self.creditsFrame.pack_forget()

    def show_credits(self):
        # Ocultar los otros marcos y mostrar la pantalla de resultados
        self.programFrame.pack_forget()
        self.creditsFrame.pack(fill=tk.BOTH, expand=1)
