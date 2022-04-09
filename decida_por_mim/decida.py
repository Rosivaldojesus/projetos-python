# Faça uma pergunta para o programa e ele terá que te dar uma resposta
import random

class DecidaPorMin():
    def __init__(self) -> None:
        self.resposta = [
            'Com certeza, você deve fazer isso!',
            'Não sei, você que sabe',
            'Não faça isso!',
            'Acho que tá na hora certa!'
        ]

    def Iniciar(self):
        input('Faça sua pergunta: ')
        print(random.choice(self.resposta))

decida = DecidaPorMin()
decida.Iniciar()