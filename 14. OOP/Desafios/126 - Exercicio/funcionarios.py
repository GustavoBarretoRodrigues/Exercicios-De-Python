from abc import ABC, abstractmethod
from rich.console import Console
from rich.panel import Panel

console = Console(force_terminal=True, color_system="truecolor")
class Funcionario(ABC):
    salario_min = 1612
    inss = 7.5

    def __init__(self, nome, salario_bruto, salario):
        self.nome = nome
        self.salario_bruto = salario_bruto
        self.salario = salario

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        conteudo = f"O salario de [bold blue]{self.nome}[/] é de [bold green]R$ {self.salario:.2f}[/] e corresponde a [bold yellow]{(self.salario / self.salario_min):.1f}salários mínimos.[/]"

        painel = Panel(conteudo, title="[bold]Análise de Salário[/]", expand=False)

        console.print(painel)

class Horista(Funcionario):
    def __init__(self, nome, valor_hora, qnd_horas):
        super().__init__(nome, salario_bruto=0, salario=0)
        self.valor_bruto = valor_hora
        self.qnd_horas = qnd_horas

    def calc_sal(self):
        self.salario_bruto = self.valor_bruto * self.qnd_horas
        self.salario = self.salario_bruto- (self.salario_bruto * (7.5 / 100))
        return self.salario


class Mensalista(Funcionario):
    def __init__(self, nome, salario_bruto):
        super().__init__(nome, salario_bruto, salario=0)


    def calc_sal(self):
        self.salario = self.salario_bruto - (self.salario_bruto * (7.5 / 100))
        return self.salario
