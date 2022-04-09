# Faça uma pergunta para o programa e ele terá que te dar uma resposta
import random
import PySimpleGUI as sg

class DecidaPorMin():
    def __init__(self) -> None:
        self.resposta = [
            'Com certeza, você deve fazer isso!',
            'Não sei, você que sabe',
            'Não faça isso!',
            'Acho que tá na hora certa!'
        ]

    def Iniciar(self):
        # layout
        layout = [
            [sg.Text('Faça sua pergunta:')],
            [sg.Input()],
            [sg.Output(size=(20,10))],
            [sg.Button('Decida por min')]
        ]
        while True:
            # criar a janela
            self.janela = sg.Window('Decida por min!', layout=layout)
            # Ler os dados
            self.eventos, self.valores = self.janela.Read()
            # Fzaer algo com os valores
            if self.eventos == 'Decida por mim':
                print(random.choice(self.resposta))
            

decida = DecidaPorMin()
decida.Iniciar()