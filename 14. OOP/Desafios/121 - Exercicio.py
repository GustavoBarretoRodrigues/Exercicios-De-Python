# Crie a classe Caneta, que simule o funcionamento de uma caneta colorida,
# podendo escrever frases na cor relativa.

from rich import print

class Caneta:
    def __init__(self, cor = "azul"):
        self.cor = cor
        self.destampada = False
    
    def destampar(self):
        self.destampada = True

    def quebra_linha(self):
        print('\n')
    
    def escrever(self, mensagem):
        if self.destampada:
            if self.cor == "azul":
                print(f"[blue]{mensagem}[/]", end="")
            
            elif self.cor == "vermelho":
                print(f"[red]{mensagem}[/]",end="")
            
            elif self.cor == "verde":
                print(f"[green]{mensagem}[/]",end="")
        else:
            print('Caneta esta tampada!')


c1 = Caneta('azul')
c2 = Caneta('vermelho')
c3 = Caneta('verde')

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever('Olá, Tudo bem? ')
c1.quebra_linha()
c2.escrever('Olá, consagrado! ')
c3.escrever('Vem sempre aqui? ')