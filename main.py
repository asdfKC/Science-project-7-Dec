import pygame  
import sys
import math


pygame.init()



width = 600
height = 700 
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("WaterSaver")


clock = pygame.time.Clock()

def draw_tiled(surface, image):
    iw, ih = image.get_width(), image.get_height()
    for x in range(0, surface.get_width(), iw):
        for y in range(0, surface.get_height(), ih):
            surface.blit(image, (x, y))

background = pygame.image.load("images/grass.png").convert_alpha()
player = pygame.image.load("images/Character_walk_1.png").convert_alpha()
player_rect = player.get_rect(topleft=(300, 350))
player_speed = 5

imgwidth = player.get_width() // 5
imgheight = player.get_height() // 5
new_size = (imgwidth, imgheight)

player = pygame.transform.scale(player, new_size)

game_loop = True

while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

    draw_tiled(window , background)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed

    window.blit(player, player_rect)

    pygame.display.update()
    clock.tick(60)