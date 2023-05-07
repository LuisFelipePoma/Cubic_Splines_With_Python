import tkinter as tk

# Creamos el objeto de la clase

ventana = tk.Tk()

# Dimensiones

ancho = 800
alto = 600
tamanio = str(ancho) + 'x' + str(alto)
ventana.geometry(tamanio)

# Titulo
ventana.title('Titulo de la ventana')

# Poner siempre al final
ventana.mainloop()
