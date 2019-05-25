import pygame
from pygame.locals import *
import os, sys


class Update:
    def __init__(self, settings, level):
        self.level = level
        # RETRIEVE POSITIONS
        self.player_pos = self.level.player_position
        self.gk_pos = self.level.gatekeeper_position
        self.wall_pos = self.level.get_wall_positions
        self.item_obj_position = self.level.get_item_obj_position
        self.settings = settings

        # SCREEN
        self.screen = pygame.display.set_mode((self.settings.level_size, self.settings.level_size))

        self.main_dir = os.path.split(os.path.abspath(__file__))[0]
        self.data_dir = os.path.join(self.main_dir, 'data')

        # LOAD IMAGES
        self.bg_image, self.bg_rect = Update.load_image(self, 'background.jpg')
        self.player_image, self.player_rect = Update.load_image(self, 'MacGyver.png')
        self.gk_image, self.gk_rect = Update.load_image(self, 'gatekeeper.png')
        self.wall_image, self.wall_rect = Update.load_image(self, 'wall.jpg')
        self.aiguille_image, self.aiguille_rect = Update.load_image(self, 'aiguille.png')
        self.seringue_image, self.seringue_rect = Update.load_image(self, 'seringue.png')
        self.ether_image, self.ether_rect = Update.load_image(self, 'ether.png')

    def update_screen(self):
        self.screen.blit(self.bg_image, self.bg_rect)

        for position in self.wall_pos:
            wall_y_pos, wall_x_pos = position
            wall_y_pos = wall_y_pos * self.settings.size_sprite
            wall_x_pos = wall_x_pos * self.settings.size_sprite
            self.screen.blit(self.wall_image, (wall_x_pos, wall_y_pos))

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

    def update_item(self):
        for item in self.item_obj_position.keys():
            if item == "aiguille":
                Update.update_aiguille(self)
            elif item == "ether":
                Update.update_ether(self)
            elif item == "seringue":
                Update.update_seringue(self)

    def update_aiguille(self):
        position = Update.position_corrector(self, "aiguille")
        self.screen.blit(self.aiguille_image, position)

    def update_ether(self):
        position = Update.position_corrector(self, "ether")
        self.screen.blit(self.ether_image, position)

    def update_seringue(self):
        position = Update.position_corrector(self, "seringue")
        self.screen.blit(self.seringue_image, position)

    def position_corrector(self, item):
        position = self.item_obj_position[item]
        position_y, position_x = position
        position_y = position_y * self.settings.size_sprite
        position_x = position_x * self.settings.size_sprite
        return (position_x, position_y)

    def victory_show(self):
        pass

    def fail_show(self):
        pass
