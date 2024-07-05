from random import *


#Lista de palabras 

palabras = ["Manuel","Carro","Perro"]

cantidadElementos = len(palabras) - 1
print(cantidadElementos)

#funcion para mostrar las lineas de las palabras 
def MostrarLineas():
    
    global palabraSeleccionadaMin
    
    listaEspacios = []
    palabra = randint(0,cantidadElementos)
    palabraSeleccionada = palabras[palabra]
    palabraSeleccionadaMin = palabraSeleccionada.lower()
    
    cantidadEspacios = len(palabraSeleccionada)
    
    for i in range(cantidadEspacios):
        
        listaEspacios.append("_")
    
    
    print(palabraSeleccionadaMin)
    
    return listaEspacios


Lineas = MostrarLineas()



#funcion para saber si la letra que ingreso es la correcta en caso de ser asi que mande la letra a la lista de espacios y remplaze el espacio por una letra

def PonerLetras():
    contador = 0
    vidas = 3
    contadorDeCaracteres = len(palabraSeleccionadaMin)
    global guardarPalabra
    
    
    
    
    while vidas != 0:
       print(Lineas)
           
       letra = input("Dame una letra")
       letraMin = letra.lower()
       contador = 0
       
       
       for x in palabraSeleccionadaMin:
           
           contador += 1
           
           if letraMin == x:
                 
                 numeroIteracion = contador - 1
                 Lineas[numeroIteracion] = letra
                 break
                 
                 
           elif contador == contadorDeCaracteres:
               vidas = vidas - 1
               print("Las vidas son" , vidas)
                
                
           
               
           
       
           
               
               
              
           

               
juego = PonerLetras()
print(juego)               
               
            
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
    