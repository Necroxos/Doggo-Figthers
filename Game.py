"Game"
import pygame as pg
from pygame.locals import *
from Sprites import *
from Constantes import *
from Jugador import *
from Plataformas import*

class Game:
	def __init__(self, seleccion, menu):
		self.m= menu
		self.s= seleccion
		self.game_on= True
		self.inGame= True
		self.prioridad = 1

		self.Sound_BioMar = pg.mixer.Sound('Sounds/BioMarina.ogg')
		self.Sound_Golpe = pg.mixer.Sound("Sounds/Golpe.wav")
		self.Sound_salto = pg.mixer.Sound("Sounds/Salto.wav")
		
		self.SheetVidas = [SpriteStripAnim('img/SheetVidas.png', (0,0,20,20), 1, -1, True, 0, True),
							SpriteStripAnim('img/SheetVidas.png', (20,0,20,20), 1, -1, True, 0, True),
							SpriteStripAnim('img/SheetVidas.png', (40,0,20,20), 1, -1, True, 0, True),
							SpriteStripAnim('img/SheetVidas.png', (60,0,20,20), 1, -1, True, 0, True),
							SpriteStripAnim('img/SheetVidas.png', (80,0,20,20), 1, -1, True, 0, True)]
		self.SheetVidas[self.s.opcion_P1-1].iter()
		self.imgVida_P1= self.SheetVidas[self.s.opcion_P1-1].next()

		self.SheetVidas[self.s.opcion_P1-1].iter()
		self.imgVida_P2= self.SheetVidas[self.s.opcion_P2-1].next()

		self.P1_indice= load_image("P1.png", "img/cursor", False)
		self.P2_indice= load_image("P2.png", "img/cursor", False)

		self.fondo2= load_image("Hawaii.png", "img/ecenarios", False)
		self.fondo1= load_image("Pastito.png", "img/ecenarios", False)
		self.fondo3= load_image("Casino.png", "img/ecenarios", False)
		self.fondo4= load_image("BiologiaMarina.png", "img/ecenarios", False)

		self.Pausa = load_image("Pausa.png", "img", False)
		self.menuPausa = False

		self.pantallaGanador = False

		self.dead_P1= False
		self.dead_P2= False

		self.setPlayer()

	def setPlayer(self):
		self.players_sprites = pg.sprite.Group()
		self.P1 = pg.sprite.Group()
		self.P2 = pg.sprite.Group()
		self.plataformas_sprites = pg.sprite.Group()

		if len(self.m.mandos) == 0:
			JoyP1= None
			JoyP2= None
		else:
			if len(self.m.mandos)==1:
				JoyP1= self.m.mandos[0]
				JoyP2= None
			else:
				JoyP1= self.m.mandos[0]
				JoyP2= self.m.mandos[1]

		self.player_1 = Player(self, self.s.opcion_P1, P1_Der, P1_Izq, P1_Dir, JoyP1, P1_respawn)
		self.P1.add(self.player_1)

		self.player_2 = Player(self, self.s.opcion_P2, P2_Der, P2_Izq, P2_Dir, JoyP2, P2_respawn, self.s.pj_RepetidoP2 )
		self.P2.add(self.player_2)

		if self.s.opcionEscenario == 1:
			self.plataforma_1 = Plataform(74,180,270,10)
			self.plataformas_sprites.add(self.plataforma_1)
			self.plataforma_2 = Plataform(592,219,270,10)
			self.plataformas_sprites.add(self.plataforma_2)
			self.plataforma_3 = Plataform(231,306,260,10)
			self.plataformas_sprites.add(self.plataforma_3)
			self.plataforma_4 = Plataform(84,420,250,10)
			self.plataformas_sprites.add(self.plataforma_4)
			self.plataforma_5 = Plataform(590,426,250,10)
			self.plataformas_sprites.add(self.plataforma_5)

		elif self.s.opcionEscenario == 2:
			self.plataforma_1 = Plataform(146,182,253,10)
			self.plataformas_sprites.add(self.plataforma_1)
			self.plataforma_2 = Plataform(586,225,219,10)
			self.plataformas_sprites.add(self.plataforma_2)
			self.plataforma_3 = Plataform(161,342,638,20)
			self.plataformas_sprites.add(self.plataforma_3)

		elif self.s.opcionEscenario == 3:
			self.plataforma_1 = Plataform(134,360,258,30)
			self.plataformas_sprites.add(self.plataforma_1)
			self.plataforma_2 = Plataform(538,359,258,30)
			self.plataformas_sprites.add(self.plataforma_2)
			self.plataforma_3 = Plataform(325,239,272,10)
			self.plataformas_sprites.add(self.plataforma_3)
			self.plataforma_4 = Plataform(546,132,259,20)
			self.plataformas_sprites.add(self.plataforma_4)
			self.plataforma_5 = Plataform(126,100,259,20)
			self.plataformas_sprites.add(self.plataforma_5)

		elif self.s.opcionEscenario == 4:
			self.plataforma_1 = Plataform(56,266,236,20)
			self.plataformas_sprites.add(self.plataforma_1)
			self.plataforma_2 = Plataform(307,400,238,20)
			self.plataformas_sprites.add(self.plataforma_2)
			self.plataforma_3 = Plataform(676,358,187,10)
			self.plataformas_sprites.add(self.plataforma_3)
			self.plataforma_4 = Plataform(762,226,188,20)
			self.plataformas_sprites.add(self.plataforma_4)
			self.plataforma_5 = Plataform(307,145,308,20)
			self.plataformas_sprites.add(self.plataforma_5)



	def run(self): 
		self.Sound_BioMar.play(-1)
		self.Sound_BioMar.set_volume(.25)

		while self.inGame:
			self.player_1.chequear_Salto()
			self.player_2.chequear_Salto()
			self.m.clock.tick(FPS)
			self.event()
			if not self.menuPausa:
				self.update()
			if self.player_1.returnVidasActuales() == 0 or self.player_2.returnVidasActuales() == 0:
				self.inGame= False
				self.pantallaGanador= True
				self.StringGanador= "El GANADOR es el JUGADOR "

				if self.player_1.returnVidasActuales() == 0:
					self.StringGanador += "2"
					self.s.win_P2 +=1
				elif self.player_2.returnVidasActuales() == 0:
					self.StringGanador += "1"
					self.s.win_P1 += 1
			self.draw()

		while self.pantallaGanador:
			self.m.clock.tick(FPS)
			self.event()
			self.draw()

	def event(self):
		for event in pg.event.get():
			self.keys = pg.key.get_pressed()
			if event.type == pg.QUIT:
				sys.exit()
			if self.pantallaGanador:
				if self.keys[K_ESCAPE] or (self.m.mandos_on == True and (event.type == pg.JOYBUTTONDOWN and (self.m.mandos[0].get_button(9) == 1 or (self.m.num_mandos == 2 and self.m.mandos[1].get_button(9) == 1) ))):
					self.pantallaGanador= False
					self.game_on= False
					self.s.inSeleccion= True
					self.s.seleccioActual= 0
					self.s.opcion_P1= 1
					self.s.opcion_P2= 4
					self.s.selectP1= False
					self.s.selectP2= False
					self.s.pos_cursorP1= 31
					self.s.pos_cursorP2= 592
					self.s.pj_RepetidoP1= False
					self.s.opcionEscenario= 1
					self.s.pos_cursorEscenario= 20
					self.m.Sound_Menu.play(-1)
					self.Sound_BioMar.stop()

			elif self.menuPausa:
				self.Sound_BioMar.stop()
				if self.keys[K_ESCAPE] or (self.m.mandos_on == True and (event.type == pg.JOYBUTTONDOWN and (self.m.mandos[0].get_button(9) == 1 or (self.m.num_mandos == 2 and self.m.mandos[1].get_button(9) == 1) ))):
					self.menuPausa= False
					self.Sound_BioMar.play(-1)
				if self.keys[K_RETURN] or (self.m.mandos_on == True and (event.type == pg.JOYBUTTONDOWN and (self.m.mandos[0].get_button(5) == 1 or (self.m.num_mandos == 2 and self.m.mandos[1].get_button(5) == 1) ))):
					self.inGame= False
					self.game_on= False
					self.s.inSeleccion= True
					self.s.seleccioActual= 0
					self.s.opcion_P1= 1
					self.s.opcion_P2= 4
					self.s.selectP1= False
					self.s.selectP2= False
					self.s.pos_cursorP1= 31
					self.s.pos_cursorP2= 592
					self.s.pj_RepetidoP1= False
					self.s.opcionEscenario= 1
					self.s.pos_cursorEscenario= 20
					self.m.Sound_Menu.play(-1)
				if self.keys[K_1] or (self.m.mandos_on == True and (event.type == pg.JOYBUTTONDOWN and (self.m.mandos[0].get_button(6) == 1 or (self.m.num_mandos == 2 and self.m.mandos[1].get_button(6) == 1) ))):
					self.inGame= False
					self.game_on= False
					self.s.inSeleccion= False
					self.s.Seleccion_on= False
					self.m.inMenu= True
					
			else:
				if (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE ) or (self.m.mandos_on == True and (event.type == pg.JOYBUTTONDOWN and (self.m.mandos[0].get_button(9) == 1 or (self.m.num_mandos == 2 and self.m.mandos[1].get_button(9) == 1) ))):
					self.menuPausa = True
				if not self.menuPausa:
					if not self.player_1.golpeado:
						if event.type == pg.KEYDOWN and event.key == pg.K_LSHIFT  or (self.m.mandos_on == True and (event.type == pg.JOYBUTTONDOWN and self.m.mandos[0].get_button(3) == 1)):
							self.player_1.golpe(self.player_2)
							self.prioridad = 2


						if event.type == pg.KEYDOWN and event.key == pg.K_w or (self.m.mandos_on == True and (event.type == pg.JOYBUTTONDOWN and self.m.mandos[0].get_button(2) == 1)):
							self.player_1.jump()

					if not self.player_2.golpeado:
						if event.type == pg.KEYDOWN and event.key == pg.K_RSHIFT or (self.m.mandos_on == True and self.m.num_mandos == 2 and (event.type == pg.JOYBUTTONDOWN and self.m.mandos[1].get_button(3) == 1)):
							self.player_2.golpe(self.player_1)
							self.prioridad = 1

						if event.type == pg.KEYDOWN and event.key == pg.K_UP or (self.m.mandos_on == True and self.m.num_mandos == 2 and (event.type == pg.JOYBUTTONDOWN and self.m.mandos[1].get_button(2) == 1)):
							self.player_2.jump()

	def update(self):
		self.P1.update()
		self.P2.update()
		self.plataformas_sprites.update()

		if self.player_1.vel.y > 0:
			hits = pg.sprite.spritecollide(self.player_1,self.plataformas_sprites, False)
			if hits:
				if hits[0].rect.top - 10 < self.player_1.pos.y < hits[0].rect.bottom + 10:
					self.player_1.vel.y = 0
					self.player_1.pos.y = hits[0].rect.top 
					self.player_1.enPlataforma = True

		if self.player_2.vel.y > 0:
			hits = pg.sprite.spritecollide(self.player_2,self.plataformas_sprites, False)
			if hits:
				if hits[0].rect.top - 10 < self.player_2.pos.y < hits[0].rect.bottom + 10:
					self.player_2.vel.y = 0
					self.player_2.pos.y = hits[0].rect.top 
					self.player_2.enPlataforma = True

	def draw(self):
		if self.pantallaGanador:
			
			self.m.dibujar_texto(self.StringGanador, 56, GREEN, 960/2 ,alto_ventana/2)

		elif self.menuPausa:
			self.m.ventana.blit(self.Pausa, (0,0))
		else:
			if self.s.opcionEscenario == 1:
				self.fondo= self.fondo1
			if self.s.opcionEscenario== 2:
				self.fondo= self.fondo2
			if self.s.opcionEscenario == 3:
				self.fondo= self.fondo3
			if self.s.opcionEscenario== 4:
				self.fondo= self.fondo4
			self.m.ventana.blit(self.fondo, (0,0))

			if self.prioridad == 1:
				self.P1.draw(self.m.ventana)
				self.m.ventana.blit(self.P1_indice,self.player_1.pos)
				self.P2.draw(self.m.ventana)
				self.m.ventana.blit(self.P2_indice,self.player_2.pos)
			else:
				self.P2.draw(self.m.ventana)
				self.m.ventana.blit(self.P2_indice,self.player_2.pos)
				self.P1.draw(self.m.ventana)
				self.m.ventana.blit(self.P1_indice,self.player_1.pos)
					
			self.plataformas_sprites.draw(self.m.ventana)
			
			if self.player_1.vidas >0:
				for i in range(self.player_1.vidas):
					self.m.ventana.blit(self.imgVida_P1,(100+20*i, 500))
				self.imgVida_P1= self.SheetVidas[self.s.opcion_P1-1].next()

			if self.player_2.vidas >0:
				for i in range(self.player_2.vidas):
					self.m.ventana.blit(self.imgVida_P2, (800+20*i, 500))
				self.imgVida_P2= self.SheetVidas[self.s.opcion_P2-1].next()

			self.m.dibujar_texto(str(self.player_1.getDañoActual())+"%", 24, WHITE, 100, 450)
			self.m.dibujar_texto(str(self.player_2.getDañoActual())+"%", 24, WHITE, 800, 450)

		pg.display.flip()
