#!/usr/bin/env python3
import sys
 
import pygame

from settings import Settings

from ship import Ship

def run_game():
    # initialixes the game and creates a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
        ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Создание коробля.
    ship = Ship(screen)

    # Starting the main game loop
    while True:
      #  Tracking keyboard and mouse events
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

      # The screen is redrawn on each pass of the loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Display the last drawn screen
        pygame.display.flip()
run_game()
