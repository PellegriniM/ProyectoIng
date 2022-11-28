from Escritura import typingInput, typingPrint, LimpiarPantalla #Formato tipo escritura y uso de comando "cls = clear"
import random #Libreria Random
from time import sleep #Delay
from imagenes import *  #Texto representado por "imagenes"
from Texto import * #Texto que narra cosas

#CLASE PRINCIPAL
class Personaje:
        #CREADOR DE CLASE
    def __init__(self, nombre):
        #ATRIBUTOS DE PERSONAJE
        self.nombre = nombre
        self.vida = 100
        self.vidaMax = self.vida
        self.fuerza = 5
        #ATRIBUTOS DE ARMA
        self.armaNombre = "none"
        self.armaDanio = 0
        self.armaNivel = 0
        #ATRIBUTOS DE ARMADURA
        self.armaduraNombre = 'none'
        self.armaduraNivel = 0
        self.defensa = 5
        #MONEDERO
        self.monedero = 0

        #MUESTRA ESTADISTIVAS GENERALES
    def Mostrar(self):
        typingPrint(f".Nombre: {self.nombre}\n")
        typingPrint(f".Vida: {self.vida}\n")
        typingPrint(f".Armadura: {self.armaduraNombre} +{self.armaduraNivel}, con defenza: {self.defensa}, vida maxima {self.vidaMax}\n")
        typingPrint(f".Arma: {self.armaNombre} +{self.armaNivel}, con danio de {self.armaDanio}\n")

        #MUESTRA BALANCE ACTUAL
    def Balance(self):
        print (f"Tu balance es {self.monedero} de oro")

        #CONSEGUIR ORO
    def ConseguirOro(self, total_oro):
        self.monedero = self.monedero + total_oro
        typingPrint(f"Has conseguido {total_oro} de oro, ahora tu balance es {self.monedero}\n")

        #SUBIR NIVEL ARMA
    def armaSubirNivel(self):
        self.armaDanio = self.armaDanio + 2
        self.armaNivel = self.armaNivel + 1

        #MOSTRAR ARMA
    def armaMostrar(self):
        typingPrint(f"{self.armaNombre} +{self.armaNivel} danio: {self.armaDanio}\n")

        #SUBIR NIVEL ARMADURA
    def armaduraSubirNivel(self):
        self.defensa = self.defensa + 8
        self.armaduraNivel = self.armaduraNivel + 1
        self.vidaMax = self.vidaMax + 2

        #MOSTRAR ARMADURA
    def armaduraMostrar(self):
        typingPrint(f"Armadura: {self.armaduraNombre} +{self.armaduraNivel} armadura: {self.defensa}\n")
        typingPrint(f"Vida Maxima: {self.vidaMax}\n")

        #AVISA DE QUE EL JUGADOR TIENE VIDA BAJA
    def AvisoVidaBaja(self):
        if self.vida <= 30:
            print(f"Tienes vida baja!, te recomendamos regresar a la iglesia.")

        #CURARSE
    def Curarse(self):
        print("Te Curas")

        #COMBATE Y SUS ACCIONES

        #RECIBIR DANIO
    def RecibirDanio(self,enemigo_nombre,recibido):
        Jugador.vida = Jugador.vida - recibido
        typingPrint(f"Apareció derrepente un {enemigo_nombre}, y ataco a {self.nombre} recibiendo {recibido} de danio\n")
        if self.vida > 0:
            typingPrint(f"Vida actual es: {self.vida}\n")
            sleep(0.5)

        #MORIR EN MAZMORRA
    def MorirMazmorra(self, enem):
        self.vida = 0
        typingPrint(f"{enem} te ha realizado un fuerte golpe el cual te dejo inconciente...\n")
        sleep(1)
        typingPrint("Por suerte un aventurero que pasaba te logro sacar de la Mazmorra y te llevo a la iglesia...\n")
        Juego.IglesiaMuerte(self)
        
        #VERIFICA SI EL PERSONAJE ESTA VIVO
    def esta_vivo(self):
        return self.vida > 0

        #VERIFICA SI EL PERSONAJE ESTA MUERTO
    def esta_muerto(self):
        return self.vida <= 0
        
        #EN CASO DE MORIR ES ANUNCIADO
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

        #CALCULA EL DANIO QUE HACE
    def daño(self, enemigo):
        return self.armaDanio * self.fuerza - enemigo.defensa

        #ACCION DE ATACAR AL ENEMIGO
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

