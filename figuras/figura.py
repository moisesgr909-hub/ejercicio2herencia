class Figura(object):
    def __init__(self):
        self.nombre = ""
        self.color = ""

    def leer_datos(self):
        self.nombre = input("Forma: ")
        self.color = input("Color: ")

    def mostrar_datos(self):
        print(f"Forma: {self.nombre}")
        print(f"Color: {self.color}")