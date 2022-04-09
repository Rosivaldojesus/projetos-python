# Simuladro de dado
# Simular o uso de um dados, gerando umvalor de 1 até 6

import random
import PySimpleGUI
import PySimpleGUI as sg

class SimuladadorDado:
    def __init__(self) -> None:
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor?: '
        #layout da tela 
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'), sg.Button('Não')]
        ]
       
    def iniciar(self):
    
        # criar Janela
        self.janela = sg.Window('Simuladro de dados', layout=self.layout)

        # ler o valores da tela 
        self.eventos,  self.valores = self.janela.Read()
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos ==  'não' or self.eventos == 'n':
                print('Agradeçemos a sua participação!')
            else:
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber a sua resposta!')        
            

    def GerarValorDoDado(self):
        print(f'Valor =>>: {random.randint(self.valor_minimo, self.valor_maximo)}')

simulador = SimuladadorDado()
simulador.iniciar()