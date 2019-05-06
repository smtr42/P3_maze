"""Here the main game runs"""

from models.level import Level
from models.position import Position
from models.player import Player
from models.gatekeeper import GateKeeper
from models.item import Item
from controllers.keyboard import KeyboardInputs
from views.update import Update
from settings import Settings

import pygame


def run_game():
    pygame.init()
    settings = Settings()

    pygame.display.set_caption("McGyver")

    # Create and load map
    level = Level("models/map.txt")
    # Get random position of items
    item = Item(level)

    position = Position(1, 1)

    # Create player and guard
    player = Player(level)
    gatekeeper = GateKeeper(level)

    print("Player initial position =", player.position)

    #
    chk_event = KeyboardInputs(player)
    updater = Update(settings)

    while True:
        chk_event.check_events()
        player.pickup_item()
        updater.update_screen()


if __name__ == "__main__":
    run_game()
