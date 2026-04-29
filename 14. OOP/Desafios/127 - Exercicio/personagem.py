from abc import ABC, abstractmethod
from random import randint, choice
from rich import print

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.forca  = 0

    def atacar(self, alvo, forca= 0):
        self.forca = forca

        if isinstance(self, Guerreiro):
            golpe = choice(Guerreiro.golpes)
        elif isinstance(self, Mago):
            golpe = choice(Mago.golpes)
        else:
            golpe = "Ataque Básico"

        dano = randint(0, self.forca)
        alvo.receber_dano(dano)

        print(f"[green]{self.nome}[/]([cyan]{self.vida}[/]) atacou [red]{alvo.nome}[/]([cyan]{alvo.vida}[/]) com um {golpe} de forca [cyan]{self.forca}[/]")

        print(f'[blue]{alvo.nome}[/] recebeu [red]{dano} de dano[/]')

        return self.forca


    def receber_dano(self, dano):
        # Calcula força do ataque
        self.vida -= dano
        return self.vida

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    golpes = ['Aram Pesada', 'Macacos me mordam', 'Soca Fofo']

    def __init__(self,nome, vida):
        super().__init__(nome, vida)
        self.cura = 0

    def curar(self, cura=0):
        self.cura = cura

        print(f'{self.nome} Usou poção de cura e curou {randint(0, self.cura)}')

class Mago(Personagem):
    golpes = ['Fire Ball', 'Thunderbolt', 'Ice Spike']

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.cura = 0

    def curar(self, cura=0):
        self.cura = cura

        print(f'{self.nome} Conjurou Cura de {randint(0, self.cura)}')