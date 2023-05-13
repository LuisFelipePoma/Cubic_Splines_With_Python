import tkinter as tk
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random as rand

def plot_grafica():
    valor = int(text_box.get())
    lista = []
    contador = 0
    for i in range(-10, 10):
        lista.append(i)
        contador = contador + 1

    x = rand.sample(lista, valor)
    y = rand.sample(lista, valor)
    x.sort()
    f = CubicSpline(x, y, bc_type='natural')
    x_new = np.linspace(x[0], x[len(x) - 1], 500)
    y_new = f(x_new)

    # Creamos una figura de Matplotlib
    fig = plt.figure(figsize=(10, 8))
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

    # Creamos el widget de FigureCanvasTkAgg
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

root = tk.Tk()
root.geometry("800x600")  # Definimos el tamaño de la ventana
root.protocol("WM_DELETE_WINDOW", root.quit)  # Registrar función de controlador de evento para cerrar la ventana

# Creamos el cuadro de texto y lo configuramos para que solo acepte números
text_box = tk.Entry(root)
text_box.pack()
text_box.config(validate="key", validatecommand=(root.register(lambda char: char.isdigit() or char == '-'), '%S'))

# Creamos el botón y lo deshabilitamos al inicio
boton = tk.Button(root, text="Ejecutar", command=plot_grafica, state="disabled")
boton.pack()

# Función para validar el valor del text_box y habilitar o deshabilitar el botón
def validar_text_box(valor):
    if valor.isdigit():
        valor = int(valor)
        if valor >= 8 and valor <= 12:
            boton.config(state="normal")
        else:
            boton.config(state="disabled")
    else:
        boton.config(state="disabled")
    return True

# Asociamos la función de validación al cuadro de texto
text_box.config(validatecommand=(root.register(validar_text_box), '%P'))

root.mainloop()