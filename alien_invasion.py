import sys
import pygame
from settings import Settings
# from pygame.locals import *
from ship import Ship
import get_functions as gf
from pygame.sprit import Group

def run_game():
    pygame.init()

    ai_settings = Settings()
    
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height),0,32)

    ship = Ship(ai_settings,screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()
    pygame.display.set_caption("飞机大战")
    



    while True:
        
        gf.update_screen(ai_settings,screen,ship)

        gf.check_events(ship)

        ship.update()
if __name__ == "__main__":
    run_game()