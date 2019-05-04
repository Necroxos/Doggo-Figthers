# trabajo con sprites
import os, pygame as pg,sys
from Constantes import *

#cargador sprites
def load_image(nombre, dir_imagen, alpha=False):
    ruta = os.path.join(dir_imagen, nombre)
    if dir_imagen.strip().split("/") == 2:
        direcciones = dir_imagen.strip().split("/")
        dir1 = direcciones[0]
        dir2 = direcciones[1]
        ruta = os.path.join(dir1, dir2, nombre)
    else:
        ruta = os.path.join(dir_imagen, nombre)
    try:
        image = pg.image.load(ruta)
    except:
        print("Error, no se puede cargar la imagen: " + ruta)
        sys.exit(1)
    if alpha is False:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image
    
#Clase carga Spritesheet
class spritesheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pg.image.load(filename).convert()
        except :
            print("Error, no se puede cargar la imagen: " + filename)
            sys.exit(1)
#sprites derecha
    #Carga una imagen especifica en un rectangulo especifico
    def image_at_der(self, rectangle, colorkey = None):
        "Carga imagen respecto x,y,ancho, alto"
        rect = pg.Rect(rectangle)
        image = pg.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pg.RLEACCEL)
        return image
    #carga imagenes y las devuelve com lista
    def images_at_der(self, rects, colorkey = None):
        "Carga multiples imagenes, proporcionadas por lista de coordenadas"
        return [self.image_at_der(rect, colorkey) for rect in rects]
    #Carga tira de imagenes
    def load_strip_der(self, rect, image_count, colorkey = None):
        "carga tira de imagenes y las devuelve como lista"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at_der(tups, colorkey)
#Sprites izquierda
    def image_at_izq(self, rectangle, colorkey = None):
            "Carga imagen respecto x,y,ancho, alto"
            rect = pg.Rect(rectangle)
            image = pg.Surface(rect.size).convert()
            image.blit(self.sheet, (0, 0), rect)
            image = pg.transform.flip(image, True, False)

            if colorkey is not None:
                if colorkey is -1:
                    colorkey = image.get_at((0,0))
                image.set_colorkey(colorkey, pg.RLEACCEL)
            return image
    #carga imagenes y las devuelve com lista
    def images_at_izq(self, rects, colorkey = None):
        "Carga multiples imagenes, proporcionadas por lista de coordenadas"
        return [self.image_at_izq(rect, colorkey) for rect in rects]
    #Carga tira de imagenes
    def load_strip_izq(self, rect, image_count, colorkey = None):
        "carga tira de imagenes y las devuelve como lista"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at_izq(tups, colorkey)

#Clase carga animacion Spritesheet
class SpriteStripAnim(object):
    "Animador de Sprites"
    """
    La clase propociona un iterador (metodos inter() y next())
    y un metodo __add__() que une las tiras de imagenes.
    """
    def __init__(self, filename, rect, count, colorkey=None, loop=False, frames=1, direccion= None):
        "Constructor de SpriteAnim"
        """
        filename, rect, count y colorkey son argumentos" 
        usados por SpriteSheet.load_tira

        loop es un boolean que, cuando es True , activa el metodo next()
        si es False, proboca que StopIteration

        frames es el numero de ticks para reiniciar iterador de tira de imagenes
        """
        self.filename = filename
        ss = spritesheet(filename)
        if direccion is not None:
            if direccion == True:
                self.images = ss.load_strip_der(rect, count, colorkey)
            elif direccion == False:
                self.images = ss.load_strip_izq(rect, count, colorkey)

        self.i = 0
        self.loop = loop
        self.frames = frames
        self.f = frames
    def iter(self):
        self.i = 0
        self.f = self.frames
        return self
    def next(self):
        if self.i >= len(self.images):
            if not self.loop:
                raise StopIteration
            else:
                self.i = 0
        image = self.images[self.i]
        self.f -= 1
        if self.f == 0:
            self.i += 1
            self.f = self.frames
        return image
    def __add__(self, ss):
        self.images.extend(ss.images)
        return self