#CLASE GUERRERO ("SubClase con herencia")
class Guerrero(Personaje):
    def __init__(self,nombre):
        super().__init__(nombre)
        self.clase = "Guerrero"
        self.armaNombre = "Espadon de Hierro"
        self.armaDanio = 5
        self.armaduraNombre = "Armadura Ligera de Escamas"
    
    def Mostrar(self):
        super().Mostrar()
        typingPrint(f".Clase: {self.clase}\n")
        print("")

#CLASE MAGO ("SubClase con herencia")
class Mago(Personaje):
    def __init__(self,nombre):
        super().__init__(nombre)
        self.clase = "Mago"
        self.armaNombre = "Anillo de Merlin"
        self.armaDanio = 5
        self.armaduraNombre = "Armadura de tela Endemoniada"
    
    def Mostrar(self):
        super().Mostrar()
        typingPrint(f".Clase: {self.clase}\n")

#CLASE ELFO ("SubClase con herencia")
class Cazador(Personaje):
    def __init__(self,nombre):
        super().__init__(nombre)
        self.clase = "Cazador"
        self.armaNombre = "Arco de Valhir"
        self.armaDanio = 5
        self.armaduraNombre = "Armadura de Malla"
    
    def Mostrar(self):
        super().Mostrar()
        typingPrint(f".Clase: {self.clase}\n")

#CLASE PALADIN ("SubClase con herencia")
class Paladin(Personaje):
    def __init__(self,nombre):
        super().__init__(nombre)
        self.clase = "Paladin"
        self.armaNombre = "Mazo de la Devosion"
        self.armaDanio = 5
        self.armaduraNombre = "Armadura Pesada Sagrada"
    
    def Mostrar(self):
        super().Mostrar()
        typingPrint(f".Clase: {self.clase}\n")

#CLASE JEFE DE MAZMORRA ("SubClase con herencia")
class Jefe_Mazmorra(Personaje):
    def __init__(self):
        self.nombre = "Gregory el Trotamundos"
        self.vida = 150
        self.fuerza = 10
        self.defensa = 20
        self.armaDanio = 8
        self.clase = "Jefe Mazmorra"
    
    def MostrarBoss(self):
        print(f".Nombre: {self.nombre}")
        print(f".Vida: {self.vida}")
        print(f".Danio: {self.danio}")
        print(f".Clase: {self.clase}")

#COMBATE ENTRE 2 PERSONAJES
def Combate(jugador_1, jugador_2):
    turno = 1
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        typingPrint(f">>> Acción de {jugador_1.nombre}:\n")
        sleep(0.5)
        jugador_1.atacar(jugador_2)
        if jugador_2.esta_muerto():#VERIFICA SI EL JUEGADOR ESTA VIVO
            print("\nHa ganado", jugador_1.nombre)
            sleep(2)
            FinalJuego(Jugador.nombre)
            
        else:#SI EL JUGADOR ESTA VIVO EJECUTA LA ACCION DEL JEFE
            typingPrint(f">>> Acción de {jugador_2.nombre}:\n")
            sleep(0.5)
            jugador_2.atacar(jugador_1)
            turno = turno + 1
            if jugador_1.esta_muerto():
                print("\nHa ganado", jugador_2.nombre)
                typingPrint(f"Has muerto en combate contra {jugador_2.nombre}, un aventurero que pasaba te encontro y te llevó a la iglesia\n")
                Game.IglesiaMuerte()
        sleep(1)

#CLASE PARA ESTABLECER LA SELECCION DEL PERSONAJE A CREAR
class CreacionPersonaje:
    def CrearPersonaje(self, eleccion):
        if eleccion == "1":
            nombre = (typingInput("Ingrese su nombre de usuario: "))
            return Guerrero(nombre)

        elif eleccion == "2":
            nombre = (typingInput("Ingrese su nombre de usuario: "))
            return Mago(nombre)
        
        elif eleccion == "3":
            nombre = (typingInput("Ingrese su nombre de usuario: "))
            return Cazador(nombre)
        
        elif eleccion == "4":
            nombre = (typingInput("Ingrese su nombre de usuario: "))
            return Paladin(nombre)
        
        else:
            print("Error!, caracter invalido")

