from tkinter import messagebox as mb
from email.mime import image
import tkinter as tk
import pandas as pd
import re

class Interfaz:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Pagos y Depositos")
        self.ventana.geometry("1080x670")
        self.ventana.config(background="#FFFDE2")
        
        self.labelTitulo=tk.Label(self.ventana, text="Pagos y Depositos", width=68, height=2, background="#DE2324", foreground="#FFFFFF", font=("Tahoma", 22,)).place(x=0,y=45)
        imagen=tk.PhotoImage(file="Logo.png")
        etiqueta=tk.Label(image=imagen, width=266, height=136)
        etiqueta.place(x=70, y=13)

        self.labelSubTitulo=tk.Label(self.ventana, text="Clabe Interbancaria:", background="#FFFDE2", foreground="#DE2324", font=("Arial", 18)).place(x=190,y=200)
        self.CajaTexto=tk.Entry(self.ventana, highlightbackground="#DE2324",highlightthickness = 1, bd=0)
        self.CajaTexto.place(x=419,y=201,width=306, height=30)
        self.btn=tk.Button(self.ventana, text="Verificar", command=lambda:condicion() ,background="#DE2324", foreground="#FCF9F9", font=("Arial", 15))
        self.btn.place(x=746,y=201, width=120, height=30)
        
        self.labelTitulo2=tk.Label(self.ventana, text="Informacion General", width=59, height=1,  background="#DE2324", foreground="#FFFFFF", font=("Arial", 15,)).place(x=200,y=340)
        self.cuadro=tk.Entry(self.ventana, background="#FFFDE2", highlightbackground="#DE2324",highlightthickness = 1, bd=0).place(x=200,y=369, width=655, height=244)
        self.labelSubTitulo2=tk.Label(self.ventana, text="Numero de Cuenta:", background="#FFFDE2", foreground="#B80203", font=("Arial", 18)).place(x=215,y=400)
        self.labelSubTitulo3=tk.Label(self.ventana, text="Región:", background="#FFFDE2", foreground="#B80203", font=("Arial", 18)).place(x=215,y=450)
        self.labelSubTitulo4=tk.Label(self.ventana, text="Banco:", background="#FFFDE2", foreground="#B80203", font=("Arial", 18)).place(x=215,y=500)

        def condicion():
            if len(self.CajaTexto.get()) == 0:
                mb.showerror('Error', 'Campo Vacio')
            elif len(self.CajaTexto.get()) > 18 or len(self.CajaTexto.get()) < 18:
                mb.showerror('Error', 'La Cadena Ingresada No Cumple Con Los 18 Digitos')
            else:
                clabe = str(self.CajaTexto.get())
                print(clabe)
                self.verificarExpresion(clabe)
         
        self.ventana.mainloop()
    
    def verificarExpresion(self, nva_cadena):
        expresionClabe = ('^[0|1|6]{1}[1-7]{1}[1|2|4|6-9]{1}[0-9]{3}[0-9]{11}[0-9]{1}$')
        evaluar = re.compile(expresionClabe)

        if evaluar.search(nva_cadena):
            mb.showinfo('Correcto', 'Cadena Correcta')
            self.verificarBanco(nva_cadena)
        else:
            mb.showerror('Error', 'Incorrecto')
    
    def verificarBanco(self, clabe):

        num_banco = ['012','014','044','036','021','137','677','059','062','058','128']
        bancos = ['Bancomer','Santander','Scotianbank','Inbursa', 'HBSC', 'BanCoppel', 
                'Caja Popular Mexicana', 'Invex', 'Afirme', 'BanRegio', 'Banco Autofin']
        
       

        


Inicio=Interfaz()