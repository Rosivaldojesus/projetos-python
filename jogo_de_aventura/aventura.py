# Um jogo de decisões onde eu teri que criar varios finais diferentes baseados nas respostas que forem dadas

# Chegar a finais diferentes na minha historia, de acordo com as respostas que eu passe para o programa

# Cenário: Eu estou em uma guerra entre duas nações, e nós temos 2 lados: LadoA e LadoB. Somente o ladoA irá vencer,
# e o ladoB irá perder! então eu teno que tomar as decisões corretas para chegar até a vitória, que somente o ladoA
# irá conseguir
class JogoDeAventura:
    def __init__(self) -> None:
        self.perguntas ={
             'p1':'Você nasceu no norte ou sul ? (n\s) ', #norte: LadoA, sul:LadoB
             's':'Qual a sua especialidade ? (frente/tatico) ', #espada: LadoA, escudo:LadoB
             'n':'Você prefere a espada ou escudo? (espada/escudo) ' #linha de frente: LadoA, tático:LadoB
        }
        self.respostas ={
             'n+espada':'Você será um herói na linha de frente!',
             'n+escudo':'Você será um herói protegendo todas as nossas tropas!',
             's+frente':'Você será um herói nas sombras!',
             's+tatico':'Você não é capaz de lutar nessa batalha!'
             }

    def Iniciar(self):
        resposta1= input(self.perguntas['p1']).lower()
        if resposta1 in ('s','n'):
        	resposta = input(self.perguntas[resposta1])
        	print(self.respostas[f'{resposta1}+{resposta}'])

jogo = JogoDeAventura()
jogo.Iniciar() 
