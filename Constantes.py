import pygame as pg
from Sprites import *

#Constantes de pantalla
titulo= "Doggo Fighters"
ancho_ventana = 960
alto_ventana = 540
dimenciones = (ancho_ventana,alto_ventana)
FPS = 60

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Propiedades del jugador
aceleracion = 0.5
friccion = -0.15
gravedad = 0.7
salto = 11.5

vec = pg.math.Vector2

"Variables de jugadores"
"Player1"
P1_Der = pg.K_d 
P1_Izq = pg.K_a
P1_Dir = True
P1_respawn = 200
P1_vidas = 0

"PLayer2"
P2_Der = pg.K_RIGHT
P2_Izq = pg.K_LEFT
P2_Dir = False
P2_respawn = 700
P2_vidas = 0

pate= 'Personajes/PateSheet.png'
choco= 'Personajes/ChocoSheet.png'
rayo= 'Personajes/LazerSheet.png'
titi= 'Personajes/TitiSheet.png'
solrac= 'Personajes/SolracSheet.png'








    






