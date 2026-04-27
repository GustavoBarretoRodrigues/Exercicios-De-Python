# Crie a classe Gamer, onde podemos cadastrar nome, nick e os jogos favoritos de uma pessoa.
# Crie também um metodo que permita mostrar a ficha desse gamer.

from rich import print
from rich.panel import Panel


class Gamer:
    def __init__(self, name, nick):
        self.name = name
        self.nick = nick
        self.games = list()
    
    def add_favorite(self, name_game):
        self.games.append(name_game)
        self.games.sort()

        return self.games

    def card(self):
        games_format = "\n".join(f"[green]🎮 {game}[/]" for game in self.games)

        conteudo = (
            f"[bold]Nome Real:[/] [red]{self.name}[/]\n\n"
            f"[bold]Jogos favoritos:[/]\n{games_format}"
        )

        game_sheet = Panel(
            conteudo, 
            title=f"[cyan]Jogador <{self.nick}>[/]",
            border_style='blue',
            width=40)

        print(game_sheet)
    
g1 = Gamer('Gustavo', 'ZarGonk')

g1.add_favorite('Terraria')
g1.add_favorite('Ark Survivel Evolved')
g1.add_favorite('Fallout New Vegas')
g1.add_favorite('Sniper Elite')

g1.card()