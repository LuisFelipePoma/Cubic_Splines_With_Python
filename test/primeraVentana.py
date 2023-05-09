import random
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.interpolate import CubicSpline

# Función para calcular los polinomios cúbicos a partir de los puntos
def calculate_polynomials(points):
    xs, ys = zip(*points)
    points = sorted(zip(xs, ys))
    xs, ys = zip(*points)
    cs = CubicSpline(xs, ys)
    return xs, ys, cs

# Función para generar puntos aleatorios
def generate_points(n):
    points = [(random.uniform(0, 1), random.uniform(0, 1)) for i in range(n)]
    return points

# Función para graficar los polinomios
def plot_polynomials(xs, ys, cs, ax):
    ax.clear()
    ax.scatter(xs, ys)
    xnew = np.linspace(min(xs), max(xs), 1000)
    ynew = cs(xnew)
    ax.plot(xnew, ynew)

# Función para manejar el botón "Generar"
def handle_generate():
    n = int(entry_n.get())
    points = generate_points(n)
    xs, ys, cs = calculate_polynomials(points)
    plot_polynomials(xs, ys, cs, ax)

# Configuración de la ventana principal
root = Tk()
root.geometry("600x800")

# Crear un marco para contener la figura
frame = Frame(root)
frame.pack(side=TOP, fill=BOTH, expand=True)

# Crear una etiqueta y una entrada para el valor de n
label_n = Label(root, text="Valor de n:")
label_n.pack(in_=frame, side=LEFT)
entry_n = Entry(root)
entry_n.pack(in_=frame, side=LEFT)

# Crear un botón y vincularlo a la función handle_generate
generate_button = Button(root, text="Generar", command=handle_generate)
generate_button.pack(in_=frame, side=LEFT)

# Crear la figura de matplotlib y agregarla al marco
fig = plt.Figure()
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

# Iniciar el bucle de eventos principal de tkinter
root.mainloop()
