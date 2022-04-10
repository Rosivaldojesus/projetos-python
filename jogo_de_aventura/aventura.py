# Um jogo de decisões onde eu teri que criar varios finais diferentes baseados nas respostas que forem dadas

# Chegar a finais diferentes na minha historia, de acordo com as respostas que eu passe para o programa

# Cenário: Eu estou em uma guerra entre duas nações, e nós temos 2 lados: LadoA e LadoB. Somente o ladoA irá vencer,
# e o ladoB irá perder! então eu teno que tomar as decisões corretas para chegar até a vitória, que somente o ladoA
# irá conseguir
class JogoDeAventura:
    def __init__(self) -> None:
        self.pergunta1 = 'Você nasceu no norte ou sul ? (n\s)' #norte: LadoA, sul:LadoB
        self.pergunta2 = 'Você prefere a espada ou escudo? (espada/escudo) ' #espada: LadoA, escudo:LadoB
        self.pergunta3 = 'Qual a sua especialidade ? (frente/tatico) ' #linha de frente: LadoA, tático:LadoB

        self.finalHistoria1 =  'Você será um herói na linha de frente!'
        self.finalHistoria2 =  'Você será um herói protegendo todas as nossas tropas!'
        self.finalHistoria3 =  'Você será um herói nas sombras!'
        self.finalHistoria4 =  'Você não é capaz de lutar nessa batalha!'

    def Iniciar(self):
        resposta1 = input(self.pergunta1)
        if resposta1 == 'n':
            resposta1B = input(self.pergunta2)
            if resposta1B == 'espada':
                print(self.finalHistoria1)
            if resposta1B == ' escudo':
                print(self.finalHistoria2)
        if resposta1 == 's':
            resposta1B = input(self.pergunta3)
            if resposta1B == 'frente':
                print(self.finalHistoria3)
            if resposta1B == 'tatico':
                print(self.finalHistoria4)

jogo = JogoDeAventura()
jogo.Iniciar()