import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('HP:',size=(15,0)),sg.Text('MANA:',size=(15,0))],
            [sg.Text('IMAGEM')],
            [sg.Text('CENA',size=(15,0))],
            [sg.Button('Ação1',size=(15,0)),sg.Button('Ação2',size=(15,0))],
            [sg.Button('Inventário',size=(15,0)),sg.Button('Status',size=(15,0))],
        ]
        #janela
        janela = sg.Window('Game').layout(layout)

        #extrair os dados da tela
        self.button, self.values = janela.Read()
    
    def Iniciar(self):
        print(self.values)

tela = TelaPython()
tela.Iniciar()