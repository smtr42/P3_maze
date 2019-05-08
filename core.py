"""Here the main game runs"""
import pygame
import settings

from models.level import Level
from models.position import Position
from models.player import Player
from models.gatekeeper import GateKeeper
from models.item import Item
from controllers.keyboard import KeyboardInputs
from views.update import Update
from settings import Settings


def run_game():
    pygame.init()
    mcsettings = Settings()

    pygame.display.set_caption("McGyver")

    # Create and load map
    level = Level("models/map.txt")
    # Get random position of items
    item = Item(level)

    position = Position(1, 1)

    # Create player and guard
    player = Player(level, mcsettings)
    gatekeeper = GateKeeper(level)

    print("Player initial position =", player.position)

    #
    chk_event = KeyboardInputs(player)
    updater = Update(mcsettings)

    running_state = True
    while running_state:
        chk_event.check_events()
        player.pickup_item()
        updater.update_screen()
        if player.check_victory_condition() == False:
            break
        else:
            continue


if __name__ == "__main__":
    run_game()
