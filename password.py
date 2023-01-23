import random
import PySimpleGUI as sg
import os 

class PassGen:
   def __init__(self):
      sg.theme('Black')
      layout = [
          [sg.Text('Login',size=(10,1)),
           sg.Input(key='site', size=(20,1))],
          [sg.Text('E-mail',size=(10,1)),
           sg.Input(key='usuario', size=(20,1))],
          [sg.Text('Quantidade de caracteres'),
           sg.Combo(values=list(range(30)))],

   def Iniciar(self):
      pass
   def salvar_senha(self):
      pass

gen = PassGen()
gen.Iniciar()