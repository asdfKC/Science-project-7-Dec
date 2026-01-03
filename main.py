import pygame  
import sys
import math


pygame.init()



width = 800
height = 900 
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("WaterSaver")


clock = pygame.time.Clock()

def draw_tiled(surface, image):
    iw, ih = image.get_width(), image.get_height()
    for x in range(0, surface.get_width(), iw):
        for y in range(0, surface.get_height(), ih):
            surface.blit(image, (x, y))

background = pygame.image.load("images/grass.png").convert_alpha()

    
game_loop = True

while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

    draw_tiled(window , background)

    
    

    pygame.display.update()
    clock.tick(60)