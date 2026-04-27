# Exercicio 116 - Crie a classe Funcionário, onde podemos cadastrar nome, setor e cargo.
# Crie também um metodo que permite ao funcionário se apresentar .

from rich import print

class Funcionario:
    empresa = "Curso em Video"
    
    def __init__(self, name='Guests', sector='Mendigo', position='Desempregado'):
        self.name       = name
        self.sector     = sector
        self.position   = position
    
    def apresentação(self):
        return f'Olá, sou [blue]{self.name}[/] e sou [blue]{self.position}[/] do setor de [green]{self.sector}[/] da empresa {Funcionario.empresa}'


c1 = Funcionario("Maria", "Administração", "Diretora")
print(c1.apresentação())

c2 = Funcionario("Pedro", "TI", "Programador")
print(c2.apresentação())