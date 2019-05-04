# Módulos
import sys, pygame, os
from pygame.locals import *

# Constantes
WIDTH = 1000
HEIGHT = 1000

def load_image(nombre, dir_imagen, alpha=False):
    ruta = os.path.join(dir_imagen, nombre)
    try:
        image = pygame.image.load(ruta)
    except:
        print("Error, no se puede cargar la imagen: " + ruta)
        sys.exit(1)
    image = image.convert()
    if alpha:
        color = image.get_at((0,0))
        image.set_colorkey(color, pygame.RLEACCEL)
    return image

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pruebas Pygame")

    image  = load_image("TitiSheet2.png","",True)
    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)

        screen.fill((100,50,50))        
        screen.blit(image, (0,0))
        pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    main()
