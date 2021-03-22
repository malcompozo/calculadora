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

# BOTONES NUMERICOS
# configurando tamaño, posición y devolución de números
boton0 = Button(ventana, text = "0", width = 14,height = 2, command = lambda:click_boton(0)) 
boton1 = Button(ventana, text = "1", width =  5,height = 2, command = lambda:click_boton(1))
boton2 = Button(ventana, text = "2", width =  5,height = 2, command = lambda:click_boton(2))
boton3 = Button(ventana, text = "3", width =  5,height = 2, command = lambda:click_boton(3))
boton4 = Button(ventana, text = "4", width =  5,height = 2, command = lambda:click_boton(4))
boton5 = Button(ventana, text = "5", width =  5,height = 2, command = lambda:click_boton(5))
boton6 = Button(ventana, text = "6", width =  5,height = 2, command = lambda:click_boton(6))
boton7 = Button(ventana, text = "7", width =  5,height = 2, command = lambda:click_boton(7))
boton8 = Button(ventana, text = "8", width =  5,height = 2, command = lambda:click_boton(8))
boton9 = Button(ventana, text = "9", width =  5,height = 2, command = lambda:click_boton(9))

boton_div   = Button(ventana, text = "/", width = 5,height = 2, command = lambda:click_boton("/"))
boton_multi = Button(ventana, text = "*", width = 5,height = 2, command = lambda:click_boton("*"))
boton_suma  = Button(ventana, text = "+", width = 5,height = 2, command = lambda:click_boton("+"))
boton_resta = Button(ventana, text = "-", width = 5,height = 2, command = lambda:click_boton("-"))

boton_par1   = Button(ventana, text = "(", width = 5,height = 2, command = lambda:click_boton("("))
boton_par2   = Button(ventana, text = ")", width = 5,height = 2, command = lambda:click_boton(")"))
boton_punto  = Button(ventana, text = ".", width = 5,height = 2, command = lambda:click_boton("."))
boton_borrar = Button(ventana, text = "AC", width = 5,height = 2, command = lambda:borrar())
boton_igual  = Button(ventana, text = "=", width = 5,height = 2, command = lambda:evaluar())

# ORDENAR BOTONES
boton_borrar.grid (row=1, column=0, padx=5, pady=5)
boton_par1.grid   (row=1, column=1, padx=5, pady=5)
boton_par2.grid   (row=1, column=2, padx=5, pady=5)
boton_multi.grid  (row=1, column=3, padx=5, pady=5)

boton7.grid     (row=2, column=0, padx=5, pady=5)
boton8.grid     (row=2, column=1, padx=5, pady=5)
boton9.grid     (row=2, column=2, padx=5, pady=5)
boton_div.grid  (row=2, column=3, padx=5, pady=5)

boton4.grid      (row=3, column=0, padx=5, pady=5)
boton5.grid      (row=3, column=1, padx=5, pady=5)
boton6.grid      (row=3, column=2, padx=5, pady=5)
boton_suma.grid  (row=3, column=3, padx=5, pady=5)

boton1.grid       (row=4, column=0, padx=5, pady=5)
boton2.grid       (row=4, column=1, padx=5, pady=5)
boton3.grid       (row=4, column=2, padx=5, pady=5)
boton_resta.grid  (row=4, column=3, padx=5, pady=5)

boton0.grid       (row=5, column=0,columnspan = 2, padx=5, pady=5)
boton_punto.grid  (row=5, column=2, padx=5, pady=5)
boton_igual.grid  (row=5, column=3, padx=5, pady=5)

firma = Label(ventana, text="By Malcom Pozo.",background="lightblue")
firma.grid(row=6, column=0,columnspan = 2, padx=5, pady=5)

ventana.mainloop()