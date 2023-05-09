import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Crear la ventana principal
        self.title("Enrutamiento de ventanas")
        self.geometry("400x300")
        
        # Crear los marcos para cada pantalla
        self.home_frame = tk.Frame(self)
        self.config_frame = tk.Frame(self)
        self.result_frame = tk.Frame(self)
        
        # Agregar widgets a la pantalla de inicio
        tk.Label(self.home_frame, text="¡Bienvenido!").pack()
        tk.Button(self.home_frame, text="Configuración", command=self.show_config).pack()
        
        # Agregar widgets a la pantalla de configuración
        tk.Label(self.config_frame, text="Configuración").pack()
        tk.Button(self.config_frame, text="Inicio", command=self.show_home).pack()
        tk.Button(self.config_frame, text="Resultados", command=self.show_results).pack()
        
        # Agregar widgets a la pantalla de resultados
        tk.Label(self.result_frame, text="Resultados").pack()
        tk.Button(self.result_frame, text="Inicio", command=self.show_home).pack()
        tk.Button(self.result_frame, text="Configuración", command=self.show_config).pack()
        
        # Mostrar la pantalla de inicio
        self.show_home()
    
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
    
    def show_results(self):
        # Ocultar los otros marcos y mostrar la pantalla de resultados
        self.home_frame.pack_forget()
        self.config_frame.pack_forget()
        self.result_frame.pack(fill=tk.BOTH, expand=1)

# Crear y ejecutar la aplicación
app = App()
app.mainloop()
