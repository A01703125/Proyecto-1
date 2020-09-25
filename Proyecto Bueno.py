# Calculadora que convierte unidades
# Este programa ayudará a aquellas personas que tengan problemas con conversiones de unidades
# :)
import math
#Aquí el programa pide qué se va a convertir
print("Bienvenido, ¿qué quieres convertir?")

#Aquí define millas a kilometros
def millas_kilometros(millas):
    if millas == 0:
       print("No se pueden convertir las unidades")
    else:
       return( millas*1.609)
    
#Aqui define grados celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return(celsius*1.8 +32)

#Aqui define que es fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return(fahrenheit-32/1.8)

#Aqui define que kilometros a millas
def kilometros_millas(kilometros):
    if kilometros == 0:
        print ("No se pueden convertir las unidades") 
    else:
        return(kilometros*.62)

#Aqui define de celsius a kelvin
def celsius_kelvin(celsiusk):
    return(celsiusk+273.15)

#Aqui define de kelvin a celsius
def kelvin_celsius(kelvin):
    return(kelvin-273.15)

#Aqui pide mas cosas
def metros_pies(metros):
    return(metros*3.2808)

#Aqui convierte de pies a metros
def pies_metros(pies):
    return(pies/3.2808)
#Aqui empieza el loop
while True:
#Aqui el usuario pone los numeros y el programa los saca

    millas = float(input("millas"))
    print("Aqui tiene sus kilometros:",millas_kilometros(millas))

    celsius = float(input("celsius"))
    print("Aqui tiene sus grados fahrenheit:", celsius*1.8 +32, "grados fahrenheit")

    fahrenheit = float(input("fahnrenheit"))
    print("Aquí tiene sus grados celsius:", fahrenheit-32/1.8, "grados celsius")

    kilometros = float(input("kilometros")) 
    if kilometros == 0:
        print("No se pueden convertir las unidades")
    print("Aqui tiene sus millas:", kilometros*.62, "millas")

    celsiusk = float(input("celsiusk"))
    print("Aqui tiene sus grados kelvin:", celsiusk+273.15, "grados kelvin")

    kelvin = float(input("kelvin"))
    print("Aqui tiene sus grados celsius:", kelvin-273.15, "grados celsius=")

    metros = float(input("metros"))
    if metros == 0:
            print("No se pueden convertir las unidades")
    print("Aqui tiene sus pies:", metros*3.2808, "pies")

    pies = float(input("pies"))
    if pies == 0:
            print("No se pueden convertir las unidades")
        
    print("Aquí tiene sus metros:", pies/3.2808, "metros")

    print("Gracias por usar nuestro programa!")

    print("¿Quieres convertir más unidades?")
    print("1. para empezar otra vez y 2. para no empezar otra vez")
 #Si el usuario quiere empezar otra vez, este es el momento
    answer = int(input("answer= "))
    if answer== 1:
        print("¿Qué quieres convertir?")
        str(input( ))    
        continue
    if answer <2 :
        print("Pon una respuesta adecuada")
    if answer == 2:
       print("Gracias por usar el programa")
#aqui acaba el loop
       break 
   
      
    
        
