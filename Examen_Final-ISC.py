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

    #2. Horas vividas
    def funcion2(self):   
        dia=int(self.pp3.get())
        mes=int(self.pes4.get())
        anio=int(self.pap5.get())
        fecha_de_nacimiento = datetime.datetime(anio, mes, dia)
        fecha_de_hoy = datetime.datetime.now()
        dias_vividos = fecha_de_hoy - fecha_de_nacimiento
        horas = dias_vividos * 24
        horas_vividas = horas.days
        self.message['text'] = 'Naciste el: {}/{}/{}, en total has vivido {} horas'.format(dia,mes,anio,horas_vividas)   
    #3. Nombre y apellido pares o impares
    def funcion3(self):
        nom=str(self.p1.get())
        apel=str(self.op2.get())
        nr_nombre=int(len(nom))
        nr_apellido=int(len(apel))
        if nr_nombre%2==0 and nr_apellido %2==0 :
            self.message['text'] = '{} {}, tu nombre es par y tu apellido es par'.format(nom,apel)
        elif nr_nombre%2==0 and nr_apellido %2==1:
            self.message['text'] = '{} {}, tu nombre es par y tu apellido es impar'.format(nom,apel)
        elif nr_nombre%2==1 and nr_apellido %2==0:
            self.message['text'] = '{} {}, tu nombre es impar y tu apellido es par'.format(nom,apel)
        else:
            self.message['text'] = '{} {}, tu nombre es impar y tu apellido es impar'.format(nom,apel)   
    #4. Vocales y consonantes en el nombre y apellido
    def funcion4(self):
        nr=str(self.p1.get())
        apd=str(self.op2.get())
        cuenta = 0
        for carac in nr:
            if carac == 'a' or carac =='A' or carac =='e' or carac =='E' or carac =='i' or carac=='I' or carac=='o' or carac=="O" or carac=="u" or carac=="U":
                cuenta += 1
        for carac in apd:
            if carac == 'a' or carac =='A' or carac =='e' or carac =='E' or carac =='i' or carac=='I' or carac=='o' or carac=="O" or carac=="u" or carac=="U":
                cuenta += 1
        cud=len(nr)
        cudd=len(apd)
        consonante=cud+cudd-cuenta
        self.message['text'] = 'Tu nombre y apellido tienen {} vocales y {} consonantes'.format(cuenta,consonante)
        #5.Nombre y apellido al reves
    def funcion5(self):
        ns=str(self.p1.get())
        ad=str(self.op2.get())
        cadena_invertida = ""
        cadena_invertida1= ""
        for letra in ns:
            cadena_invertida = letra + cadena_invertida
        for letra1 in ad:
            cadena_invertida1 = letra1 + cadena_invertida1
        self.message['text'] = '{} {}, al reves es: {} {}'.format(ns,ad,cadena_invertida,cadena_invertida1)
if __name__ == '__main__':
    window = Tk()
    app = Desk(window)
    window.mainloop()