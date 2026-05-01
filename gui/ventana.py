import tkinter as tk  # Importa la librería Tkinter y la renombra como "tk" para usarla más fácil

from logic.funciones import saludar  # Importa la función "saludar" desde otro archivo (lógica separada)

def iniciar_app():  # Define una función que se encargará de iniciar toda la aplicación
    ventana = tk.Tk()  # Crea la ventana principal de la aplicación

    ventana.title("Mi Proyecto")  # Establece el título que aparece en la barra de la ventana

    ventana.geometry("400x300")  # Define el tamaño de la ventana: 400px ancho x 300px alto

    # Crea un botón dentro de la ventana
    # - "ventana" → indica dónde se coloca
    # - "text" → texto que aparece en el botón
    # - "command" → función que se ejecuta al hacer clic
    boton = tk.Button(ventana, text="Saludar", command=saludar)

    boton.pack(pady=80)  
    # "pack" coloca el botón en la ventana
    # "pady=20" añade espacio vertical (arriba y abajo) de 20 píxeles

    ventana.mainloop()  
    # Inicia el bucle principal de la interfaz
    # Mantiene la ventana abierta y escuchando eventos (clics, teclado, etc.)