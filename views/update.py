import pygame
from pygame.locals import *
import os, sys


class Update:
    def __init__(self, settings, level):
        self.level = level
        self.player_pos = self.level.player_position
        self.settings = settings

        # SELF SCREEN
        self.screen = pygame.display.set_mode((self.settings.level_size, self.settings.level_size))

        self.main_dir = os.path.split(os.path.abspath(__file__))[0]
        self.data_dir = os.path.join(self.main_dir, 'data')

        # LOAD IMAGES
        self.bg_image, self.bg_rect = Update.load_image(self, 'structures.png')
        self.player_image, self.player_rect = Update.load_image(self, 'MacGyver.png')

    def update_screen(self):
        self.screen.blit(self.bg_image, self.bg_rect)
        # pygame.display.flip()

    def update_player(self):
        if self.player_pos != self.level.player_position:
            Update.update_screen(self)
        self.player_pos = self.level.player_position
        pg_y, pg_x = self.player_pos
        self.screen.blit(self.player_image, (pg_x*self.settings.size_sprite, pg_y*self.settings.size_sprite))
        pygame.display.update()

    def load_image(self, name):
        fullname = os.path.join(self.data_dir, name)
        image = pygame.image.load(fullname)
        image = image.convert_alpha()
        return image, image.get_rect()
