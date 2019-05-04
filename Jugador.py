#clases jugadores
import pygame as pg
import random as rd
from Constantes import *
from Sprites import *


class Player(pg.sprite.Sprite):
    def __init__(self, game, personaje,mov_der, mov_izq, direccion, movJoystick, respawn, skin=False):
        "======================================================================================="
        "Varibles iniciales del jugador"
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.n=0
        self.frames = 12
        self.skin = skin
        "Perros"
        if personaje ==1:
            self.Sound_ATK= pg.mixer.Sound("Sounds/pate.wav")
            self.ataque = 10 
            self.defensa = 3
            self.velocidad = 1
            if self.skin:
                self.Perro= [
                            SpriteStripAnim('Personajes/PateSheet2.png', (0,0,112.5,75), 3, -1, True, self.frames, True),  #Standby der
                            SpriteStripAnim('Personajes/PateSheet2.png', (0,0,112.5,75), 3, -1, True, self.frames, False), #standby izq

                            SpriteStripAnim('Personajes/PateSheet2.png', (0,145,94.5,78), 3, -1, True, self.frames, True),  #mov der
                            SpriteStripAnim('Personajes/PateSheet2.png', (0,145,94.5,78), 3, -1, True, self.frames, False), #mov izq

                            SpriteStripAnim('Personajes/PateSheet2.png', (0,223,105,89), 1, -1, True, self.frames, True),  #Jump der
                            SpriteStripAnim('Personajes/PateSheet2.png', (0,223,105,89), 1, -1, True, self.frames, False), #Jump izq

                            SpriteStripAnim('Personajes/PateSheet2.png', (106,223,105,88), 1, -1, True, self.frames, True),  #caida der
                            SpriteStripAnim('Personajes/PateSheet2.png', (106,223,105,88), 1, -1, True, self.frames, False), #caida izq

                            SpriteStripAnim('Personajes/PateSheet2.png', (0,312,91,74), 2, -1, True, self.frames, True),  #daño der
                            SpriteStripAnim('Personajes/PateSheet2.png', (0,312,91,74), 2, -1, True, self.frames, False),  #daño izq

                            SpriteStripAnim('Personajes/PateSheet2.png', (0,456,127,68), 2, -1, True, self.frames, True),  #ATK der
                            SpriteStripAnim('Personajes/PateSheet2.png', (0,456,127,68), 2, -1, True, self.frames, False) #ATK izq
                            ]

            else:            
                self.Perro= [
                            SpriteStripAnim('Personajes/PateSheet.png', (0,0,112.5,75), 3, -1, True, self.frames, True),  #Standby der
                            SpriteStripAnim('Personajes/PateSheet.png', (0,0,112.5,75), 3, -1, True, self.frames, False), #standby izq

                            SpriteStripAnim('Personajes/PateSheet.png', (0,145,94.5,78), 3, -1, True, self.frames, True),  #mov der
                            SpriteStripAnim('Personajes/PateSheet.png', (0,145,94.5,78), 3, -1, True, self.frames, False), #mov izq

                            SpriteStripAnim('Personajes/PateSheet.png', (0,223,105,89), 1, -1, True, self.frames, True),  #Jump der
                            SpriteStripAnim('Personajes/PateSheet.png', (0,223,105,89), 1, -1, True, self.frames, False), #Jump izq

                            SpriteStripAnim('Personajes/PateSheet.png', (106,223,105,88), 1, -1, True, self.frames, True),  #caida der
                            SpriteStripAnim('Personajes/PateSheet.png', (106,223,105,88), 1, -1, True, self.frames, False), #caida izq

                            SpriteStripAnim('Personajes/PateSheet.png', (0,312,91,74), 2, -1, True, self.frames, True),  #daño der
                            SpriteStripAnim('Personajes/PateSheet.png', (0,312,91,74), 2, -1, True, self.frames, False),  #daño izq

                            SpriteStripAnim('Personajes/PateSheet.png', (0,456,127,68), 2, -1, True, self.frames, True),  #ATK der
                            SpriteStripAnim('Personajes/PateSheet.png', (0,456,127,68), 2, -1, True, self.frames, False) #ATK izq
                            ]     
                    
        elif personaje ==2:
            self.Sound_ATK= pg.mixer.Sound("Sounds/choco.ogg")
            self.ataque = 2
            self.defensa = 4
            self.velocidad = 3
            if self.skin:                    
                self.Perro = [
                        SpriteStripAnim('Personajes/ChocoSheet2.png', (0,241,105,60), 3, -1, True, self.frames, True),#Standby derecha
                        SpriteStripAnim('Personajes/ChocoSheet2.png', (0,241,105,60), 3, -1, True, self.frames, False), #Standby izquierda
                        
                        SpriteStripAnim('Personajes/ChocoSheet2.png', (0,182,105,60), 3, -1, True, self.frames, True),#Mov der 
                        SpriteStripAnim('Personajes/ChocoSheet2.png', (0,182,105,60), 3, -1, True, self.frames, False),#Mov izq

                        SpriteStripAnim('Personajes/ChocoSheet2.png', (0,301,105,60), 1, -1, True, self.frames, True),#Jump der
                        SpriteStripAnim('Personajes/ChocoSheet2.png', (0,301,105,60), 1, -1, True, self.frames, False),#Jump izq

                        SpriteStripAnim('Personajes/ChocoSheet2.png', (105,301,105,60), 1, -1, True, self.frames, True),#caida der
                        SpriteStripAnim('Personajes/ChocoSheet2.png', (105,301,105,60), 1, -1, True, self.frames, False),#caida izq

                        SpriteStripAnim('Personajes/ChocoSheet2.png', (0,361,105,52), 2, -1, True, self.frames, True),#daño der
                        SpriteStripAnim('Personajes/ChocoSheet2.png', (0,361,105,52), 2, -1, True, self.frames, False),#daño izq

                        SpriteStripAnim('Personajes/ChocoSheet2.png', (0,556,124,60), 2, -1, True, self.frames, True),#ATK der
                        SpriteStripAnim('Personajes/ChocoSheet2.png', (0,556,124,60), 2, -1, True, self.frames, False)#ATK izq
                        ]
            else:
                self.Perro = [
                    SpriteStripAnim('Personajes/ChocoSheet.png', (0,241,105,60), 3, -1, True, self.frames, True),#Standby derecha
                    SpriteStripAnim('Personajes/ChocoSheet.png', (0,241,105,60), 3, -1, True, self.frames, False), #Standby izquierda
                    
                    SpriteStripAnim('Personajes/ChocoSheet.png', (0,182,105,60), 3, -1, True, self.frames, True),#Mov der 
                    SpriteStripAnim('Personajes/ChocoSheet.png', (0,182,105,60), 3, -1, True, self.frames, False),#Mov izq

                    SpriteStripAnim('Personajes/ChocoSheet.png', (0,301,105,60), 1, -1, True, self.frames, True),#Jump der
                    SpriteStripAnim('Personajes/ChocoSheet.png', (0,301,105,60), 1, -1, True, self.frames, False),#Jump izq

                    SpriteStripAnim('Personajes/ChocoSheet.png', (105,301,105,60), 1, -1, True, self.frames, True),#caida der
                    SpriteStripAnim('Personajes/ChocoSheet.png', (105,301,105,60), 1, -1, True, self.frames, False),#caida izq

                    SpriteStripAnim('Personajes/ChocoSheet.png', (0,361,105,52), 2, -1, True, self.frames, True),#daño der
                    SpriteStripAnim('Personajes/ChocoSheet.png', (0,361,105,52), 2, -1, True, self.frames, False), #daño 

                    SpriteStripAnim('Personajes/ChocoSheet.png', (0,556,124,60), 2, -1, True, self.frames, True),#ATK der
                    SpriteStripAnim('Personajes/ChocoSheet.png', (0,556,124,60), 2, -1, True, self.frames, False)#ATK izq
                    ]
                    
        elif personaje ==3:
            self.Sound_ATK= pg.mixer.Sound("Sounds/rayo.ogg")
            self.ataque = 1
            self.defensa = 3
            self.velocidad = 5
            if self.skin:
                self.Perro = [
                        SpriteStripAnim('Personajes/LazerSheet2.png', (0,0,73,61), 2, -1, True, self.frames, True),#Standby der
                        SpriteStripAnim('Personajes/LazerSheet2.png', (0,0,73,61), 2, -1, True, self.frames, False),#Standby izq

                        SpriteStripAnim('Personajes/LazerSheet2.png', (0,184,73.5,61), 3, -1, True, self.frames, True),#Mov der
                        SpriteStripAnim('Personajes/LazerSheet2.png', (0,184,73.5,61), 3, -1, True, self.frames, False),#Mov izq

                        SpriteStripAnim('Personajes/LazerSheet2.png', (0,246,73,63), 1, -1, True, self.frames, True),#Jump der
                        SpriteStripAnim('Personajes/LazerSheet2.png', (0,246,73,63), 1, -1, True, self.frames, False),#Jump izq

                        SpriteStripAnim('Personajes/LazerSheet2.png', (157,246,63,63), 1, -1, True, self.frames, True),#caida der
                        SpriteStripAnim('Personajes/LazerSheet2.png', (157,246,63,63), 1, -1, True, self.frames, False),#caida izq 

                        SpriteStripAnim('Personajes/LazerSheet2.png', (0,123,73,61), 2, -1, True, self.frames, True),#daño der
                        SpriteStripAnim('Personajes/LazerSheet2.png', (0,123,73,61), 2, -1, True, self.frames, False),#daño izq  

                        SpriteStripAnim('Personajes/LazerSheet2.png', (0,315,90,57), 1, -1, True, self.frames, True)+
                        SpriteStripAnim('Personajes/LazerSheet2.png', (92,315,115,57), 1, -1, True, self.frames, True),#ATk der
                        SpriteStripAnim('Personajes/LazerSheet2.png', (0,315,90,57), 1, -1, True, self.frames, False)+
                        SpriteStripAnim('Personajes/LazerSheet2.png', (92,315,115,57), 1, -1, True, self.frames, False)#ATk izq 
                        ]
            else:
                self.Perro = [
                        SpriteStripAnim('Personajes/LazerSheet.png', (0,0,73,61), 2, -1, True, self.frames, True),#Standby der
                        SpriteStripAnim('Personajes/LazerSheet.png', (0,0,73,61), 2, -1, True, self.frames, False),#Standby izq

                        SpriteStripAnim('Personajes/LazerSheet.png', (0,184,73.5,61), 3, -1, True, self.frames, True),#Mov der
                        SpriteStripAnim('Personajes/LazerSheet.png', (0,184,73.5,61), 3, -1, True, self.frames, False),#Mov izq

                        SpriteStripAnim('Personajes/LazerSheet.png', (0,246,73,63), 1, -1, True, self.frames, True),#Jump der
                        SpriteStripAnim('Personajes/LazerSheet.png', (0,246,73,63), 1, -1, True, self.frames, False),#Jump izq

                        SpriteStripAnim('Personajes/LazerSheet.png', (157,246,63,63), 1, -1, True, self.frames, True),#caida der
                        SpriteStripAnim('Personajes/LazerSheet.png', (157,246,63,63), 1, -1, True, self.frames, False),#caida izq 

                        SpriteStripAnim('Personajes/LazerSheet.png', (0,123,73,61), 2, -1, True, self.frames, True),#daño der
                        SpriteStripAnim('Personajes/LazerSheet.png', (0,123,73,61), 2, -1, True, self.frames, False),#daño izq  

                        SpriteStripAnim('Personajes/LazerSheet.png', (0,315,90,57), 1, -1, True, self.frames, True)+
                        SpriteStripAnim('Personajes/LazerSheet.png', (92,315,115,57), 1, -1, True, self.frames, True),#ATk der
                        SpriteStripAnim('Personajes/LazerSheet.png', (0,315,90,57), 1, -1, True, self.frames, False)+
                        SpriteStripAnim('Personajes/LazerSheet.png', (92,315,115,57), 1, -1, True, self.frames, False)#ATk izq 
                        ]                  
        
        elif personaje== 4:
            self.Sound_ATK= pg.mixer.Sound("Sounds/titi.ogg")
            self.ataque = 3
            self.defensa = 3
            self.velocidad = 3
            if self.skin:
                self.Perro = [
                    SpriteStripAnim('Personajes/TitiSheet2.png', (0,0,72,64), 2, -1, True, self.frames, True),  #Standby derecha
                    SpriteStripAnim('Personajes/TitiSheet2.png', (0,0,72,64), 2, -1, True, self.frames, False), #Standby izquierda

                    SpriteStripAnim('Personajes/TitiSheet2.png', (0,65,72,65), 2, -1, True, self.frames, True),  #Movimiento derecha
                    SpriteStripAnim('Personajes/TitiSheet2.png', (0,65,72,65), 2, -1, True, self.frames, False), #Movimiento izquierda

                    SpriteStripAnim('Personajes/TitiSheet2.png', (0,195,72,65), 1, -1, True, self.frames, True),  #Jump derecha
                    SpriteStripAnim('Personajes/TitiSheet2.png', (0,195,72,65), 1, -1, True, self.frames, False), #Jump izquierda

                    SpriteStripAnim('Personajes/TitiSheet2.png', (144,195,72,63), 1, -1, True, self.frames, True),  #caida derecha
                    SpriteStripAnim('Personajes/TitiSheet2.png', (144,195,72,63), 1, -1, True, self.frames, False), #caida izquierda

                    SpriteStripAnim('Personajes/TitiSheet2.png', (144,130,69,64), 2, -1, True, self.frames, True),  #Daño der
                    SpriteStripAnim('Personajes/TitiSheet2.png', (144,130,69,64), 2, -1, True, self.frames, False),  #Daño izq

                    SpriteStripAnim('Personajes/TitiSheet2.png', (0,325,92,61), 2, -1, True, self.frames, True),  #Daño der
                    SpriteStripAnim('Personajes/TitiSheet2.png', (0,325,92,61), 2, -1, True, self.frames, False)  #Daño izq
                    ]
            else:
                self.Perro = [
                    SpriteStripAnim('Personajes/TitiSheet.png', (0,0,72,64), 2, -1, True, self.frames, True),  #Standby derecha
                    SpriteStripAnim('Personajes/TitiSheet.png', (0,0,72,64), 2, -1, True, self.frames, False), #Standby izquierda

                    SpriteStripAnim('Personajes/TitiSheet.png', (0,65,72,65), 2, -1, True, self.frames, True),  #Movimiento derecha
                    SpriteStripAnim('Personajes/TitiSheet.png', (0,65,72,65), 2, -1, True, self.frames, False), #Movimiento izquierda

                    SpriteStripAnim('Personajes/TitiSheet.png', (0,195,72,65), 1, -1, True, self.frames, True),  #Jump derecha
                    SpriteStripAnim('Personajes/TitiSheet.png', (0,195,72,65), 1, -1, True, self.frames, False), #Jump izquierda

                    SpriteStripAnim('Personajes/TitiSheet.png', (144,195,72,63), 1, -1, True, self.frames, True),  #caida derecha
                    SpriteStripAnim('Personajes/TitiSheet.png', (144,195,72,63), 1, -1, True, self.frames, False), #caida izquierda

                    SpriteStripAnim('Personajes/TitiSheet.png', (144,130,70,64), 2, -1, True, self.frames, True),  #Daño der
                    SpriteStripAnim('Personajes/TitiSheet.png', (144,130,70,64), 2, -1, True, self.frames, False),  #Daño izq

                    SpriteStripAnim('Personajes/TitiSheet.png', (0,325,92,61), 2, -1, True, self.frames, True),  #Daño der
                    SpriteStripAnim('Personajes/TitiSheet.png', (0,325,92,61), 2, -1, True, self.frames, False)  #Daño izq
                    ] 

        elif personaje ==5:
            self.Sound_ATK= pg.mixer.Sound("Sounds/solrac.ogg")
            self.ataque = 4
            self.defensa = 1
            self.velocidad = 4
            if self.skin:
                self.Perro= [
                            SpriteStripAnim(solrac , (0,0,143,70), 3, -1, True, self.frames, True),  #Standby der
                            SpriteStripAnim(solrac, (0,0,143,70), 3, -1, True, self.frames, False), #standby izq

                            SpriteStripAnim(solrac, (0,70,128,70), 3, -1, True, self.frames, True),  #mov der
                            SpriteStripAnim(solrac, (0,70,128,70), 3, -1, True, self.frames, False), #mov izq

                            SpriteStripAnim(solrac, (0,140,100,104), 1, -1, True, self.frames, True),  #Jump der
                            SpriteStripAnim(solrac, (0,140,100,104), 1, -1, True, self.frames, False), #Jump izq

                            SpriteStripAnim(solrac, (0,244,117,63), 1, -1, True, self.frames, True),  #caida der
                            SpriteStripAnim(solrac, (0,244,117,63), 1, -1, True, self.frames, False), #caida izq

                            SpriteStripAnim(solrac, (247,397,120,61), 1, -1, True, self.frames, True),  #daño der
                            SpriteStripAnim(solrac, (247,397,120,61), 1, -1, True, self.frames, False),  #daño izq

                            SpriteStripAnim(solrac, (0,481,180,70), 2, -1, True, self.frames, True),  #ATK der
                            SpriteStripAnim(solrac, (0,481,180,70), 2, -1, True, self.frames, False)  #ATK izq
                            ]
            else:            
                self.Perro= [
                            SpriteStripAnim('Personajes/SolracSheet2.png', (0,0,143,70), 6, -1, True, self.frames, True),  #Standby der
                            SpriteStripAnim('Personajes/SolracSheet2.png', (0,0,143,70), 6, -1, True, self.frames, False), #standby izq

                            SpriteStripAnim('Personajes/SolracSheet2.png', (0,70,128,70), 4, -1, True, self.frames, True),  #mov der
                            SpriteStripAnim('Personajes/SolracSheet2.png', (0,70,128,70), 4, -1, True, self.frames, False), #mov izq

                            SpriteStripAnim('Personajes/SolracSheet2.png', (0,140,100,104), 1, -1, True, self.frames, True),  #Jump der
                            SpriteStripAnim('Personajes/SolracSheet2.png', (0,140,100,104), 1, -1, True, self.frames, False), #Jump izq

                            SpriteStripAnim('Personajes/SolracSheet2.png', (0,244,117,63), 1, -1, True, self.frames, True),  #caida der
                            SpriteStripAnim('Personajes/SolracSheet2.png', (0,244,117,63), 1, -1, True, self.frames, False), #caida izq

                            SpriteStripAnim('Personajes/SolracSheet2.png', (247,397,120,61), 1, -1, True, self.frames, True),  #daño der
                            SpriteStripAnim('Personajes/SolracSheet2.png', (247,397,120,61), 1, -1, True, self.frames, False) , #daño izq

                            SpriteStripAnim('Personajes/SolracSheet2.png', (0,481,180,70), 2, -1, True, self.frames, True),  #ATK der
                            SpriteStripAnim('Personajes/SolracSheet2.png', (0,481,180,70), 2, -1, True, self.frames, False)  #ATK izq
                            ] 

        self.Perro[self.n].iter()
        self.image= self.Perro[self.n].next()
        
        self.rect = self.image.get_rect() #crea ractangulo de bordes de imagen

        self.respawn = respawn #pos de inicio y reicnio del jugador
        self.pos = vec(self.respawn, alto_ventana/2) #vector posicion
        self.vel = vec(0,0) #vector velocidad
        self.acc = vec(0,0) #vector aceleracion

        self.mov_izq = mov_izq #Boton movimiento izquierda
        self.mov_der = mov_der #Boton movimiento derecha
        self.numRandomGolpes= rd.randint(3, 5)

        self.saltosDisponibles = 0 #disponibilidad del doble salto
        self.saltando =False #chequea si esta saltando
        self.enPlataforma = None #chequeo si esta en plataforma
        self.direccion = direccion #dereccion del jugador
        self.vidas = game.m.opcionesVidas #CANTIDAD DE VIDAS
        self.golpeado = None #chequeo cuando es golpeado
        self.EsperaGolpe =0 #tiempo de espera de estado golpeado
        self.golpes =0 #cantidad de golpes recibidos
        self.dañoActual = 0 #daño recibido
        self.esperaRespawn= 0
        self.contadorGolpe = 0
        self.joystick= movJoystick
        self.ATk= False
        self.x=0

    def goLeft(self):
        keys = pg.key.get_pressed() 
        if self.joystick != None:
            if self.joystick.get_axis(0) == -1:
                self.acc.x = -(aceleracion + aceleracion*(self.velocidad-2)*0.25)
                self.direccion=False

        if keys[self.mov_izq] :
            self.acc.x = -(aceleracion + aceleracion*(self.velocidad-2)*0.25)
            self.direccion=False


    def goRigth(self):
        keys = pg.key.get_pressed() 
        if self.joystick != None:
            if self.joystick.get_axis(0) > 0.1:
                self.acc.x = (aceleracion + aceleracion*(self.velocidad-2)*0.25)
                self.direccion=True

        if keys[self.mov_der] :
            self.acc.x = (aceleracion + aceleracion*(self.velocidad-2)*0.25)
            self.direccion=True

    def update(self): 
        # ACTUALIZACIONES DEL PERSONAJE
        self.grav() 
        self.contadorGolpe+=1 
        #---------------------------------------------------------------------------------------
        #Movimiento izq/der precionando botones
        if self.golpeado:
            self.EsperaGolpe+=1
            if self.direccion:
                self.n =8  
            else:
                self.n =9
            if self.EsperaGolpe == 5:
                    self.golpeado =False 
                    self.golpes= 0    

        elif not self.golpeado:
            self.EsperaGolpe= 0    
            

            self.goLeft()
            self.goRigth()

            if self.ATk:
                self.x+=1
                if self.direccion:
                    self.n =10
                else:
                    self.n =11 
                if self.x == 20:
                    self.ATk= False
                    self.x= 0
            else:
                if self.vel.x > 0:
                    self.n=2

                elif self.vel.x < 0:
                    self.n=3

                if self.vel.y < 0 :
                    if self.direccion==True:
                        self.n =4
                    else:
                        self.n =5

                elif self.vel.y >0:
                    if self.direccion==True:
                        self.n =6
                    else:
                        self.n =7  

                elif self.n>0 and self.acc.x==0 :
                    if self.direccion==True:
                        self.n =0
                    else:
                        self.n =1


        "Ejecucion de la fisica de movimiento en X"
        # implementacion de la friccion en eje x
        self.acc.x += self.vel.x * friccion

        # movimiento (ecuac. de mov)
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # colicion con los bordes de la pantalla
        if self.pos.x > ancho_ventana+100 or self.pos.x < 0-100 or self.pos.y > alto_ventana+250:
            self.esperaRespawn+=1
            if self.esperaRespawn == 50:
                self.vel.y = 0
                self.pos.x = rd.randint(ancho_ventana/4,ancho_ventana-ancho_ventana/4)
                self.pos.y = alto_ventana/2
                self.vidas-=1
                self.dañoActual = 0
                self.esperaRespawn = 0 
                
            
        self.rect.midbottom = self.pos

        self.image = self.Perro[self.n].next()

        if self.dañoActual > 0:
            if ((self.contadorGolpe>300) and (self.contadorGolpe % 24 == 0)):
                self.dañoActual -= 3
                if self.dañoActual < 0:
                    self.dañoActual = 0

    def grav(self):
        #GRAVEDAD
        self.acc = vec(0,gravedad)

    def jump(self):
        #DOBLE SALTO 
        if self.saltosDisponibles > 0:
            self.vel.y = - salto
            self.saltosDisponibles = self.saltosDisponibles - 1
            self.enPlataforma = False
            self.saltando = True
            self.game.Sound_salto.play()

    def chequear_Salto(self):
        # CHEQUEO SI ESA SALTANDO EL PERSONAJE
        if self.enPlataforma:
            self.saltosDisponibles = 2

    def returnVidasActuales(self):
        return self.vidas

    def golpe(self, enemigo):
        if (self.direccion == True and (enemigo.getRect().left < self.rect.right + 1 < enemigo.getRect().right) or (enemigo.getRect().left < self.rect.right + 1 < enemigo.getRect().right )) or (self.direccion == False and (enemigo.getRect().left < self.rect.left + 1 < enemigo.getRect().right) or (enemigo.getRect().left < self.rect.left + 1 < enemigo.getRect().right)):
            if (enemigo.getRect().top < (self.rect.top+self.rect.bottom)/2 < enemigo.getRect().bottom):
                enemigo.recibirGolpe(self.direccion, self.ataque)
                self.ATk= True
                self.Sound_ATK.play()
                self.Sound_ATK.set_volume(.5)
            
    def recibirGolpe(self, direccion, ataque):
        self.golpes+=1
        self.game.Sound_Golpe.play()
        self.dañoActual+= 20 +int((ataque - self.defensa)*4)
        self.contadorGolpe = 0
        
        if direccion:
            self.vel.x += 2 +(0.15*self.dañoActual)
            self.vel.y -= 0.1 +(0.04*self.dañoActual)
        else:
            self.vel.x -= 2  +(0.15*self.dañoActual)
            self.vel.y -= 0.1  +(0.04*self.dañoActual)

        if self.golpes == rd.randint(1, 5) or self.golpes == 5:
            self.golpeado =True        

    def getDañoActual(self):
        return self.dañoActual                
        
    def getRect(self):
        return self.rect
