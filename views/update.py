import pygame
from pygame.locals import *
import os, sys

class Update:
    def __init__(self, settings, level, player):
        self.level = level
        self.player = player
        # RETRIEVE POSITIONS
        self.player_pos = self.level.player_position
        self.gk_pos = self.level.gatekeeper_position
        self.wall_pos = self.level.get_wall_positions
        self.item_obj_position = self.level.get_item_obj_position
        self.settings = settings

        # SCREEN
        self.screen = pygame.display.set_mode(
            (self.settings.level_size, self.settings.level_size + self.settings.size_sprite))
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
        self.bbar_image, self.bbar_rect = Update.load_image(self, 'bottombar.png')
        self.victory_image, self.victory_rect = Update.load_image(self, 'victory.png')
        self.fail_image, self.fail_rect = Update.load_image(self, 'fail.png')

        self.picked_position = [(128, 480), (160, 480), (192, 480)]

    def update_screen(self):
        self.screen.blit(self.bg_image, self.bg_rect)
        self.screen.blit(self.bbar_image, (0, self.settings.level_size))
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
        item_list = list(self.item_obj_position.keys())
        if "aiguille" in item_list:
            a_position = Update.position_corrector(self, "aiguille")
            Update.display_item(self, a_position, self.aiguille_image, False)
        elif "aiguille" not in item_list:
            Update.display_item(self, self.picked_position[0], self.aiguille_image, True)

        if "ether" in item_list:
            a_position = Update.position_corrector(self, "ether")
            Update.display_item(self, a_position, self.ether_image, False)
        elif "ether" not in item_list:
            Update.display_item(self, self.picked_position[1], self.ether_image, True)

        if "seringue" in item_list:
            a_position = Update.position_corrector(self, "seringue")
            Update.display_item(self, a_position, self.seringue_image, False)
        elif "seringue" not in item_list:
            Update.display_item(self, self.picked_position[2], self.seringue_image, True)

    def display_item(self, position, item_name=None, picked=False):
        if not picked:
            self.screen.blit(item_name, position)
        else:
            self.screen.blit(item_name, position)

    def position_corrector(self, item):
        position = self.item_obj_position[item]
        position_y, position_x = position
        position_y = position_y * self.settings.size_sprite
        position_x = position_x * self.settings.size_sprite
        return (position_x, position_y)

    def ending_display(self):
        if self.player.victory_condition is None:
            return True
        elif self.player.victory_condition:
            self.screen.blit(self.victory_image, (0,0))
            pygame.display.update()
            return False
        else:
            self.screen.blit(self.fail_image, (0,0))
            pygame.display.update()
            return False