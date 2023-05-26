import tkinter as tk
from tkinter import messagebox
import tkinter.messagebox as msg
from pyperclip import copy
import numpy as np
import random as rand
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# --------------------- CLASES DE LOS FRAMES DE LA APP

# --------------------- Frame de Home


class FrameHome(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.config(background='#d3d9e9')
        self.pack()
        # Variables del Frame Home
        self.texto = ""
        self.canvas = None
        # Llamada a componentes
        self.textInput()
        self.buttonCreateSplin()
        self.buttonCreatePair()

        # Configuración de la distribución de columnas
        self.grid_columnconfigure(0, weight=1)

    # -------------------- Funciones de Componentes
    def textInput(self):
        self.text_box = tk.Entry(self)
        self.text_box.config(validate="key", validatecommand=(
            self.register(lambda char: char.isdigit() or char == '-'), '%S'))
        self.text_box.config(validatecommand=(
            self.register(self.validar_text_box), '%P'))
        self.text_box.config(width=35, font='Consolas', justify='center')
        self.text_box.grid(row=0, column=0, pady=(15, 15))

    def buttonCreateSplin(self):
        self.boton = tk.Button(self, text="Ejecutar", command=self.plot_grafica,
                               state="disabled", bg="#a6a9c8", fg="#31293f", relief="raised", activebackground="#796ea8", font="Consolas")
        self.boton.grid(row=1, column=0, sticky='w', padx=(350, 0))

    def buttonCreatePair(self):
        self.boton_plot = tk.Button(self, text="Copiar Pares", command=self.copiar_pares,
                                    state="disabled", bg="#a6a9c8", fg="#31293f", relief="raised", activebackground="#796ea8", font="Consolas")
        self.boton_plot.grid(row=1, column=0, sticky='e', padx=(0, 350))

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
        fig = plt.figure(figsize=(10, 8), facecolor="#d3d9e9")
        ax = fig.add_subplot(111)

        # Graficamos los datos en la figura
        ax.plot(x_new, y_new, 'b')
        ax.plot(x, y, 'ro')
        for xy in zip(x, y):
            ax.annotate('(%.2f, %.2f)' % xy, xy=xy)
        ax.set_title('Interpolación con Splines Cúbicos')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.grid(True)

        # Verificamos si hay un canvas
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
        # Creamos el widget de FigureCanvasTkAgg
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=2, column=0, pady=(15, 0))
        # Habilitamos el botón de plotear gráfica
        self.boton_plot.config(state="normal")

    # -------------------- Funciones de interactividad
    def validar_text_box(self, valor):
        if valor.isdigit():
            valor = int(valor)
            if valor >= 8 and valor <= 12:
                self.boton.config(state="normal")
            else:
                self.boton.config(state="disabled")
        else:
            self.boton.config(state="disabled")
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


class FrameCredits(tk.Frame):
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
            card_frame = tk.Frame(self, bg=frame_bg_color, bd=border_width)
            card_frame.pack(pady=(padding_y, 10), expand=True)

            nombre_label = tk.Label(card_frame, text=participant["nombre"], font=nombre_font,
                                    foreground="white", bg=card_bg_color, width=40, height=2, cursor="dot", relief="sunken")
            nombre_label.pack(pady=(padding_y // 2, 0))

            informacion_label = tk.Label(card_frame, text=participant["informacion"], font=informacion_font,
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
        self.creditsFrame = FrameCredits(self)

        # Posicionamiento de la ventana
        self.overrideredirect(False)
        self.center_window(width, height)
        # Mostrar la pantalla de inicio
        self.show_home()

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
