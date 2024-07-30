import pygame
import sys
from ship import Ship
from settings import Settings
import game_functions as gf
def run_game():
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship = Ship(screen)
    pygame.display.set_caption('Alien Invasion')
    while True:
        gf.check_events()
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()
run_game()