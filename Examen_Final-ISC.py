#Import del tkinter
from tkinter import ttk
from tkinter import *
import math
import datetime
class Desk:
    def __init__(self, window,):
#Ventana del programa
        anc = 350
        alt = 225
        self.wind = window
        self.wind.geometry(str(anc)+'x'+str(alt))
        #Titulo del programa
        self.wind.columnconfigure(0, weight=1)
        self.wind.title('Examen Final')
        #Titulo de entrada
        frame = LabelFrame(self.wind, text = 'BIENVENIDO')
        frame.grid(row = 0, column = 2, columnspan = 20, pady = 20)
        #Nombre
        Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
        self.p1 = Entry(frame)
        self.p1.focus()
        self.p1.grid(row = 1, columnspan = 6)
        #Apellido
        Label(frame, text = 'Apellido: ').grid(row = 2, column = 0)
        self.op2 = Entry(frame)
        self.op2.grid(row = 2, columnspan = 6)
        #Dia
        Label(frame, text = 'Día: ').grid(row = 3, column = 0)
        self.pp3 = Entry(frame)
        self.pp3.grid(row = 3, columnspan = 6)
        #Mes
        Label(frame, text = 'Mes: ').grid(row = 4, column = 0)
        self.pes4 = Entry(frame)
        self.pes4.grid(row = 4, columnspan = 6)
        #Año
        Label(frame, text = 'Año: ').grid(row = 5, column = 0)
        self.pap5 = Entry(frame)
        self.pap5.grid(row = 5, columnspan = 6)
        #Botones y colocacion
        Button(frame, text = 'Función 1', command = self.funcion1).grid(row = 6, column = 0 , sticky = W + E)
        Button(frame, text = 'Función 2', command = self.funcion2).grid(row = 6, column = 1 , sticky = W + E)
        Button(frame, text = 'Función 3', command = self.funcion3).grid(row = 6, column = 2 , sticky = W + E)
        Button(frame, text = 'Función 4', command = self.funcion4).grid(row = 6, column = 3 , sticky = W + E)
        Button(frame, text = 'Función 5', command = self.funcion5).grid(row = 6, column = 4 , sticky = W + E)
        #Resutado 
        self.message = Label(text = '', fg = 'Black')
        self.message.grid(row = 3, column = 1, columnspan = 2, sticky = W + E)

#1. Letras a numeros Hexadecimales
    def funcion1(self):
        dia=int(self.pp3.get())
        mes=int(self.pes4.get())
        anio=int(self.pap5.get())
        hexdia=format(dia, '0x')
        hexmes=format(mes, '0x')
        hexanio=format(anio, '0x')
        self.message['text'] = 'Su fecha de nacimiento: {}/{}/{}, en Hexadecimal es: {}/{}/{}'.format(dia,mes,anio,hexdia,hexmes,hexanio)       