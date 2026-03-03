from figuras.circulo import Circulo
from figuras.triangulo import Triangulo


def menuPrincipal():
    while True:
        print("::Menú")
        print("1. Círculo")
        print("2. Triángulo")
        print("3. Salir")

        op = int(input("Ingrese la opción: "))

        match op:
            case 1:
                c = Circulo()
                c.leer_datos()
                c.mostrar_datos()
                print()

            case 2:
                t = Triangulo()
                t.leer_datos()
                t.mostrar_datos()
                print()

            case 3:
                print("Hasta pronto")
                break

            case _:
                print("Opción inválida")
                print()
