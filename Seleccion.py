"SELECCION PERSONAJES"
import pygame as pg
from pygame.locals import *
from Sprites import *
from Constantes import *
from Game import *

class Seleccion:
	def __init__(self, menu):
		"VARIABLES"	
		self.menu= menu	
		self.Seleccion_on= True
		self.inSeleccion= True
		self.seleccioActual= 0

		"VARIABLES SELECCION DE JUGADORES"
		self.fondoSeleccionPersonaje = load_image("SelectScreen.png", "img", alpha=False)
		self.cursorPlayer1 = load_image("SeleccionPrimerPlayer.png", "img/cursor", alpha=False)
		self.cursorPlayer2 = load_image("SeleccionSegundoPlayer.png", "img/cursor", alpha=False)
		self.seleccion1 = load_image("PrimerPlayer_SELECT.png", "img/cursor", alpha=False)
		self.seleccion2 = load_image("SegundoPlayer_SELECT.png", "img/cursor", alpha=False)
		self.pate = load_image("Pate Select.png", "img", alpha=False)
		self.choco = load_image("Chocolate Select.png", "img", alpha=False)
		self.rayo = load_image("Rayo Select.png", "img", alpha=False)
		self.titi = load_image("Titi Select.png", "img", alpha=False)
		self.solrac = load_image("Solrac Select.png", "img", alpha= False)

		self.estadisticasTiti= load_image("EstadisticasTiti.png", "img", alpha= False)
		self.estadisticasChoco= load_image("EstadisticasChoco.png", "img", alpha= False)
		self.estadisticasPate= load_image("EstadisticasPate.png", "img", alpha= False)
		self.estadisticasLazer= load_image("EstadisticasLazer.png", "img", alpha= False)
		self.estadisticasSolrac= load_image("EstadisticasSorlac.png", "img", alpha= False)

		self.opcion_P1= 1
		self.opcion_P2= 4
		self.selectP1= False
		self.selectP2= False
		self.pos_cursorP1= 31
		self.pos_cursorP2= 592
		self.pj_RepetidoP2= False
		self.Seguir = False
		self.win_P1= 0
		self.win_P2= 0

		self.perro = [SpriteStripAnim(pate,(0,0,112.5,75), 3, -1, True, 8, True ),
				SpriteStripAnim(choco,(0,241,105,60), 3, -1, True, 8, True ),
				SpriteStripAnim(rayo, (0,0,73,61), 2, -1, True, 8, True),
				SpriteStripAnim(titi, (0,0,72,64), 2, -1, True, 8, True),
				SpriteStripAnim(solrac, (0,0,143,70),6, -1, True, 8, True)
				]
		self.perro[self.opcion_P1-1].iter()
		self.imagenAnim= self.perro[self.opcion_P1-1].next()

		self.dog = [SpriteStripAnim(pate,(0,0,112.5,75), 3, -1, True, 8, False ),
				SpriteStripAnim(choco,(0,241,105,60), 3, -1, True, 8, False ),
				SpriteStripAnim(rayo, (0,0,73,61), 2, -1, True, 8, False),
				SpriteStripAnim(titi, (0,0,72,64), 2, -1, True, 8, False),
				SpriteStripAnim(solrac, (0,0,143,70),6, -1, True, 8, False)
				]
		self.dog[self.opcion_P2-1].iter()
		self.imgAnim= self.dog[self.opcion_P2-1].next()

		"VARIBLES SELECION DE ESCENARIO"
		self.fondoSeleccionEscenario= load_image("MENU.png", "img/seleccion_etapa", alpha= False)
		self.cursorEscenarios= load_image("Seleccion.png", "img/seleccion_etapa", alpha= False)
		self.imgPastito= load_image("Pastito_Grande.png", "img/seleccion_etapa", alpha= False)
		self.imgHawaii= load_image("Hawaii_Grande.png", "img/seleccion_etapa", alpha= False)
		self.imgCasino= load_image("Casino_Grande.png", "img/seleccion_etapa", alpha= False)
		self.imgBioMarina= load_image("Biologia_Marina_Grande.png", "img/seleccion_etapa", alpha= False)
		self.pastito= load_image("Pastito_Mini.png", "img/seleccion_etapa", alpha= False)
		self.hawai= load_image("Hawaii_Mini.png", "img/seleccion_etapa", alpha= False)
		self.casino= load_image("Casino_Mini.png", "img/seleccion_etapa", alpha= False)
		self.bioMarina= load_image("Biologia_Marina_Mini.png", "img/seleccion_etapa", alpha= False)
		self.bioMarina_Lock= load_image("Biologia_Marina_Lock.png", "img/seleccion_etapa", alpha= False)

		self.opcionEscenario= 1
		self.pos_cursorEscenario= 20
		self.movim= 4
		self.unlockDog = False
		self.unlockStage = False

	def run(self):
		while self.inSeleccion:
			self.menu.clock.tick(FPS)
			self.event()
			self.draw()

		if self.Seguir:
			while self.g.game_on:
				self.g.run()

	def event(self):
		for event in pg.event.get():

			if self.inSeleccion:
				if self.win_P1 + self.win_P2 == 2:
					self.unlockDog = True
				if self.win_P1 + self.win_P2 == 3:
					self.unlockStage = True
				self.keys = pg.key.get_pressed()
                        
				if event.type == pg.QUIT:
					sys.exit()
				if self.seleccioActual == 0:
					if not self.selectP1:
						if self.keys[K_a] or (self.menu.mandos_on == True and (self.menu.mandos[0].get_axis(0) == -1)):
							if self.opcion_P1 > 1:
								self.opcion_P1 -= 1
								self.pos_cursorP1 -= 187
						if self.keys[K_d] or (self.menu.mandos_on == True  and (self.menu.mandos[0].get_axis(0) > 0.1)):
							if self.opcion_P1 < 4 or (self.unlockDog and self.opcion_P1 < 5):
								self.opcion_P1 += 1
								self.pos_cursorP1 += 187
						if self.keys[K_LSHIFT] or (self.menu.mandos_on == True and (event.type == pg.JOYBUTTONDOWN and self.menu.mandos[0].get_button(2) == 1)):
							self.selectP1= True
					if not self.selectP2:
						if self.keys[K_LEFT] or (self.menu.mandos_on == True and self.menu.num_mandos == 2 and (self.menu.mandos[1].get_axis(0) == -1)):
							if self.opcion_P2 > 1:
								self.opcion_P2 -= 1
								self.pos_cursorP2 -= 187
						if self.keys[K_RIGHT] or (self.menu.mandos_on == True and self.menu.num_mandos == 2 and (self.menu.mandos[1].get_axis(0) > 0.1)):
							if self.opcion_P2 < 4 or (self.unlockDog and self.opcion_P2 < 5):
								self.opcion_P2 += 1
								self.pos_cursorP2 += 187
						if self.keys[K_RETURN] or (self.menu.mandos_on == True and self.menu.num_mandos == 2 and (event.type == pg.JOYBUTTONDOWN and self.menu.mandos[1].get_button(2) == 1)):
							self.selectP2= True

					if self.keys[K_TAB] or (self.menu.mandos_on == True and (event.type == pg.JOYBUTTONDOWN and self.menu.mandos[0].get_button(1) == 1)):
						self.selectP1 = False
					if self.keys[K_BACKSPACE] or (self.menu.mandos_on == True and self.menu.num_mandos == 2 and (event.type == pg.JOYBUTTONDOWN and self.menu.mandos[1].get_button(1) == 1)): 
						self.selectP2 = False

					if self.opcion_P1 == self.opcion_P2:
						self.pj_RepetidoP2= True

					if self.selectP1 and self.selectP2:
						if event.type == pg.KEYDOWN or event.type == pg.JOYBUTTONDOWN:
							self.seleccioActual = 1

					if (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE ):
						self.menu.inMenu= True
						self.inSeleccion= False
						self.Seleccion_on= False
						self.menu.Sound_Menu.stop()

				
				elif self.seleccioActual == 1:
					if self.keys[K_UP] or self.keys[K_w] or (self.menu.mandos_on == True and (self.menu.mandos[0].get_axis(1)== -1)):
						if self.opcionEscenario >1:
							self.opcionEscenario -= 1
							self.pos_cursorEscenario -= 130
					if self.keys[K_DOWN] or self.keys[K_s] or (self.menu.mandos_on == True and (self.menu.mandos[0].get_axis(1) > 0.1)):
						if self.opcionEscenario < 3 or (self.unlockStage and self.opcionEscenario < 4):
							self.opcionEscenario += 1
							self.pos_cursorEscenario += 130
					if self.keys[K_RETURN] or self.keys[K_LSHIFT] or (self.menu.mandos_on == True and (event.type == pg.JOYBUTTONDOWN and self.menu.mandos[0].get_button(2) == 1)):
						self.Seguir= True
						self.inSeleccion= False
						self.g= Game(self, self.menu)
						self.menu.Sound_Menu.stop() 

					if (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE ):
						self.seleccioActual= 0
						self.selectP1= False
						self.selectP2= False
						
										

	def draw(self):
		if self.inSeleccion:
			if self.seleccioActual == 0:
				self.menu.ventana.blit(self.fondoSeleccionPersonaje, (0,0))
				self.menu.ventana.blit(self.pate, (31, 376))
				self.menu.ventana.blit(self.choco, (218, 376))
				self.menu.ventana.blit(self.rayo, (405, 376))
				self.menu.ventana.blit(self.titi, (592, 376))
				self.menu.ventana.blit(self.solrac, (779, 376))

				self.menu.ventana.blit(self.cursorPlayer1, (self.pos_cursorP1, 376))
				self.menu.ventana.blit(self.cursorPlayer2, (self.pos_cursorP2, 376))

				self.menu.dibujar_texto("Ganadas P1: "+str(self.win_P1), 22, GREEN, ancho_ventana/8, alto_ventana -alto_ventana/2.5)
				self.menu.dibujar_texto("Ganadas P2: "+str(self.win_P2), 22, RED, ancho_ventana - ancho_ventana/8, alto_ventana -alto_ventana/2.5)

				if self.selectP1:
					self.menu.ventana.blit(self.seleccion1, (self.pos_cursorP1, 376))
				if self.selectP2:
					self.menu.ventana.blit(self.seleccion2, (self.pos_cursorP2, 376))

				self.menu.ventana.blit(self.imagenAnim,(140, 125) )
				self.imagenAnim= self.perro[self.opcion_P1-1].next()

				self.menu.ventana.blit(self.imgAnim,(700, 125))
				self.imgAnim= self.dog[self.opcion_P2-1].next()

				if self.opcion_P1 == 1:
					self.estadistica= self.estadisticasPate
				if self.opcion_P1 == 2:

					self.estadistica= self.estadisticasChoco
				if self.opcion_P1 == 3:
					self.estadistica= self.estadisticasLazer
				if self.opcion_P1 == 4:
					self.estadistica= self.estadisticasTiti
				if self.opcion_P1 == 5:
					self.estadistica= self.estadisticasSolrac
				self.menu.ventana.blit(self.estadistica, (150,220))

				if self.opcion_P2 == 1:
					self.estadis= self.estadisticasPate
				if self.opcion_P2 == 2:
					self.estadis= self.estadisticasChoco
				if self.opcion_P2 == 3:
					self.estadis= self.estadisticasLazer
				if self.opcion_P2 == 4:
					self.estadis= self.estadisticasTiti
				if self.opcion_P2 == 5:
					self.estadis= self.estadisticasSolrac
				self.menu.ventana.blit(self.estadis, (710,220))



			elif self.seleccioActual == 1:
				self.menu.ventana.blit(self.fondoSeleccionEscenario, (0,0))
				self.menu.ventana.blit(self.pastito,(15, 20))
				self.menu.ventana.blit(self.hawai, (15,150))
				self.menu.ventana.blit(self.casino, (15, 280))
				if self.unlockStage:
					self.menu.ventana.blit(self.bioMarina, (15, 410))
				else:
					self.menu.ventana.blit(self.bioMarina_Lock, (15, 410))
				
				self.menu.ventana.blit(self.cursorEscenarios, (15,self.pos_cursorEscenario))

				if self.opcionEscenario==1:
					self.imgEscenario= self.imgPastito
				if self.opcionEscenario==2:
					self.imgEscenario= self.imgHawaii
				if self.opcionEscenario==3:
					self.imgEscenario= self.imgCasino
				if self.opcionEscenario== 4:
					self.imgEscenario= self.imgBioMarina
				self.menu.ventana.blit(self.imgEscenario, (232, 65))

		pg.display.flip()



