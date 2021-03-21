# -----------> creada por Malcom Pozo <----------- #

from tkinter import * #importar la libreria

# VENTANA
ventana = Tk() #interfaz
ventana.title("Calculadora") #configura el titulo de la ventana
ventana.config(backgroud="lightblue") #configura el color de fondo de la ventana

# PANEL
panel = Entry(ventana,font = ("Calibri 17")) #agrega la pantalla con configuracion del tipo y tamaño de letra
panel.grid (row = 0, column = 0, columnspan = 4, padx = 5, pady = 5) # configuracion de layer 


# FUNCIONES
count = 0

# función que captura los botones apretados
def click_boton(a):
    global count
    panel.insert(count,a)
    count += 1
    
# función que borra lo ingresado en panel
def borrar():
    panel.delete(0,END)
    count = 0
    
# función que evalúa la operaciones matemáticas y devuelve el resultado    
def evaluar():
    evaluar = panel.get()
    resultado = eval(evaluar)
    panel.delete(0,END)
    panel.insert(0,resultado)
    count = 0


ventana.mainloop()