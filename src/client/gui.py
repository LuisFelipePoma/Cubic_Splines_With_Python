import tkinter as tk


# --------------------- CLASES DE LOS FRAMES DE LA APP
class FrameHome(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()


class FrameConfig(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        self.config(bg="green")


class FrameCredits(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        self.config(bg="blue")

# ----------------------- CLASE DE LA APP
class App(tk.Tk):
    def __init__(self, width=800, height=600):
        super().__init__()

        # Crear la ventana principal
        self.title("Splines Cubicos")
        self.barra_menu()
        # Crear los marcos para cada pantalla
        self.home_frame = FrameHome(self)
        self.config_frame = FrameConfig(self)
        self.result_frame = FrameCredits(self)

        # Posicionamiento de la ventana
        self.overrideredirect(True)
        self.center_window(width,height)
        # Mostrar la pantalla de inicio
        self.show_home()
        
    # ------------ Funciones para la Ventana
    
    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def barra_menu(self):
        barra_menu = tk.Menu(self)
        self.config(menu=barra_menu, width=300, height=300)

        barra_menu.add_cascade(label='Inicio', command=self.show_home)
        barra_menu.add_cascade(label='Teoria', command=self.show_config)
        barra_menu.add_cascade(label='Creditos', command=self.show_credits)
        barra_menu.add_cascade(label='Salir', command=self.destroy)

    def show_home(self):
        # Ocultar los otros marcos y mostrar la pantalla de inicio
        self.config_frame.pack_forget()
        self.result_frame.pack_forget()
        self.home_frame.pack(fill=tk.BOTH, expand=1)

    def show_config(self):
        # Ocultar los otros marcos y mostrar la pantalla de configuración
        self.home_frame.pack_forget()
        self.result_frame.pack_forget()
        self.config_frame.pack(fill=tk.BOTH, expand=1)

    def show_credits(self):
        # Ocultar los otros marcos y mostrar la pantalla de resultados
        self.home_frame.pack_forget()
        self.config_frame.pack_forget()
        self.result_frame.pack(fill=tk.BOTH, expand=1)
