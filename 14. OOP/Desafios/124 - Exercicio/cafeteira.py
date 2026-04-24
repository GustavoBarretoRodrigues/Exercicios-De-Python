from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def __init__(self):
        pass
    def preparar(self):
        print('--- iniciando o Preparo ---')
        print(f'{self.ferver_agua()}\n{self.misturar()}\n{self.servir()}')
        print('--- Bebida Pronta ---')

    def ferver_agua(self):
        return f'1. Fervendo água a 100 graus Celsius.'

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        return f"2. Passando água pressuriazada pelo pó de café moído."

    def servir(self):
        return f"3.Servindo em xícara pequena."


class Cha(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        return f'2. Mergulhando o sache de ervas na agua'

    def servir(self):
        return f'3. Servindo na canela de porcelana com limão'


class Leite(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        return f'2. Passando vapor pressurizado pelo bico co leite.'

    def servir(self):
        return f'3. Servindo na caneca grande, já com café.'