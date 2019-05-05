"""Here the main game runs"""

from models.level import Level
from models.position import Position
from models.player import Player
from controllers.keyboard import KeyboardInputs
from views.update import Update
from settings import Settings

import pygame


def run_game():
    pygame.init()
    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("McGyver")

    level = Level("models/map.txt")
    position = Position(1, 1)
    player = Player(level)
    print("Player initial position =", player.position)
    chk_event = KeyboardInputs(player)
    updater = Update(settings, screen)

    while True:
        chk_event.check_events()
        updater.update_screen()


if __name__ == "__main__":
    run_game()
