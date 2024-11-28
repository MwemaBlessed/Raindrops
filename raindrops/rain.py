import pygame
import sys
from pygame.sprite import Group
import functions as f 
def run_rain():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption('Rain')
    raindrops = Group()
    f.create_rain(screen,raindrops)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
        for raindrop in raindrops:
            raindrop.update()
        f.rain_fall(raindrops,screen)
        f.update_screen(screen,raindrops)  
run_rain()