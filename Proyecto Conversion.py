# Calculadora que convierte unidades :)
import math

def millas_kilometros(x):
    print("Aqui tiene sus kilometros", x*1.609)

millas_kilometros(10)

def celsius_fahrenheit(x):
    print(("Aqui tiene sus grados fahrenheit", x*1.8 +32))

celsius_fahrenheit(15)

def fahrenheit_celsius(x):
    print(("Aquí tiene sus grados celsius", (x-32/1.8)))
fahrenheit_celsius(10)

def kilometros_millas(x):
    print("Aqui tiene sus millas", x*.62)
kilometros_millas(20)

def celsius_kelvin(x):
    print("Aqui tiene sus grados kelvin", x+273.15)
celsius_kelvin(10)

def kelvin_celsius(x):
    print("Aqui tiene sus grados celsius", x-273.15)
kelvin_celsius(10)

def metros_pies(x):
    print("Aqui tiene sus pies", x*3.2808)
metros_pies(10)

def pies_metros(x):
    print ("Aquí tiene sus metros", x/3.2808)
pies_metros(10)




