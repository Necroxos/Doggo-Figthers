"Menu"
import pygame as pg
from pygame.locals import *
from Constantes import *
from Seleccion import *

class Menu:
	def __init__(self):
		"INICIALIZACIONES DEL JUEGO"
		pg.init()
		pg.mixer.init()
		pg.joystick.init()

		"VENTANA DEL JUEGO"
		self.ventana = pg.display.set_mode(dimenciones)
		pg.display.set_caption(titulo)
		pg.display.toggle_fullscreen()

		self.clock = pg.time.Clock()
		self.tipo_fuente = "img/Fighting Spirit 2.ttf"
		self.Sound_Menu = pg.mixer.Sound("Sounds/Menu.ogg")

		"VARIABLES"
		self.Menu_on = True
		self.inMenu = True
		self.menuActual = 0
		self.opcionOpciones = 1
		self.opcionesVidas = 3

		self.mandos=[]
		self.mandos_on = False
		self.num_mandos = 0

		"PANTALLA INICIO"
		self.pantallaInicio = load_image("Inicio.png", "img", alpha=False)

		"VARIABLES MENU PRINCIPAL"
		self.menuPrincipal = load_image("MenuScreen.png", "img", alpha=False)
		self.cursor = load_image("10.png", "img/cursor", alpha=False)
		self.pos_cursorMenu = 230
		self.opcionMenu= 1

		self.menuOpciones = load_image("MenuOpciones.png", "img", alpha=False)
		self.menuAyuda= load_image("MENU AYUDA.png", "img", False)

	def run(self):
		self.Sound_Menu.play(-1)
		self.Sound_Menu.set_volume(.5)
		self.verificador_joystick()
		while self.inMenu:
			self.clock.tick(FPS)
			self.event()
			self.draw()
		while self.s.Seleccion_on:
			self.s.run()

	def event(self):
		"EVENTOS DEL MENU"
		for event in pg.event.get():
			if self.inMenu:
				self.keys = pg.key.get_pressed()
				if event.type == pg.QUIT:
					sys.exit()
				if self.menuActual == 0:
					if event.type == pg.KEYDOWN or event.type == pg.JOYBUTTONDOWN:
						self.menuActual = 1
				elif self.menuActual == 1:
					if self.keys[K_UP] or self.keys[K_w] or (self.mandos_on == True and (self.mandos[0].get_axis(1) == -1)):
						if self.opcionMenu > 1:
							self.opcionMenu -= 1
							self.pos_cursorMenu -= 50
					if self.keys[K_DOWN] or self.keys[K_s] or (self.mandos_on == True and (self.mandos[0].get_axis(1) > 0.1)):
						if self.opcionMenu < 4:
							self.opcionMenu += 1
							self.pos_cursorMenu += 50
					if self.keys[K_ESCAPE] or (self.mandos_on == True and (event.type == pg.JOYBUTTONDOWN and self.mandos[0].get_button(1) == 1)):
						self.menuActual = 0
						self.opcionMenu = 1
						self.pos_cursorMenu = 230
					if self.keys[K_RETURN] or (self.mandos_on == True and (event.type == pg.JOYBUTTONDOWN and self.mandos[0].get_button(2) == 1)):
						if self.opcionMenu == 1:
							self.inMenu = False
							self.s = Seleccion(self)
						elif self.opcionMenu == 2:
							self.menuActual = 2
						elif self.opcionMenu == 3:
							self.menuActual= 3
						elif self.opcionMenu == 4:
							pg.quit()
						self.opcionMenu = 1
						self.pos_cursorMenu = 230
				elif self.menuActual == 2:
					if self.keys[K_DOWN] and self.opcionOpciones < 2:
						self.opcionOpciones +=1
					elif self.keys[K_UP] and self.opcionOpciones > 1:
						self.opcionOpciones -=1
					if self.opcionOpciones == 1:
						if self.keys[K_LEFT] and self.opcionesVidas > 1:
							self.opcionesVidas -=1
						elif self.keys[K_RIGHT] and self.opcionesVidas < 7:
							self.opcionesVidas +=1
					if self.opcionOpciones == 2 and self.keys[K_RETURN]:
						self.menuActual = 1
				elif self.menuActual == 3:
					if event.type == pg.KEYDOWN or event.type == pg.JOYBUTTONDOWN:
						self.menuActual = 1


	def draw(self):
		if self.inMenu:
			if self.menuActual == 0:
				self.ventana.blit(self.pantallaInicio,(0,0))
				self.dibujar_texto("PRESS ANY KEY", 20, BLACK, ancho_ventana/2, alto_ventana/2)
			elif self.menuActual == 1:
				self.ventana.blit(self.menuPrincipal, (0, 0))
				self.ventana.blit(self.cursor, (400, self.pos_cursorMenu))
			elif self.menuActual == 2:
				self.ventana.blit(self.menuOpciones, (0,0))
				self.dibujar_texto("Vidas actuales = "+str(self.opcionesVidas), 24, WHITE, 400,400)
				self.dibujar_texto("Volver", 24, WHITE, 400, 500)
				self.ventana.blit(self.cursor, (350, 300+self.opcionOpciones*100))
			elif self.menuActual== 3:
				self.ventana.blit(self.menuAyuda, (0,0))

		pg.display.flip()

	def verificador_joystick(self):
		joystick_count = pg.joystick.get_count()
		if joystick_count != 0:
			self.mandos_on = True
			self.num_mandos = joystick_count
			for i in range(joystick_count):
				joystick = pg.joystick.Joystick(i)
				self.mandos.append(joystick)
				joystick.init()
		else:
			print("No hay mandos conectados")

	def dibujar_texto(self, texto, tamaño, color, x, y):
		"IMPRIME TEXTOS"
		fuente = pg.font.Font(self.tipo_fuente, tamaño)
		text_surface = fuente.render(texto, True, color)
		text_rect = text_surface.get_rect()
		text_rect.midtop =(x, y)
		self.ventana.blit(text_surface, text_rect)



	




