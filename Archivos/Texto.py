from Escritura import typingInput,typingPrint,LimpiarPantalla
from time import sleep
from barraCargado import *
from imagenes import titulo, victoria, fin

def Puntos():
    sleep(0.5)
    typingPrint(".")
    sleep(0.5)
    typingPrint(".")
    sleep(0.5)
    typingPrint(".\n")

def Inicializacion():
    LimpiarPantalla()
    typingPrint("Inicizalizando")
    Puntos()
    sleep(0.5)
    typingPrint("Cargando configuracion")
    Puntos()
    sleep(2)
    typingPrint("Iniciando la creacion de personaje")
    Puntos()
    sleep(1)
    print("")

def InicioDeJuego(nombre,clase):
    print("")
    typingPrint("Completado")
    Puntos()
    sleep(2)
    LimpiarPantalla()
    sleep(2)
    Barra()
    sleep(2)
    LimpiarPantalla()
    print(titulo)
    sleep(2)
    typingPrint(f"Damos comienzo a la aventura de {nombre} un {clase}, que se enfrentara al Jefe de la Mazmorra para poder liberar el pueblo de su maldición")

def FinalJuego(nombre):
    LimpiarPantalla()
    sleep(1)
    print(victoria)
    sleep(1)
    print("")
    typingPrint(f"{nombre}, ha podido derrotar al Jefe de la Mazmorra y pudo liberar al pueblo de la maldición.\n")
    typingPrint(f"Ya sin ninguna preocupacion, {nombre}, se toma unas vacaciones para poder disfrutar su victoria")
    Puntos()
    sleep(2)
    LimpiarPantalla()
    print(fin)
    print("")
    sleep(2)
    typingPrint("Muchas gracias por jugar este juego\n")
    print("")
    typingPrint("Desarrolladores:\n\nPellegrini Mateo\nPodesta Felipe\nPellegrini Ulises")
    sleep(10)

def Cierre():
    LimpiarPantalla()
    typingPrint("Gracias por probar el juego\n\n")
    sleep(2)
    typingPrint("Desarrolladores:\n\nPellegrini Mateo\nPodesta Felipe\nPellegrini Ulises")
    sleep(2)

def GuiaDeInicio():
    typingPrint("GUIA para comprender los aspectos básicos sobre el juego:\n")
    print("")
    typingPrint("Mazmorra: Lugar donde el jugador se enfrentara a enemigos y donde se completa el juego.\n\n")
    typingPrint("Herreria: Lugar donde el jugador puede mejorar su arma y armadura para aumentas sus estadisticas.\n\n")
    typingPrint("Iglesia: Lugar donde el jugador podra curarse a coste de una 'donacion'.\n\n")
    typingPrint("Zonas de caza y mineria: Lugares donde el jugador podra comseguir oro a cambio de tiempo de juego.\n\n")
    typingPrint("Estadisticas: El jugador podra consultar sus estadisticas actuales.\n\n")
    print("\n\n\n\n")
    typingPrint("El objetivo principal del Jugador es poder superar el ultimo nivel de la Mazmorra, enfrentandose al Jefe.\n")

def GuiaDentroJuego():
    print("Mazmorra: El Jugador se enfrentara a enemigos y llegar al ultimo nivel para derrotar al Jefe para completar el Juego.")
    print("Herreria: Lugar donde se puede mejorar el arma y armadura del Jugador para poder mejorar las estadisticas.")
    print("Iglesia: El Jugador se podra curar toda la vida, donando $20.")
    print("Zonas de caza y mineria: El Jugador puede gastar tiempo a cambio de conseguir recursos que vendera para conseguir oro.")