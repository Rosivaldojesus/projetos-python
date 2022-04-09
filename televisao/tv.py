class Televisao():

    def __init__(self) -> None:
        self.ligada = False
        self.canal = 2
    
    def muda_canal_para_baixo(self):
        self.canal -= 1
    
    def muda_canal_para_cima(self):
        self.canal += 1

if __name__ == '__main__':
    tv = Televisao()
    print('Canal Inicial: ', tv.canal)
    print('Ligada: ', tv.ligada)

    tv.ligada = True
    tv.canal = 5

    print('Canal: ', tv.canal)
    print('Ligada: ', tv.ligada)
    tv.muda_canal_para_cima()
    print('Canal: ', tv.canal)
    tv.muda_canal_para_cima()
    print('Canal: ', tv.canal)
    tv.muda_canal_para_baixo()
    print('Canal: ', tv.canal)
    tv.muda_canal_para_baixo()
    print('Canal: ', tv.canal)
    tv.muda_canal_para_baixo()
    print('Canal: ', tv.canal)
    tv.muda_canal_para_baixo()
    print('Canal: ', tv.canal)

