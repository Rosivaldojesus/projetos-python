# Criar um algoritimo que gera um valor aleatório e eu tenho que ficar
# tentando até acertar

import random
import PySimpleGUI as sg

class ChuteONumero:
    def __init__(self) -> None:
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
         # layout
        self.layout = [
            [sg.Text('Seu chute', size=(20,0))],
            [sg.Input(size=(18,0), key='ValorChute')],
            [sg.Button('Chutar')],
            [sg.Output(size=(20,10))]
        ]
        # Criar uma janela
        self.janela = sg.Window("Chute o número!", layout=self.layout)
        self.GerarNumeroAleatorio()
        try:
            while True:
                # receber valores
                self.evento, self.valores = self.janela.Read()
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valores['valorChute']
                    while self.tentar_novamente == True:
                        if self.valor_do_chute > self.valor_aleatorio:
                            print('Chute um valor mais baixo!')
                            break
                        elif self.valor_do_chute < self.valor_aleatorio:
                            print("Chute um valor mais alto!")
                            break
                        elif self.valor_aleatorio == self.valor_do_chute:
                            self.tentar_novamente = False
                            print("Acertou!!!!!")
                            break
        except:
            print("Digite apenas número!!!")
            self.Iniciar()
    
    def LervaloresDaTela(self):
        self.evento, self.valores = self.janela.Read()

    def PedirValorAleatorio(self):
        self.valor_do_chute = int(input("Chute um número: "))

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

inicio = ChuteONumero()
inicio.Iniciar()