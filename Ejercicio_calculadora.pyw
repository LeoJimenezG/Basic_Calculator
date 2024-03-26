from tkinter import *

#Creación de raíz
raiz = Tk()
raiz.title("Calculadora")
raiz.resizable(0,0)
raiz.iconbitmap("calculadora.ico")
raiz.config(bg="black")
raiz.geometry("189x210")


#Creación de frame
frame = Frame(raiz)
frame.config(bg = "white")
frame.pack(fill = "both", expand = "True")


operacion = ""
resultado_final = 0.0
r_pantalla = False


relleno1 = Label(frame, text = "")
relleno1.grid(row = 0, column = 4)
relleno1.config(width = 0, height = 2)
relleno2 = Label(frame, text = "")
relleno2.grid(row = 1, column = 4)
relleno2.config(width = 0, height = 2)


#Pantalla de la calculadora
numeros = StringVar()
entrada = Entry(frame, textvariable = numeros, bg = "black", fg = "green", font = ("Arial", 13))
entrada.place(x = 1, y = 1, width = 187, height = 34)
entrada.config(justify = "right")


#Código números
def num_pulsado(num):
    global operacion
    global numeros
    global r_pantalla
   
    if r_pantalla != False:
        numeros.set(num)
        r_pantalla = False
    else:
        numeros.set(numeros.get() + num)


#Código operaciones
def suma(num_p):
    global operacion
    global resultado_final
    global r_pantalla

    resultado_final += float(num_p)
    numeros.set(resultado_final)
    
    operacion = "suma"
    r_pantalla = True

def resta(num_p):
    global operacion
    global resultado_final
    global r_pantalla

    if resultado_final == 0:
        resultado_final += float(num_p)
        numeros.set(resultado_final)
    else:
        resultado_final -= float(num_p)
        numeros.set(resultado_final) 
    
    operacion = "resta"
    r_pantalla = True
 
def division(num_p):
    global operacion
    global resultado_final
    global r_pantalla

    operacion = "division"
    r_pantalla = True
    
    if resultado_final == 0:
        resultado_final += float(num_p)
        numeros.set(resultado_final)

    else:
        resultado_final /= float(num_p)
        numeros.set(resultado_final) 
    
    
def multiplicacion(num_p):
    global operacion
    global resultado_final
    global r_pantalla

    if resultado_final == 0:
        resultado_final += float(num_p)
        numeros.set(resultado_final)
    else:
        resultado_final *= float(num_p)
        numeros.set(resultado_final) 

    operacion = "multiplicacion"
    r_pantalla = True    

def resultadoF(op):
    global operacion
    global resultado_final
    global numeros
    global r_pantalla  
    
    if op == "suma":
        numeros.set(resultado_final + float(numeros.get()))
    elif op == "resta":
        numeros.set(resultado_final - float(numeros.get()))
    elif op == "multiplicacion":
        numeros.set(float(resultado_final) * float(numeros.get()))
    elif op == "division":
        numeros.set(float(resultado_final) / float(numeros.get()))
 
    resultado_final = 0
    r_pantalla = True


#Números y funciones
nueve = Button(frame, text = "9", command = lambda: num_pulsado("9"))
nueve.grid(row = 1, column = 2, padx = 1, pady = 1)
nueve.config(width = 5, height = 2, activebackground = "grey", bg = "lightblue")      

ocho = Button(frame, text = "8", command = lambda: num_pulsado("8"))
ocho.grid(row = 1, column = 1, padx = 1, pady = 1)
ocho.config(width = 5, height = 2, activebackground = "grey", bg = "lightblue")

siete=Button(frame, text = "7", command = lambda: num_pulsado("7"))
siete.grid(row = 1, column = 0, padx = 1, pady = 1)
siete.config(width = 5, height = 2, activebackground = "grey", bg = "lightblue")

seis = Button(frame, text = "6", command = lambda: num_pulsado("6"))
seis.grid(row = 2, column = 2, padx = 1, pady =1)
seis.config(width = 5, height = 2, activebackground = "grey", bg = "lightblue")

cinco = Button(frame, text = "5", command = lambda: num_pulsado("5"))
cinco.grid(row = 2, column = 1, padx = 1, pady = 1)
cinco.config(width = 5, height = 2, activebackground = "grey", bg = "lightblue")

cuatro = Button(frame, text = "4", command = lambda: num_pulsado("4"))
cuatro.grid(row = 2, column = 0, padx = 1, pady = 1)
cuatro.config(width = 5, height = 2, activebackground = "grey", bg = "lightblue")

tres = Button(frame, text = "3", command = lambda: num_pulsado("3"))
tres.grid(row = 3, column = 2, padx = 1, pady = 1)
tres.config(width = 5, height = 2, activebackground = "grey", bg = "lightblue")

dos = Button(frame, text = "2", command = lambda: num_pulsado("2"))
dos.grid(row = 3, column = 1, padx = 1, pady = 1)
dos.config(width = 5, height = 2, activebackground = "grey", bg = "lightblue")

uno = Button(frame, text = "1", command = lambda: num_pulsado("1"))
uno.grid(row = 3, column = 0, padx = 1, pady = 1)
uno.config(width = 5, height = 2, activebackground = "grey", bg = "lightblue")

punto = Button(frame, text = ".", command = lambda: num_pulsado("."))
punto.grid(row = 4, column = 0, padx = 1, pady = 1)
punto.config(width = 5, height = 2, activebackground = "grey", bg = "lightblue")

cero = Button(frame, text = "0", command = lambda: num_pulsado("0"))
cero.grid(row = 4, column = 1, padx = 1, pady = 1)
cero.config(width = 5, height = 2, activebackground = "grey", bg = "lightblue")

restar = Button(frame, text = "-", command = lambda: resta(numeros.get()))
restar.grid(row = 3, column = 3, padx = 1, pady = 1)
restar.config(width = 5, height = 2, bg = "lightgreen", activebackground = "grey")

sumar = Button(frame, text = "+", command = lambda: suma(numeros.get()))
sumar.grid(row = 4, column = 3, padx = 1, pady = 1)
sumar.config(width = 5, height = 2, bg = "lightgreen", activebackground = "grey")

dividir = Button(frame, text = "÷", command = lambda: division(numeros.get()))
dividir.grid(row = 2, column = 3, padx = 1, pady = 1)
dividir.config(width = 5, height = 2, bg = "lightgreen", activebackground = "grey")

multiplicar = Button(frame, text = "x", command = lambda: multiplicacion(numeros.get()))
multiplicar.grid(row = 1, column = 3, padx = 1, pady = 1)
multiplicar.config(width = 5, height = 2, bg = "lightgreen", activebackground = "grey")

resultado = Button(frame, text = "=", command = lambda: resultadoF(operacion))
resultado.grid(row = 4, column = 2, padx = 1, pady = 1)
resultado.config(width = 5, height = 2, bg = "orange", activebackground = "grey")


#Loop de la interfaz
raiz.mainloop()