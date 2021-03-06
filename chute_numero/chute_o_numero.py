# Criar um algoritimo que gera um valor aleatório e eu tenho que ficar
# tentando até acertar

import random

class ChuteONumero:
    def __init__(self) -> None:
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        try:
            while self.tentar_novamente == True:
                if self.valor_do_chute > self.valor_aleatorio:
                    print('Chute um valor mais baixo!')
                    self.PedirValorAleatorio()
                elif self.valor_do_chute < self.valor_aleatorio:
                    print("Chute um valor mais alto!")
                    self.PedirValorAleatorio()
                elif self.valor_aleatorio == self.valor_do_chute:
                    self.tentar_novamente = False
                    print("Acertou!!!!!")
        except:
            print("Digite apenas número!!!")
            self.Iniciar()

    def PedirValorAleatorio(self):
        self.valor_do_chute = int(input("Chute um número: "))

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

inicio = ChuteONumero()
inicio.Iniciar()