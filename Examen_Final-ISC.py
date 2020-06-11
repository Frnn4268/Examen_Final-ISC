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