#DEFINICION DE VARIABLE CREAR LA CUAL SE ENCARGAR DE CREAR AL PERSONAJE CON LA CLASE SELECCIONADA
def Crear():
    Crear_Personaje = CreacionPersonaje()
    eleccion = typingInput("Ingrese:\n1: Guerrero\n2: Mago\n3: Cazador\n4: Paladin\n\nRespete los numeros por favor\n\n")
    return Crear_Personaje.CrearPersonaje(eleccion)

#PERSONAJE YA CREADO CON LA CLASE SELECCIONADA
#Jugador =  Crear()

#PERSONAJE DE TESTEO YA ESTABLECIDO (Se activa a la hora del testeo)
#Jugador = Guerrero("Nombre")

#jUEGO EN GENERAL
class Juego:
    def __init__(self):
        self.matados = 0
        self.nivel = 1
        self.precioArmaMejora = 150
        self.precioArmaduraMejora = 150

    #POBLADO
    def Poblado(self):
        LimpiarPantalla()
        #MENU       
        llave = 0
        while llave != 1:
            print(poblado) #TEXTO QUE APARECE ARRIBA
            print ("Estas en el poblado")
            print ("1     Mazmorra")
            print ("2     Herreria")
            print ("3     Iglesia")
            print ("4     Zona de caza")
            print ("5     Zona de minas")
            print ("6     Estadisticas")
            print ("7     Guia")
            print ("8     Salir del Juego")
            print("")


            typingPrint("A donde quieres ir?\n")
            case = typingInput("")
            if case == "1":
                typingPrint("Yendo a la Mazmorra\n")
                sleep(2)
                Juego.Mazmorra(self)
                llave = 1
            elif case == "2":
                typingPrint("Yendo a la Herreria\n")
                sleep(2)
                Juego.Herreria(self)
                llave = 1
            elif case == "3":
                typingPrint("Yendo a la Iglesia\n")
                sleep(2)
                Juego.Iglesia(self)
                llave = 1
            elif case == "4":
                typingPrint("Yendo a la zona de caza\n")
                sleep(2)
                Juego.Zona_Caza(self)
                llave = 1
            elif case == "5":
                typingPrint("Yendo a la mina\n")
                sleep(2)
                Juego.Mina(self)
                llave = 1
            elif case == "6":
                typingPrint("Estadisticas... \n")
                sleep(1)
                Jugador.Mostrar()
                sleep(1)
                LimpiarPantalla()
            elif case == "7":
                typingPrint("Guia...\n")
                sleep(1)
                GuiaDentroJuego()
                sleep(5)
                LimpiarPantalla()
            elif case == "8":
                typingPrint("Saliendo del juego\n")
                sleep(1.5)
                Cierre()
                llave = 1
            else:
                print("Error!, opcion incorrecta. Reingresar:")
                sleep(1)
                LimpiarPantalla()
            
    #MAZMORRA
    def Mazmorra(self):
        LimpiarPantalla()
        print(mazmorra) #TEXTO QUE APARECE ARRIBA
        enemigos = ["Ogro","Esqueleto","Goblin","Zombie","Duende","Arania","Dragon","Slime","Lobo"]
        total_oro = 0
        print ("Estas en la mazmorra")
        print (f"Nivel actual: {self.nivel}")
        print (f"Enemigos matados: {self.matados}")
        llave = 0
        while llave != 1:
            print(f"ESTAS EN EL NIVEL {self.nivel}")
            #NIVEL 1
            while self.nivel == 1 and llave !=1:
                case = input("Atacar o no? s o n: ")
                if case == 's':
                    enem = random.choice(enemigos)
                    print(f"Has matado a un {enem}")
                    self.matados = self.matados + 1
                    oro = random.randrange(25, 35) #Oro dropeado
                    total_oro = total_oro + oro
                elif case == 'n':
                    typingPrint ("Regresando al PUEBLO")
                    Puntos()
                    Jugador.ConseguirOro( total_oro)
                    sleep(3)
                    llave = 1
                    Juego.Poblado(self)
                else:
                    print("Error!, caracter invalido")
                if self.matados == 10:
                    print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                    print("Has pasado al siguiente nivel")
                    print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                    self.nivel = 2
            #NIVEL 2
            while self.nivel == 2 and llave !=1:
                Jugador.AvisoVidaBaja()
                case = input("Atacar o no? s o n: ")
                if case == 's':
                    prob = random.randint(0,10)
                    enem = random.choice(enemigos)
                    if prob > 7:#Probabilidad del 30% de recibir ataque
                        enem_danio=random.randint(25,30)
                        Jugador.RecibirDanio(enem, enem_danio)
                        if Jugador.esta_muerto():
                            Jugador.monedero = Jugador.monedero + total_oro
                            Jugador.MorirMazmorra(enem)
                    else:
                        print(f"Has matado a un {enem}")
                        self.matados = self.matados + 1
                        oro = random.randrange(35, 45) #Oro dropeado
                        total_oro = total_oro + oro
                elif case == 'n':
                    typingPrint ("Regresando al PUEBLO")
                    Puntos()
                    Jugador.ConseguirOro( total_oro)
                    sleep(3)
                    llave = 1
                    Juego.Poblado(self)
                else:
                    print("Error!, caracter invalido")
                if self.matados == 20:
                    print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                    print("Has pasado al siguiente nivel")
                    print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                    self.nivel = 3
            #NIVEL 3
            while self.nivel == 3 and llave !=1:
                Jugador.AvisoVidaBaja()
                case = input("Atacar o no? s o n: ")
                if case == 's':
                    prob = random.randint(0,10)
                    enem = random.choice(enemigos)
                    if prob > 5:#Probabilidad del 50% de recibir ataque
                        enem_danio=random.randint(25,30)
                        Jugador.RecibirDanio(enem, enem_danio)
                        if Jugador.esta_muerto():
                            Jugador.monedero = Jugador.monedero + total_oro
                            Jugador.MorirMazmorra(enem)
                    else:
                        print(f"Has matado a un {enem}")
                        self.matados = self.matados + 1
                        oro = random.randrange(50, 60) #Oro dropeado
                        total_oro = total_oro + oro
                elif case == 'n':
                    typingPrint ("Regresando al PUEBLO")
                    Puntos()
                    Jugador.ConseguirOro( total_oro)
                    sleep(3)
                    llave = 1
                    Juego.Poblado(self)
                else:
                    print("Error!, caracter invalido")
                if self.matados == 25:
                    typingPrint("Estas a 5 enemigos de avanzar al Jefe final, ten mucho cuidado\n")
                    sleep(1)
                if self.matados == 30:
                    print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                    print("Has pasado al siguiente nivel")
                    print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                    self.nivel = 4            
            #NIVEL 4
            while self.nivel == 4 and llave !=1:
                Jugador.AvisoVidaBaja()
                llave = 0
                while llave != 1:
                    case = typingInput("Quieres enfrentarte al Jefe Final o regresar? s o n: ")
                    if case == 's':
                        typingPrint("Te enfrentaras al Jefe\n")
                        print("")
                        sleep(2)
                        Jefe = Jefe_Mazmorra()
                        llave = 1
                        Combate(Jugador, Jefe)
                    elif case == 'n':
                        typingPrint ("Regresando al PUEBLO")
                        Puntos()
                        Jugador.monedero = Jugador.monedero + total_oro
                        sleep(3)
                        llave = 1
                        Juego.Poblado(self)
                    else:
                        print ("Error!, ingresaste un caracter invalido")
    #HERRERIA
    def Herreria(self):
        LimpiarPantalla()
        llave = 0
        while llave != 1:
            print(herreria) #TEXTO QUE APARECE ARRIBA
            print(f"Balance actual: {Jugador.monedero}")
            print(f"1)   Mejorar arma, costo: {self.precioArmaMejora}")
            print(f"2)   Mejorar armadura, costo: {self.precioArmaduraMejora}")
            print(f"3)   Salir,(regresar al poblado)")
            case = input("Que quiere hacer? (Ingrese numero) \n")
            if case == '1':
                sleep(1)
                if Jugador.armaNivel < 5:
                    if Jugador.monedero >= self.precioArmaMejora:
                        typingPrint(f"Mejorando: {Jugador.armaNombre}\n")
                        Jugador.monedero = Jugador.monedero - self.precioArmaMejora
                        Jugador.armaSubirNivel()
                        Jugador.armaMostrar()
                        sleep(3)
                        self.precioArmaMejora = round(self.precioArmaMejora * 1.25)
                        LimpiarPantalla()
                    else:
                        print("No posees la cantidad para mejorar el arma")
                        sleep(2)
                        LimpiarPantalla()
                else:
                    print("Tienes el nivel maximo posible del arma")
                    self.precioArmaMejora = "MAX"
                    sleep(2)
                    LimpiarPantalla()
            elif case == '2':
                if Jugador.armaduraNivel < 5:
                    if Jugador.monedero >= self.precioArmaduraMejora:
                        typingPrint(f"Mejorando: {Jugador.armaduraNombre}\n")
                        Jugador.monedero = Jugador.monedero - self.precioArmaduraMejora
                        Jugador.armaduraSubirNivel()
                        Jugador.armaduraMostrar()
                        sleep(3)
                        self.precioArmaduraMejora = round(self.precioArmaduraMejora * 2)
                        LimpiarPantalla()
                    else:
                        print("No posees la cantidad para mejorar la armadura")
                        sleep(2)
                        LimpiarPantalla()
                else:
                    print("Tienes el nivel maximo posible del la armadura")
                    self.precioArmaduraMejora = "MAX"
                    sleep(2)
                    LimpiarPantalla()
            elif case == '3':
                typingPrint("Saliendo")
                Puntos()
                sleep(2)
                Juego.Poblado(self)
                llave = 1
            else:
                sleep(1)
                print("Error!, caracter invalido. Ingrese nuevemante su opcion")
                sleep(2)
                LimpiarPantalla()
    #IGLESIA
    def Iglesia(self):
        LimpiarPantalla()
        llave = 0
        while llave != 1:
            LimpiarPantalla()
            print(iglesia) #TEXTO QUE APARECE ARRIBA
            print("1             Donar = $20")
            print("2             Salir")
            case = input()
            if case == "1":
                if Jugador.vida != Jugador.vidaMax:
                    if Jugador.monedero > 20:
                        typingPrint("Has donado $20 pero te los sacerdontes te han curado\n")
                        Jugador.monedero = Jugador.monedero - 20
                        sleep(2)
                        falta = Jugador.vidaMax - Jugador.vida
                        Jugador.vida = Jugador.vida + falta
                        sleep(2)
                        typingPrint(f"Te has curado {falta} puntos de vida\n")
                        sleep(3)
                    else:
                        typingPrint("No te puedes permitir donar $20\n")
                        sleep(3)
                else:
                    typingPrint("Tienes la vida completa\n")
                    sleep(3)
            elif case == "2":
                typingPrint("Saliendo")
                Puntos()
                sleep(2)
                Juego.Poblado(self)
                llave = 1
            else:
                typingPrint("Error!, caracter invalido\n")

    #IGLESIA CUANDO EL PERSONAJE MUERE (solo se invoca cuando el personaje muere)
    def IglesiaMuerte(self):
        Jugador.vida = Jugador.vidaMax
        sleep(2)
        LimpiarPantalla()
        print(iglesia)
        typingPrint("Luego de varios segundos te despiertas y emprendes de nuevo tu viaje\n")
        sleep(2)
        Juego.Poblado(self)
    
    #ZONA DE CAZA ("Prevenir que el jugador no tenga oro para realizar acciones")
    def Zona_Caza(self):
        animales = ["conejo","ciervo","perdiz","zorro","nada"]
        llave = 0
        self.conejo_total = 0
        self.ciervo_total = 0
        self.perdiz_total = 0
        self.zorro_total = 0
        self.total_caza = 0
        self.tiempo_total = 0
        while llave != 1:
            conejo = 0
            ciervo = 0
            perdiz = 0
            zorro = 0
            nada = 0
            LimpiarPantalla()
            print(zona_de_caza)
            case = typingInput("Quieres arrancar la caza o salir? s o n: ")
            if case == 's':
                tiempo = float(typingInput("Cuanto tienpo quieres caza?,(solo numeros),seg: "))
                self.tiempo_total = self.tiempo_total + tiempo
                cantidad_norm = tiempo + (tiempo * 0.65)
                cantidad = round(cantidad_norm)
                for i in range(cantidad):
                    animal_cazado = random.choice(animales)
                    if animal_cazado == 'conejo':
                        conejo = conejo + 1
                        self.conejo_total = self.conejo_total + 1
                    elif animal_cazado == 'ciervo':
                        ciervo = ciervo + 1
                        self.ciervo_total = self.ciervo_total + 1
                    elif animal_cazado == 'perdiz':
                        perdiz = perdiz + 1
                        self.perdiz_total = self.perdiz_total + 1
                    elif animal_cazado == 'zorro':
                        zorro = 1
                        self.zorro_total = self.zorro_total + 1
                    else:
                        nada = nada + 1
                sleep(tiempo)
                typingPrint("Has matado:\n")
                print(f".Conejo: {conejo}")
                print(f".Ciervo: {ciervo}")
                print(f".Perdiz: {perdiz}")
                print(f".Zorro {zorro}")
                sleep(5)
            elif case == 'n':
                typingPrint("Total animales matados:\n")
                print(f".Conejo: {self.conejo_total}")
                print(f".Ciervo: {self.ciervo_total}")
                print(f".Perdiz: {self.perdiz_total}")
                print(f".Zorro {self.zorro_total}")
                print("")
                typingPrint(f"Tienpo de caza: {self.tiempo_total:.0f}Hs\n")
                total_caza = self.conejo_total + self.ciervo_total + self.perdiz_total + self.zorro_total
                typingPrint(f"Has cazado un total de {total_caza} animales\n")
                valor_normal = total_caza + (total_caza * 2.5)
                total_oro = round(valor_normal)
                typingPrint(f"Le has vendido las cosas obtenidas al cazador del pueblo.\n")
                Jugador.ConseguirOro(total_oro)
                sleep(2)
                typingPrint("Saliendo")
                Puntos()
                sleep(2)
                Juego.Poblado(self)
                llave = 1
            else:
                print("Error!, caracter invalido!")
                sleep(2)

    #ZONA DE MINERIA ("Prevenir que el jugador no tenga oro para realizar acciones")
    def Mina(self):
        llave = 0
        minerales = [1,1,1,0,0,]
        minerales_con_bono = [1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,2,2]
        self.minerales = 0
        self.mithril = 0
        self.tiempo_total = 0
        while llave != 1:
            minados = 0
            mithril = 0
            LimpiarPantalla()
            print(zona_de_mineria)
            case = typingInput("Quieres arrancar a minar o salir? s o n: ")
            if case == 's':
                tiempo = float(typingInput("Cuanto tienpo quieres minar?,(solo numeros),seg: "))
                self.tiempo_total = self.tiempo_total + tiempo
                cantidad_norm = tiempo + (tiempo * 2.8)
                cantidad = round(cantidad_norm)
                if tiempo > 7:
                    for i in range(cantidad):
                        mineral_minado = random.choice(minerales_con_bono)
                        if mineral_minado == 1:
                            minados = minados + 1
                            self.minerales = self.minerales + 1
                        elif mineral_minado == 2:
                            mithril = mithril + 1
                            self.mithril = self.mithril + 1
                else:
                    for i in range(cantidad):
                        mineral_minado = random.choice(minerales)
                        if mineral_minado == 1:
                            minados = minados + 1
                            self.minerales = self.minerales + 1
                sleep(tiempo)
                typingPrint("Has minado:\n")
                typingPrint(f".Minerales: {minados}\n")
                sleep(2)
                if mithril != 0:
                    typingPrint(f"Has conseguir {mithril} de mithril, muy valioso!\n")
                    sleep(2)
            elif case == 'n':
                typingPrint(f"Total de minerales minados: {self.minerales}\n")
                sleep(2)
                if self.mithril != 0:
                    typingPrint(f".Mithril conseguido: {self.mithril}\n")
                    sleep(2)
                typingPrint(f"Tienpo de minando: {self.tiempo_total:.0f}Hs\n")
                valor_normal = self.minerales + (self.minerales * 4.2)
                valor_mithril = self.mithril + (self.mithril * 50)
                total_oro = round(valor_normal + valor_mithril)
                typingPrint("Le has vendido los minerales obtenidos al minero del pueblo.\n")
                Jugador.ConseguirOro(total_oro)
                sleep(2)
                typingPrint("Saliendo...\n")
                sleep(2)
                Juego.Poblado(self)
                llave = 1

            else:
                print("Error!, caracter invalido!")


Inicializacion()
Jugador = Crear()
InicioDeJuego(Jugador.nombre,Jugador.clase)
sleep(2)
LimpiarPantalla()
GuiaDeInicio()
sleep(3)
Game = Juego()
Game.Poblado()
