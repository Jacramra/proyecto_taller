import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import matplotlib as plt
import os
from participante import Participante

ruta_csv = os.path.join("datos", "participantes.csv")
data = pd.read_csv(ruta_csv)


# Función para registrar persona
def registrar():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    taller = combo_taller.get()
    clases = entry_clases.get()

    if not (nombre and edad and taller and clases):
        messagebox.showerror("Campos incompletos.")
        return

    #Instancia de la clase Participante
    p = Participante(nombre, edad, taller, clases)
    df_nuevo = pd.DataFrame([p.diccionario()])     #Llama al método diccionario del objeto Participante para obtener un diccionario

    #Guardar datos en un archivo CSV
    if os.path.exists(ruta_csv):
        df_nuevo.to_csv(ruta_csv, mode="a", header=False, index=False)
    else:
        df_nuevo.to_csv(ruta_csv, index=False)
    
    messagebox.showinfo(f"{nombre} registrado satisfactoriamente.")

    #Limpio el contenido que el usuario ingresó en los campos de texto
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_clases.delete(0, tk.END)
    combo_taller.set("")


#---------------------Interfaz---------------------

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Talleres Artísticos")

# Campo: Nombre
label_nombre = tk.Label(ventana, text="Nombre:")                             # Mostrar etiqueta nombre
label_nombre.grid(row=0, column=0)          
entry_nombre = tk.Entry(ventana)                                            # Mostrar campo de texto
entry_nombre.grid(row=1, column=1)

# Campo: Nombre
label_edad = tk.Label(ventana, text="Edad:")
label_edad.grid(row=1, column=0)                                            # Mostrar etiqueta edad
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=1, column=1)                                            # Mostrar campo de texto

# Campo: Taller inscrito
label_taller = tk.Label(ventana, text="Taller inscrito:")                    # Mostrar etiqueta taller
label_taller.grid(row=2, column=0)
combo_taller = ttk.Combobox(ventana, values=["Pintura", "Teatro", "Danza"])  # Mostrar lista de opciones
combo_taller.grid(row=2, column=1)

# Campo: Número de clases tomadas
label_clases = tk.Label(ventana, text="Número de claes:")                    # Mostrar etiqueta número de clases
label_clases.grid(row=3, column=0)
entry_clases = tk.Entry(ventana)                                             # Mostrar campo de texto
entry_clases.grid(row=3, column=1)

# Botón para registrar persona
boton_registrar = tk.Button(ventana, text="Registrar persona", command=registrar)
boton_registrar.grid(row=4, column=0, pady=10)

# Botón para generar reporte
boton_reporte = tk.Button(ventana, text="Reporte", command=none)
boton_reporte.grid(row=4, column=1)

ventana.mainloop()



