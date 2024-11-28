from raindrop import Raindrop
from random import randint
import pygame
def create_rain(screen,raindrops):
    screen_rect = screen.get_rect()
    raindrop = Raindrop(screen)
    drop_width = raindrop.drop_rect.width
    number_x = get_number_x(screen,drop_width)
    number_y = get_number_y(screen_rect,raindrop)
    for num_y in range(number_y):
        for num_x in range(number_x):
            create_raindrop(raindrops,screen,num_x,num_y)

def get_number_x(screen,drop_width):
    screen_rect = screen.get_rect()
    available_x = screen_rect.width - 6
    number_x = int(available_x/(2*drop_width))
    return number_x
def get_number_y(screen_rect,raindrop):
    available_y = screen_rect.height - 6
    number_y = int(available_y/(2*raindrop.drop_rect.height))
    return number_y
def create_raindrop(raindrops,screen,num_x,num_y):
    raindrop = Raindrop(screen)
    drop_x = 48 + (2*raindrop.drop_rect.width*num_x)
    drop_y = 3 + (2*raindrop.drop_rect.height*num_y)
    raindrop.drop_rect.x = drop_x
    raindrop.drop_rect.y = drop_y
    raindrops.add(raindrop)
def create_rain_row(screen,drop_width,raindrops):
    number_x = get_number_x(screen,drop_width)
    for num in range(number_x):
        drop = Raindrop(screen)
        drop.drop_rect.x =  48 + (2*drop.drop_rect.width*num)
        raindrops.add(drop)
def rain_fall(raindrops,screen):
    screen_rect = screen.get_rect()
    for raindrop in raindrops:
        if raindrop.drop_rect.y >= screen_rect.bottom:
            raindrops.remove(raindrop)
    if len(raindrops) == 24:
        drrop = Raindrop(screen)
        create_rain_row(screen,drrop.drop_rect.width,raindrops)
def update_screen(screen,raindrops):
    screen.fill((0,0,0))
    for raindrop in raindrops:
        raindrop.blit_me()
    pygame.display.flip()