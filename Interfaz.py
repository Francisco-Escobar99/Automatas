from tkinter import messagebox as mb
from email.mime import image
import tkinter as tk
import pandas as pd
import re

class Interfaz:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Pagos y Depositos")
        self.ventana.geometry("1000x600")
        self.ventana.config(background="#FFFDE2")
        
        self.labelTitulo=tk.Label(self.ventana, text="Pagos y Depositos", width=68, height=2, background="#DE2324", foreground="#FFFFFF", font=("Tahoma", 22,)).place(x=0,y=45)
        imagen=tk.PhotoImage(file="Logo.png")
        etiqueta=tk.Label(image=imagen, width=266, height=136)
        etiqueta.place(x=70, y=13)

        self.labelSubTitulo=tk.Label(self.ventana, text="Clabe Interbancaria:", background="#FFFDE2", foreground="#DE2324", font=("Arial", 18)).place(x=150,y=200)
        self.CajaTexto=tk.Entry(self.ventana, highlightbackground="#DE2324",highlightthickness = 1, bd=0, font=("Arial", 13))
        self.CajaTexto.place(x=380,y=201,width=315, height=36)
        self.btn=tk.Button(self.ventana, text="Verificar", command=lambda:condicion() ,background="#DE2324", foreground="#FCF9F9", font=("Arial", 14))
        self.btn.place(x=710,y=201, width=150, height=30)
        
        self.labelTitulo2=tk.Label(self.ventana, text="Informacion General", width=64, height=1,  background="#DE2324", foreground="#FFFFFF", font=("Arial", 15,)).place(x=150,y=300)
        self.cuadro=tk.Entry(self.ventana, background="#FFFDE2", highlightbackground="#DE2324",highlightthickness = 1, bd=0).place(x=150,y=329, width=709, height=180)
        self.labelSubTitulo2=tk.Label(self.ventana, text="Numero de Cuenta:", background="#FFFDE2", foreground="#B80203", font=("Arial", 18)).place(x=200,y=350)
        self.labelSubTitulo3=tk.Label(self.ventana, text="Región:", background="#FFFDE2", foreground="#B80203", font=("Arial", 18)).place(x=200,y=400)
        self.labelSubTitulo4=tk.Label(self.ventana, text="Banco:", background="#FFFDE2", foreground="#B80203", font=("Arial", 18)).place(x=200,y=450)

        def condicion():
            if len(self.CajaTexto.get()) == 0:
                mb.showwarning('Advertencia', 'Campo Vacio')
            elif len(self.CajaTexto.get()) > 18 or len(self.CajaTexto.get()) < 18:
                mb.showerror('Error', 'La Cadena Ingresada No Cumple Con Los 18 Digitos')
            else:
                clabe = str(self.CajaTexto.get())
                self.verificarExpresion(clabe)
         
        self.ventana.mainloop()
    
    def verificarExpresion(self, nva_cadena):
        expresionClabe = ('^[0|1|6]{1}[1-7]{1}[1|2|4|6-9]{1}[0-9]{3}[0-9]{11}[0-9]{1}$')
        evaluar = re.compile(expresionClabe)

        if evaluar.search(nva_cadena):
            mb.showinfo('Correcto', 'Clabe Interbancaria Ingresada Valida')
            self.verificarDatos(nva_cadena)
        else:
            mb.showerror('Error', 'Clabe Interbancaria Ingresada NO Valida')
    
    def verificarDatos(self, clabe):
        num_banco = ['012','014','044','036','021','137','677','059','062','058','128']
        bancos = ['Bancomer','Santander','Scotianbank','Inbursa', 'HBSC', 'BanCoppel', 
                'Caja Popular Mexicana', 'Invex', 'Afirme', 'BanRegio', 'Banco Autofin']

        archivo = pd.read_csv('plaza_codigo.csv', header=0)
        plaza = pd.DataFrame(archivo)
        num_Plaza = list(plaza['plaza'])
        nombre_Plaza = list(plaza['nombre'])

        clabe = list(clabe)
        print(clabe)

        cod_banco = []
        cod_plaza = []
        num_cuenta = []
        dig_control = []

        cod_banco.append(''.join(clabe[0:3]))
        cod_plaza.append(''.join(clabe[3:6]))
        num_cuenta.append(''.join(clabe[6:17]))
        dig_control.append(''.join(clabe[17]))

        cod_banco = ''.join(cod_banco)
        cod_plaza = ''.join(cod_plaza)
        num_cuenta = ''.join(num_cuenta)
        dig_control = ''.join(dig_control)

        
        if cod_banco in num_banco:
            posicionBanco = num_banco.index(cod_banco)
            print('Numero de Banco: ', num_banco[posicionBanco], '\nNombre del Banco: ', bancos[posicionBanco])

            if int(cod_plaza) in num_Plaza:
                posicionPlaza = num_Plaza.index(int(cod_plaza))
                print('Numero de Plaza: ',num_Plaza[posicionPlaza], '\nNombre de la Plaza: ', nombre_Plaza[posicionPlaza])
                print('Numero de Cuenta: ', num_cuenta, '\nDigito de Control: ', dig_control)

                tk.Label(self.ventana, text=(num_cuenta), background="#FFFDE2", foreground="#B80203", font=("Arial", 18)).place(x=430,y=350)
                tk.Label(self.ventana, text=(nombre_Plaza[posicionPlaza]), background="#FFFDE2", foreground="#B80203", font=("Arial", 18)).place(x=300,y=400)
                tk.Label(self.ventana, text=(bancos[posicionBanco]), background="#FFFDE2", foreground="#B80203", font=("Arial", 18)).place(x=300,y=450)

            else:
                mb.showerror('Error','La Clabe Interbancaria Ingresada, No Permite Depositos/Pagos')
        else:
            mb.showerror('Error','La Clabe Interbancaria Ingresada, No Permite Depositos/Pagos')

Inicio=Interfaz()