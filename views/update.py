import pygame
from pygame.locals import *
import os, sys


class Update:
    def __init__(self, settings, level):
        self.level = level
        self.player_pos = self.level.player_position
        self.gk_pos = self.level.gatekeeper_position
        self.wall_pos = self.level.get_wall_positions
        print(self.wall_pos)
        self.settings = settings

        # SELF SCREEN
        self.screen = pygame.display.set_mode((self.settings.level_size, self.settings.level_size))

        self.main_dir = os.path.split(os.path.abspath(__file__))[0]
        self.data_dir = os.path.join(self.main_dir, 'data')

        # LOAD IMAGES
        self.bg_image, self.bg_rect = Update.load_image(self, 'background.jpg')
        self.player_image, self.player_rect = Update.load_image(self, 'MacGyver.png')
        self.gk_image, self.gk_rect = Update.load_image(self, 'gatekeeper.png')
        self.wall_image, self.wall_rect = Update.load_image(self, 'wall.jpg')

    def update_screen(self):
        self.screen.blit(self.bg_image, self.bg_rect)

        for position in self.wall_pos:
            wall_y_pos, wall_x_pos = position
            print(position)
            self.screen.blit(self.wall_image, (wall_x_pos * self.settings.size_sprite, wall_y_pos* self.settings.size_sprite))


    def update_player(self):
        if self.player_pos != self.level.player_position:
            Update.update_screen(self)
        self.player_pos = self.level.player_position
        pg_y, pg_x = self.player_pos
        self.screen.blit(self.player_image, (pg_x * self.settings.size_sprite, pg_y * self.settings.size_sprite))
        pygame.display.update()

    def load_image(self, name):
        fullname = os.path.join(self.data_dir, name)
        image = pygame.image.load(fullname)
        image = image.convert_alpha()
        return image, image.get_rect()

    def update_gatekeeper(self):
        gk_y_pos, gk_x_pos = self.gk_pos
        self.screen.blit(self.gk_image,
                         (gk_x_pos * self.settings.size_sprite, gk_y_pos * self.settings.size_sprite))
        pygame.display.update()

    def update_item1(self):
        pass

    def update_item2(self):
        pass

    def update_item3(self):
        pass
