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