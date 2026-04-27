# Exercicio 117 - Crie a classe  Produto, onde podemos cadastrar nome e o preço.
# Crie também um metodo que mostre uma etiqueta de preço do produto.
from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def etiqueta(self):
        larg = 26
        conteudo = (
            f"{self.name.center(larg)}\n"
            f"{('-'*larg)}\n"
            f"{('R$ ' + f'{self.value:,.2f}').center(larg, '.')}")

        
        etiqueta = Panel(
            conteudo,
            title="Produto",
            width=30
        )
        print(etiqueta)


p1 = Produto('iPhone 17 Pro Max', 25_000.85)
p1.etiqueta()

p2 = Produto("Laptop Gamer", 8_000.00)
p2.etiqueta()