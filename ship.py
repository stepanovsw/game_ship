#!/usr/bin/env python3
import pygame

class Ship():

    def __init__(self, screen):
        """ Инициализирует корабль """
        self.screen = screen

        # Загрузка изображения коробля
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Каждый новый корабль появляеться у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
       
    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
