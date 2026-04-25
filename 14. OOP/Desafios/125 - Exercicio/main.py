from rich.table import Table
from rich.console import Console
from transporte import *

def main():
    dist = 100

    entrega = Drone(dist)
    #print(f'Frete de {type(entrega).__name__} em {dist}km = {entrega.calc_frete()}')

    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]


    console = Console()
    table = Table(title='Tabela de Frete')

    table.add_column('Transporte', style='Cyan', no_wrap=True)
    table.add_column('Distancia', style='Magenta')
    table.add_column('Frete', style='Green')

    for i in viagem:
        table.add_row(f'{type(i).__name__}', f'{dist}km', f'{i.calc_frete()}')

    console.print(table)


if __name__ == '__main__':
    main()
