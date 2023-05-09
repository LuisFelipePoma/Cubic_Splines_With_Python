from tkinter import *

# Funciones para cambiar de ventana
def show_main_window():
    main_window.deiconify()
    other_window.withdraw()

def show_other_window():
    other_window.deiconify()
    main_window.withdraw()

# Crear la ventana principal
main_window = Tk()
main_window.title("Ventana principal")

# Crear una etiqueta y una entrada para el valor de n
label_n = Label(main_window, text="Valor de n:")
label_n.pack(pady=(20, 5))  # Espacio vertical: 20 píxeles arriba, 5 píxeles abajo
entry_n = Entry(main_window)
entry_n.pack(pady=5)  # Espacio vertical: 5 píxeles arriba y abajo

# Crear un botón para ir a otra ventana
other_window_button = Button(main_window, text="Ir a otra ventana", command=show_other_window)
other_window_button.pack(pady=20)  # Espacio vertical: 20 píxeles arriba

# Configurar el empaquetado de la ventana principal
main_window.geometry("400x300")
main_window.pack_propagate(0)  # Evita que la ventana cambie de tamaño al añadir widgets
main_window.pack(fill=BOTH, expand=True)  # Rellena la ventana principal y expande los widgets

# Crear otra ventana
other_window = Toplevel(main_window)
other_window.title("Otra ventana")

# Crear un botón para volver a la ventana principal
main_window_button = Button(other_window, text="Volver a la ventana principal", command=show_main_window)
main_window_button.pack(pady=20)

# Configurar el empaquetado de la otra ventana
other_window.geometry("300x200")
other_window.pack_propagate(0)  # Evita que la ventana cambie de tamaño al añadir widgets

# Mostrar la ventana principal
main_window.mainloop()
