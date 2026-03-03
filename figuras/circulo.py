from figuras.figura import Figura
import math

class Circulo(Figura):

    def __init__(self):
        super().__init__()
        self.radio = 0

    def leer_datos(self):
        super().leer_datos()
        self.radio = float(input("Radio: "))

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Radio: {self.radio}")
        print(f"Área: {round(self.calcular_area(),2)}")