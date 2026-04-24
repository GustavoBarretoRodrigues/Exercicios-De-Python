from abc import  ABC, abstractmethod
from math import pi

class Poligono(ABC):
    def __init__(self, qtd_lado):
        self.qtd_lado = qtd_lado

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(qtd_lado=4)
        self.lado = lado

    def perimetro(self):
        """Calcula o perimetro de um quadrado"""
        return  self.qtd_lado * self.lado

    def area(self):
        """Calcula a area de um quadrado"""
        return self.lado ** 2


class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(qtd_lado=0 )
        self.raio = raio

    def perimetro(self):
        """Calcula o perimetro de um circulo"""
        return 2 * pi *self.raio

    def area(self):
        """Calcula a area de um circulo"""
        return pi * (self.raio ** 2)