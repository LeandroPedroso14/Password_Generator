import random
import PySimpleGUI as sg
import os


class PassGen:

    def __init__(self):
       # Layout
        sg.theme('Black')
        layout = [
            [sg.Text('Plataforma', size=(10, 1)),
             sg.Input(key='Sistema', size=(20, 1))],
            [sg.Text('E-mail', size=(10, 1)),
             sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres'),
             sg.Combo(values=list(range(30)), key='total_chars', default_value=1, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar senha')],
        ]
        # Declarar Janela
        self.janela = sg.Window('Password Generator', layout)

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)

    def gerar_senha(self, valores):
        char_list = 'ABCDEFGHIJLMNOPQRSTUVXZKWYabcdefghijklmnopqrstuvxzkwy1234567890!@#$%"&*'

    def salvar_senha(self):
        pass


gen = PassGen()
gen.Iniciar()
