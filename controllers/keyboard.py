"""Every input is taken care of and sent
to the appropriate object"""

import sys
import pygame


class KeyboardInputs:

    def __init__(self, player):
        self.player = player

    def check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player.move("right")
                if event.key == pygame.K_LEFT:
                    self.player.move("left")
                if event.key == pygame.K_UP:
                    self.player.move("up")
                if event.key == pygame.K_DOWN:
                    self.player.move("down")
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
