import os
os.system("cls")

from math import pi
from turtle import *

class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        self.area = pi * self.radio ** 2
        return self.area

    def perimetro(self):
        self.perimetro = 2 * pi * self.radio
        return self.perimetro

    def dibujar_circulo(self):
        dibujo = Turtle()
        dibujo.begin_fill()
        dibujo.circle(ingresar_radio)
        dibujo.color("black", "blue")
        dibujo.end_fill()
        return dibujo

    def dibujar_circulo_multiplicado(self):
        dibujo = Turtle()
        dibujo.begin_fill()
        dibujo.circle(ingresar_radio * n)
        dibujo.color("black", "red")
        dibujo.end_fill()
        return dibujo

respuesta = str(input("》¿Desea realizar un circulo?: "))
print()

while True:
    if (respuesta.lower() == "no"):
        print("¡Hasta pronto!")
        print()
        break

    elif (respuesta.lower() == "si"):
        try:
            ingresar_radio = int(input("》Ingrese el radio del circulo: "))
        except ValueError:
            print("\n¤ Se ingreso un valor no correspondiente. Ingrese un número. \n")
            continue

        if(ingresar_radio > 0):
            crear_circulo = Circulo(ingresar_radio)
            print(f"\n• El area del circulo es: {crear_circulo.area()}")
            print(f"\n• El perimetro del circulo es:{crear_circulo.perimetro()}")
            print("\n• El dibujo se abre en una nueva ventana. \n")
            Circulo.dibujar_circulo(ingresar_radio)

            multiplicar_circulo = input("》¿Desea multiplicar el radio del circulo?: ")

            if(multiplicar_circulo.lower() == "si"):
                n = int(input("》¿Cuantas veces desea multiplicar el radio?: "))
                Circulo.dibujar_circulo_multiplicado(ingresar_radio * n)
                respuesta = str(input("\n》¿Desea realizar otro circulo?: "))
                print()
                continue
            else:
                respuesta = str(input("\n》¿Desea realizar otro circulo?: "))
                print()

        else:
            print("¤ El radio que ingreso esta afuera de rango.")
            break

    else:
        print("¤ Error, responda 'SI' o 'NO'.")
        print()
        respuesta = str(input("》¿Desea realizar un circulo?: "))
        print()
