"""This is where everything is displayed."""
import pygame
import os


class Update:
    """
    This is the main class used to display.
    """

    def __init__(self, settings, level, player):
        """
        Args:
            settings (obj): instance of settings.
            level (obj): instance of level.
            player (obj): instance of player.

        Attributes:
            level (obj): instance of level.
            player (obj): instance of player.
            player_pos (tuple): the player position.
            gk_pos (tuple): the gate keeper position.
            wall_pos  (list):the wall list of position.
            item_obj_position (dict): the dictionary item to position.
            settings (obj): settings instance.
            screen  (pygame surface): the main screen object used.
            main_dir (str): used to give the main directory.
            data_dir (str): used to give the data directory.
            bg_image  (pygame surface): the background image.
            bg_rect (pygame surface): the pygame rectangle from the image
            gk_image  (pygame surface): the gatekeeper image.
            wall_image  (pygame surface): the wall image.
            aiguille_image  (pygame surface):the aiguille image.
            seringue_image  (pygame surface):the seringue image.
            ether_image  (pygame surface): the ether image.
            bbar_image  (pygame surface):the bottom bar image.
            victory_image  (pygame surface): the victory image.
            fail_image  (pygame surface): the fail image.
            picked_position  (list): the three positions for the item
            at the bottom of the screen for the picked up items.

        """
        self.level = level
        self.player = player
        # RETRIEVE POSITIONS
        self.player_pos = self.level.player_position
        self.gk_pos = self.level.get_finish_position
        self.wall_pos = self.level.get_wall_positions
        self.item_obj_position = self.level.get_item_obj_position
        self.settings = settings

        # SCREEN
        self.screen = pygame.display.set_mode(
            (self.settings.level_size,
             self.settings.level_size + self.settings.size_sprite))
        self.main_dir = os.path.split(os.path.abspath(__file__))[0]
        self.data_dir = os.path.join(self.main_dir, 'data')

        # LOAD IMAGES
        self.bg_image = Update.load_image(self, 'background.jpg')
        self.bg_rect = self.bg_image.get_rect()
        self.player_image = Update.load_image(self, 'MacGyver.png')
        self.gk_image = Update.load_image(self, 'gatekeeper.png')
        self.wall_image = Update.load_image(self, 'wall.jpg')
        self.aiguille_image = Update.load_image(self, 'aiguille.png')
        self.seringue_image = Update.load_image(self, 'seringue.png')
        self.ether_image = Update.load_image(self, 'ether.png')
        self.bbar_image = Update.load_image(self, 'bottombar.png')
        self.victory_image = Update.load_image(self, 'victory.png')
        self.fail_image = Update.load_image(self, 'fail.png')

        self.picked_position = [(128, 480), (160, 480), (192, 480)]

    def update_screen(self):
        """
        Display the background, the bottom black menu and the walls
        """

        self.screen.blit(self.bg_image, self.bg_rect)
        self.screen.blit(self.bbar_image, (0, self.settings.level_size))
        for position in self.wall_pos:
            # We adapt the coordinates for pygame
            wall_y_pos, wall_x_pos = position
            wall_y_pos = wall_y_pos * self.settings.size_sprite
            wall_x_pos = wall_x_pos * self.settings.size_sprite
            self.screen.blit(self.wall_image, (wall_x_pos, wall_y_pos))

    def update_player(self):
        """
        Update the player display when moving.
        """
        if self.player_pos != self.level.player_position:
            # Reset the display to remove old position of player
            Update.update_screen(self)
        self.player_pos = self.level.player_position
        pg_y, pg_x = self.player_pos
        self.screen.blit(
            self.player_image,
            (pg_x * self.settings.size_sprite,
             pg_y * self.settings.size_sprite)
        )
        pygame.display.update()

    def load_image(self, name):
        """
        The main method to load images for pygame.
        """
        fullname = os.path.join(self.data_dir, name)
        image = pygame.image.load(fullname)
        image = image.convert_alpha()
        return image

    def update_gatekeeper(self):
        """
        Display the gate keeper.
        """
        gk_y_pos, gk_x_pos = self.gk_pos
        self.screen.blit(
            self.gk_image,
            (gk_x_pos * self.settings.size_sprite,
             gk_y_pos * self.settings.size_sprite)
        )
        pygame.display.update()

    def update_item(self):
        """
        This will display or not the item providing they were picked up
        or not. It tests the dictionary if the item exists or not.
        """
        item_list = list(self.item_obj_position.keys())
        if "aiguille" in item_list:
            a_position = Update.position_corrector(self, "aiguille")
            Update.display_item(self, a_position, self.aiguille_image, False)
        elif "aiguille" not in item_list:
            Update.display_item(self,
                                self.picked_position[0],
                                self.aiguille_image, True)

        if "ether" in item_list:
            a_position = Update.position_corrector(self, "ether")
            Update.display_item(self, a_position, self.ether_image, False)
        elif "ether" not in item_list:
            Update.display_item(self,
                                self.picked_position[1],
                                self.ether_image, True)

        if "seringue" in item_list:
            a_position = Update.position_corrector(self, "seringue")
            Update.display_item(self, a_position, self.seringue_image, False)
        elif "seringue" not in item_list:
            Update.display_item(self,
                                self.picked_position[2],
                                self.seringue_image, True)

    def display_item(self, position, item_name=None, picked=False):
        """
        Args:
            position (tuple): the position of the item.
            item (obj): the attributes pygame image.
            picked (bool): False if not picked, True if picked up by
                         the player.
        """
        if not picked:
            self.screen.blit(item_name, position)
        else:
            self.screen.blit(item_name, position)

    def position_corrector(self, item):
        """
        The method will adjust the position to fit pygame standards.
        Returns:
             tuple: x and y position corrected
        """
        position = self.item_obj_position[item]
        position_y, position_x = position
        position_y = position_y * self.settings.size_sprite
        position_x = position_x * self.settings.size_sprite
        return (position_x, position_y)

    def ending_display(self):
        """
        This will display the ending, victory or fail.
        Returns:
             Bool: True when the player has not met the gatekeeper
                   False when he meets him
        """
        if self.player.victory_condition is None:
            return True
        elif self.player.victory_condition:
            self.screen.blit(self.victory_image, (0, 0))
            pygame.display.update()
            return False
        else:
            self.screen.blit(self.fail_image, (0, 0))
            pygame.display.update()
            return False
