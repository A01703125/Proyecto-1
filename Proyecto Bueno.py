# Calculadora que convierte unidades
# Este programa ayudará a aquellas personas que tengan problemas con conversiones de unidades
# :)
import math
#Aquí el programa pide qué se va a convertir
print("Bienvenido, ¿qué quieres convertir?")

#Aquí define millas a kilometros
def millas_kilometros(millas):
    return("Aqui tiene sus kilometros", millas*1.609)
millas = float(input("millas"))
print(millas*1.609, "km")

#Aqui define grados celsius a fahrenheit
def celsius_fahrenheit(celsius):
    print("Aqui tiene sus grados fahrenheit", celsius*1.8 +32)

celsius = float(input("celsius"))
print(celsius*1.8 +32, "grados fahrenheit")

#Aqui define que es fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    print("Aquí tiene sus grados celsius", (fahrenheit-32/1.8))

fahrenheit = float(input("fahnrenheit"))
print(fahrenheit-32/1.8, "grados celsius")

#Aqui define que kilometros a millas
def kilometros_millas(kilometros):
    print("Aqui tiene sus millas", kilometros*.62)

kilometros = float(input("kilometros"))
print(kilometros*.62, "millas")

#Aqui define de celsius a kelvin
def celsius_kelvin(celsiusk):
    print("Aqui tiene sus grados kelvin", celsiusk+273.15)
celsiusk = float(input("celsiusk"))
print(celsiusk+273.15, "grados kelvin")

#Aqui define de kelvin a celsius
def kelvin_celsius(kelvin):
    print("Aqui tiene sus grados celsius", kelvin-273.15)

kelvin = float(input("kelvin"))
print(kelvin-273.15, "grados celsius")

#Aqui pide mas cosas
def metros_pies(metros):
    print("Aqui tiene sus pies", metros*3.2808)
metros = float(input("metros"))
print(metros*3.2808, "pies")

def pies_metros(pies):
    print ("Aquí tiene sus metros", pies/3.2808)

pies = float(input("pies"))
print(pies/3.2808, "metros")




