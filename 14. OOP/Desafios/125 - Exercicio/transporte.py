from abc import ABC, abstractmethod
from rich.table import Table


class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):
    fator = 0.50
    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        self.frete = self.distancia * self.fator
        return f'R$ {self.frete:.2f}'


class Caminhao(Transporte):
    fator = 1.20

    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.distancia < 50:
            return f'Distancia minima de 50km'
        else:
            self.frete = self.distancia * self.fator
            return f'R$ {self.frete:.2f}'



class Drone(Transporte):
    fator = 9.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.distancia > 10:
            return f'Distancia maxima de 10km'
        else:
            self.frete = self.distancia * self.fator
            return f'R$ {self.frete:.2f}'
