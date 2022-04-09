# Simuladro de dado
# Simular o uso de um dados, gerando umvalor de 1 até 6

from logging import exception
import random



class SimuladadorDado:
    def __init__(self) -> None:
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor?: '

    def iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 'sim' or resposta == 's':
                self.GerarValorDoDado()
            elif resposta ==  'não' or resposta == 'n':
                print('Agradeçemos a sua participação!')
                
            else:
                print('Favor digitar sim ou não')

        except exception:
            print('Ocorreu um erro ao receber a sua resposta!')


    def GerarValorDoDado(self):
        print(f'Valor =>>: {random.randint(self.valor_minimo, self.valor_maximo)}')

simulador = SimuladadorDado()
simulador.iniciar()