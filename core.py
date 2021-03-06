"""Here the main game runs"""
import pygame
from models.level import Level
from models.position import Position
from models.player import Player
from models.item import Item
from controllers.keyboard import KeyboardInputs
from views.update import Update
from settings import Settings


def run_game():
    """
    The main function.
    Here we intanciate every class.
    Then runs the loop for the game to runs.
    """
    # Pygame initialization.
    pygame.init()
    pygame.display.set_caption("McGyver")

    # Instanciation.
    mcsettings = Settings()
    level = Level("models/map.txt")
    item = Item(level)
    position = Position(1, 1)
    player = Player(level, mcsettings)
    chk_event = KeyboardInputs(player)
    updater = Update(mcsettings, level, player)

    updater.update_screen()

    running_state = True
    while running_state:
        chk_event.check_events()
        player.pickup_item()
        updater.update_player()
        updater.update_gatekeeper()
        updater.update_item()
        player.check_victory_condition()
        if updater.ending_display():
            continue
        else:
            while True:
                chk_event.check_events()


if __name__ == "__main__":
    run_game()
