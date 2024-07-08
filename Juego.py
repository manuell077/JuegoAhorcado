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
    contadorCaracteres = len(palabraSeleccionadaMin)
    estadoJuego = ""
    
    
    global guardarPalabra
    
    
    
    
    while vidas != 0:
       existePalabra = False
       print(Lineas)
           
       letra = input("Dame una letra")
       letraMin = letra.lower()
       
       
       
       
       contador = 0
       
       for x in palabraSeleccionadaMin:
           
           contador += 1
           
           if letraMin == x:
                 
                 numeroIteracion = contador - 1
                 Lineas[numeroIteracion] = letra
                 existePalabra = True
           
           elif existePalabra == False and contador == contadorCaracteres:
                vidas = vidas - 1
                print("Vidas restantes",vidas)
                        
                 
                    
 
def añadirLetra():
    
    palabra = input("Añade una palabra a la lista ") 
    
    palabras.append(palabra)
  
                
           
def menu():
    
    mostrarMenu = True
    
    while  mostrarMenu == True:
        
        print("JUEGO DEL AHORCADO") 
        print("1.Iniciar juego")
        print("2.Añadir Palabras")
        print("3.salir del juego")           
           
        opcionJuego = int(input("Que quieres hacer?"))   
           
        if   opcionJuego == 1:
            
            juego = PonerLetras()
            print(juego) 
        
        elif opcionJuego == 2:     
                 
            añadir = añadirLetra()
            print(añadir)
            
        elif opcionJuego == 3:
            
            mostrarMenu = False         

                   
              
           
menu()

               
              
               
            
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
    