import pygame as pg
from Constantes import *

class Plataform(pg.sprite.Sprite):
    def __init__(self, x, y, p_ancho, p_alto):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((p_ancho, p_alto))
        self.image.set_colorkey(BLACK)
        # self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
