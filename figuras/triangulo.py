from figuras.figura import Figura

class Triangulo(Figura):

    def __init__(self):
        super().__init__()
        self.base = 0
        self.altura = 0

    def leer_datos(self):
        super().leer_datos()
        self.base = float(input("Base: "))
        self.altura = float(input("Altura: "))

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Base: {self.base}")
        print(f"Altura: {self.altura}")
        print(f"Área: {self.calcular_area()}")