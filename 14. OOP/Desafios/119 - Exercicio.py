# Exercicio 119 - Crie a classe Livro, que vai simular a passagem de páginas de um livro,
# considerando também se o usuário chegou ao fim da leitura.

from time import sleep
from rich import print


class Livro:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
        self.current_page = 1
        self.book = False

    def open_book(self) -> None:
        self.book = True

        print(f":book:[blue] Você acabou de abrir o livro [red]'{self.title}'[/] que tem [green]{self.pages}[/] no total. Você agora está na [yellow]{self.current_page}[/]")

    def avancar_paginas(self, value=1):
        if self.book:
            if self.current_page == self.pages:
                print(f":rotating_light:[red]Você terminou o livro!'{self.title}'[/]")

            count = 0
            for _ in range(value):
                if self.current_page < self.pages:
                    sleep(.3)
                    self.current_page += 1
                    count += 1
                    print(f'Pág{self.current_page} :right_arrow:  ', end='', flush=True)
                else:
                    break

            print(f"[blue]Você avançou {count} páginas e agora está na [yellow]página {self.current_page}[/]")

            if self.current_page == self.pages:
                print(f":rotating_light:[red]Você chegou ao final do livro '{self.title}'[/]")
        else: print(f"📘 É necessario abrir o livro para ler")

l1 = Livro('Magico de OS', 20)
l1.open_book()
l1.avancar_paginas(5)
l1.avancar_paginas(10)