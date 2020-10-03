# Calculadora que convierte unidades
# Este programa ayudará a aquellas personas que tengan problemas con conversiones de unidades
# :)
#Aquí el programa pide qué se va a convertir
print("Bienvenido, ¿qué quieres convertir?")

#Aquí define millas a kilometros
def millas_kilometros(millas):
    if millas == 0:
       print("No se pueden convertir las unidades")
    else:
        kilometros = millas*1.609
        guardar('Millas-Kilometros', kilometros) 
        return kilometros
    
    
#Aqui define grados celsius a fahrenheit
def celsius_fahrenheit(celsius):
    fahrenheit = celsius*1.8 + 32
    guardar('Celsius-Fahrenheit', fahrenheit) 
    return celsius
   

#Aqui define que es fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    celsiusf = fahrenheit-32/1.8
    guardar('Fahrenheit-Celsius', celsiusf)
    return celsius
   

#Aqui define que kilometros a millas
def kilometros_millas(kilometros):
    if kilometros == 0:
        print ("No se pueden convertir las unidades") 
    else:
        millas = kilometros*.62
        guardar('Kilometros-Millas', millas) 
        return millas
        

#Aqui define de celsius a kelvin
def celsius_kelvin(celsiusk):
        kelvin = celsiusk+273.15
        guardar('Celsius-kelvin', kelvin) 
        return kelvin
    

#Aqui define de kelvin a celsius
def kelvin_celsius(kelvin):
    celsiusk = kelvin-273.15
    guardar('Kelvin-celsius', celsiusk) 
    return celsius
  

#Aqui pide mas cosas
def metros_pies(metros):
    pies = metros*3.2808
    guardar('metros-pies', pies) 
    return pies
   

#Aqui convierte de pies a metros
def pies_metros(pies):
    metros = pies/3.2808
    guardar('Pies-Metros', metros) 
    return metros
    

def guardar(unidades, resultado): # Para guardar datos en una lista
    resp = input('¿Quieres que lo guarde?')
    if resp == 'si':
        g = 'Operacion '+unidades+' : '+str(resultado)
        guardado.append(g)
        return guardado
    if resp == 'no':
        print("OK, no lo guardare")

guardado = list() #Crear una lista para guardar cosas.



#Aqui empieza el loop
while True:
#Aqui el usuario pone los numeros y el programa los saca

    millas = float(input("millas"))
    print("Aqui tiene sus kilometros:",millas_kilometros(millas))

    celsius = float(input("celsius"))
    print("Aqui tiene sus grados fahrenheit:", celsius_fahrenheit(celsius), "grados fahrenheit")

    fahrenheit = float(input("fahrenheit"))
    print("Aquí tiene sus grados celsius:", fahrenheit_celsius(fahrenheit) , "grados celsius")

    kilometros = float(input("kilometros")) 
    if kilometros == 0:
        print("No se pueden convertir las unidades")
    print("Aqui tiene sus millas:", kilometros_millas(kilometros), "millas")

    celsiusk = float(input("celsiusk"))
    print("Aqui tiene sus grados kelvin:", celsius_kelvin(celsiusk), "grados kelvin")

    kelvin = float(input("kelvin"))
    print("Aqui tiene sus grados celsius:", kelvin_celsius(kelvin) , "grados celsius=")

    metros = float(input("metros"))
    if metros == 0:
            print("No se pueden convertir las unidades")
    print("Aqui tiene sus pies:", metros_pies(metros), "pies")

    pies = float(input("pies"))
    if pies == 0:
            print("No se pueden convertir las unidades")
        
    print("Aquí tiene sus metros:", pies_metros(pies) , "metros")

    print("Gracias por usar nuestro programa!")

    print("¿Quieres convertir más unidades?")
    print("1. para empezar otra vez y 2. para no empezar otra vez y 3. para ver todo lo que tengas guardado")
 #Si el usuario quiere empezar otra vez, este es el momento
    answer = int(input("answer= "))
    if answer== 1:
        print("¿Qué quieres convertir?")
        str(input( ))    
        continue
    if answer >3 :
        print("Pon una respuesta adecuada")
    if answer == 2:
        print("Gracias por usar el programa")
    if answer == 3: 
        print("Aqui tiene su lista", guardado)
#aqui acaba el loop
    break 
   
      
    
        
